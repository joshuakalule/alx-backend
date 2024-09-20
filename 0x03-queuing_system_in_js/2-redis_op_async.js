import { createClient, print as redisPrint } from 'redis';
import { promisify } from 'util';

const client = createClient();

client.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err.message}`);
});

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

async function setNewSchool(schoolName, value) {
  client.set(schoolName, value, redisPrint);
};

async function displaySchoolValue(schoolName) {
  const response = await promisify(client.get).bind(client)(schoolName);
  console.log(response);
};

async function main() {
  await displaySchoolValue('Holberton');
  await setNewSchool('HolbertonSanFrancisco', '100');
  await displaySchoolValue('HolbertonSanFrancisco');
}

client.on('connect', async () => {
  await main();
});
