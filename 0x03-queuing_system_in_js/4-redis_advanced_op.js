import { createClient, print as redisPrint } from 'redis';

const client = createClient();

client.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err.message}`);
});

function updateHash(hashName, fieldName, fieldValue) {
  client.HSET(hashName, fieldName, fieldValue, redisPrint);
}

function printHash (hashName) {
  client.HGETALL(hashName, (_err, reply) => console.log(reply));
};

const hashObj = {
  Portland: 50,
  Seattle: 80,
  'New York': 20,
  Bogota: 20,
  Cali: 40,
  Paris: 2,
};

function main() {
  for (const [field, value] of Object.entries(hashObj)) {
    updateHash('HolbertonSchools', field, value);
  }
  printHash('HolbertonSchools');
}

client.on('connect', () => {
  console.log('Redis client connected to the server');
  main();
});
