import { createClient } from 'redis';

const publisher = createClient();

publisher.on('connect', () => {
  console.log('Redis client connected to the server');
});

publisher.on('error', err => {
  console.log(`Redis client not connected to the server: ${err.message}`);
});

function publishMessage(msg, time) {
  setTimeout(() => {
    console.log(`About to send ${msg}`);
    publisher.publish('holberton school channel', msg);
  }, time);
}

publishMessage("Holberton Student #1 starts course", 100);
publishMessage("Holberton Student #2 starts course", 200);
publishMessage("KILL_SERVER", 300);
publishMessage("Holberton Student #3 starts course", 400);
