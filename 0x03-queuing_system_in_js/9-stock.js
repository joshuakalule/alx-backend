import express from 'express';
import { createClient } from 'redis';
import { promisify } from 'util';

const app = express();
const PORT = 1245;
const client = createClient();

client.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err.message}`);
});

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

const listProducts = [
  { id: 1, name: 'Suitcase 250', price: 50, stock: 4 },
  { id: 2, name: 'Suitcase 450', price: 100, stock: 10 },
  { id: 3, name: 'Suitcase 650', price: 350, stock: 0 },
  { id: 4, name: 'Suitcase 1050', price: 550, stock: 5 }
];

function getItemById(id) {
  for (const obj of listProducts) {
    if (obj.id == id) {
      return obj;
    }
  }
  return null;
}

function reserveStockById(itemId, stock) {
  client.set(`item.${itemId}`);
}

async function getCurrentReservedStockById(itemId) {
  const getAsync = promisify(client.get).bind(client);
  const stock = await getAsync(`item.${itemId}`);
  // console.log(stock);
  return stock ? stock : 0;
}

app.listen(PORT, () => {
  console.log(`Server listening on port: ${PORT}`);
});

app.get('/list_products', (_req, res) => {
  res.json(listProducts);
})

app.get('/list_products/:itemId', async (req, res) => {
  const itemId = req.params.itemId;

  const currentStock = await getCurrentReservedStockById(itemId);
  const { name, price, stock } = getItemById(itemId) ?? {};
  const obj = {
    itemId,
    itemName: name,
    price,
    initialAvailableQuantity: stock,
    currentQuantity: currentStock
  }

  if (stock) {
    return res.json(obj);
  }
  return res.json({ "status": "Product not found" });
})

app.get('/reserve_product/:itemId', (req, res) => {
  const itemId = req.params.itemId;

  const item = getItemById(itemId);

  if (!item) {
    return res.json({ "status": "Product not found" });
  }
  if (item.stock < 1) {
    return res.json({ "status": "Not enough stock available", "itemId": itemId });
  }

  reserveStockById(itemId, 1);
  return res.json({ "status": "Reservation confirmed", "itemId": itemId });
})
