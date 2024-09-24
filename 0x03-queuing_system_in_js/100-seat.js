import { createClient } from 'redis';
import { promisify } from 'util';
import { createQueue } from 'kue';
import express from 'express';

const app = express();
const queue = createQueue();
const client = createClient();
const asyncGet = promisify(client.get).bind(client);
let reservationEnabled = true;
const PORT = 1245;

// Redis
// initiate available seats to 50
client.set('available_seats', 50);

client.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err.message}`);
});

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

// Functions
function reserveSeat(number) {
  client.set('available_seats', number);
}

async function getCurrentAvailableSeats() {
  const availableSeats = await asyncGet('available_seats');
  return availableSeats ?? 0;
}

// Express app
app.listen(PORT, () => {
  console.log(`Server listening on port: ${PORT}`);
});

// GET /process
app.get('/process', (_req, res) => {
  queue.process('reserve_seat', async (_job, done) => {
    const availableSeats = await getCurrentAvailableSeats();
    const newAvailableSeats = Number(availableSeats) - 1;
    reserveSeat(newAvailableSeats);
    if (newAvailableSeats == 0) {
      reservationEnabled = false;
    }
    if (newAvailableSeats >= 0) {
      done();
    } else {
      done(new Error('Not enough seats available'));
    }
  });
  res.json({ 'status': 'Queue processing' });
});

// GET /available_seats
app.get('/available_seats', async (_req, res) => {
  const available_seats = await asyncGet('available_seats') ?? '0';
  res.json({ 'numberOfAvailableSeats': available_seats });
});

// GET /reserve_seat
app.get('/reserve_seat', (_req, res) => {
  if (!reservationEnabled) {
    return res.json({ 'status': 'Reservation are blocked' });
  }
  const job = queue.create('reserve_seat', { title: 'seat_reservation' });
  job
    .on('complete', () => {
      console.log(`Seat reservation job ${job.id} completed`);
    })
    .on('failed', (err) => {
      console.log(`Seat reservation job ${job.id} failed:`, err.message ?? err.toString());
    })
  job.save((err) => {
    if (err) {
      res.json({ 'status': 'Reservation failed' });
    } else {
      res.json({ 'status': 'Reservation in process' });
    }
  });
});
