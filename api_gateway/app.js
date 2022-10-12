const express = require('express');
const crypto = require('crypto');
const app = express();
const { Sequelize, DataTypes } = require('sequelize');
require("dotenv").config({path: '../.env'})
const sequelize = new Sequelize(process.env.POSTGRES_URL)
const views = require('./views');

try {
    sequelize.authenticate();
    console.log('connceted');
}   catch (error) {
        console.error('not connceted', error);

}

const db = require("./models")(sequelize,DataTypes);
(async() => {
    db.sync();
})();

app.use(express.json());

hash = (key) => crypto.createHash('sha256').update(String(key)).digest('hex');

app.get('/api/images/:idd', (req,res) => {
    b = req.headers.authorization;
    const { idd } = req.params;
    hashes = hash(b);
    views.viewimage(req, res, hashes, db);
    console.log(b   , hash(b), idd );
});


app.post('/api/images/:idd', (req,res) => {
    b = req.headers.authorization;
    const { idd } = req.params;
    hashes = hash(b);
    views.postviewimage(req, res, hashes, db);
    console.log( b, hash(b), idd );
});


app.post('/api/savekeys', (req, res) => {
    views.savekey(req, res, db);  
});


app.listen(9000, () => console.log("server ready"));