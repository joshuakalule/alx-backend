import { createClient, print as redisPrint } from 'redis';

const client = createClient();

client.connect();

client.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err.message}`);
});

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

function setNewSchool(schoolName, value) {
  client.set(schoolName, value)
    .then(reply => console.log(`Reply: ${reply}`))
    .catch(err => console.log(`Error: ${err.message}`));
}

function displaySchoolValue(schoolName) {
  client.get(schoolName)
    .then(response => console.log(response))
    .catch(err => console.log(`Error: ${err.message}`));
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
