import { createClient, print as redisPrint } from 'redis';

const subscriber = createClient();

subscriber.on('connect', () => {
  console.log('Redis client connected to the server');
});

subscriber.on('error', err => {
  console.log(`Redis client not connected to the server: ${err.message}`);
});

subscriber.subscribe('holberton school channel');

subscriber.on('message', (err, msg) => {
  console.log(msg);
  if (msg === 'KILL_SERVER') {
    subscriber.unsubscribe('holberton school channel');
    subscriber.quit();
  }
});
