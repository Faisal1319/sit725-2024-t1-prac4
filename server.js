const express = require('express');
const path = require('path');
const MongoClient = require('mongodb').MongoClient;

const app = express();

// Serve static files from the 'public' directory
app.use(express.static(path.join(__dirname, 'public')));

// Define route to serve index.html by default
app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, 'public', 'index.html'));
});

// MongoDB connection
const url = 'mongodb+srv://Cluster0:Mohdfaisal%401319@atlascluster.tbt7zv3.mongodb.net/';
const dbName = 'sit725';

MongoClient.connect(url, { useNewUrlParser: true, useUnifiedTopology: true }, (err, client) => {
    if (err) {
        console.error('Failed to connect to the database:', err);
        return;
    }
    console.log('Connected successfully to the database');

    const db = client.db(dbName);

    // Now you can perform database operations using the 'db' object
    // For example, you can insert a document into a collection
    const collection = db.collection('server.js');
    collection.insertOne({ name: 'John', age: 30 }, (err, result) => {
        if (err) {
            console.error('Failed to insert document:', err);
            return;
        }
        console.log('Document inserted successfully:', result.ops[0]);
    });

    // Don't forget to close the connection when you're done
    // client.close(); // This should not be closed here if you want to keep the connection open
});

// Start the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});

