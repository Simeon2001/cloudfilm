const express = require('express');
const crypto = require('crypto');
const app = express();
const { Sequelize, DataTypes } = require('sequelize');
require("dotenv").config({path: '../.env'})
const sequelize = new Sequelize(process.env.POSTGRES_URL)
try {
    sequelize.authenticate();
    console.log('connceted');
}   catch (error) {
        console.error('not connceted', error);

}

const db = require("./models")(sequelize,DataTypes);

db.sync();

app.use(express.json());


hash = (key) => crypto.createHash('sha256').update(String(key)).digest('hex');

app.get('/hello', (req,res) => {
    b = req.headers.authorization,
    res.send(hash(b)),
    console.log(b   , hash(b) );
});

app.post('/api/savekeys', (req,res) => {
    if (req.headers.authorization == process.env.AUTH_TOKEN){

        const enc_private_key  = req.body.pri_key;
        const enc_public_key   = req.body.pub_key;
        const token   = req.body.token;
        if (enc_private_key.length == 0 | enc_public_key.length == 0){
            return res.status(401).json({"status": false,})
        }
        const key_data = {enc_private: enc_private_key, enc_public: enc_public_key, token: token};
        data = db.create(key_data)
        console.log(data.token);
        return res.status(200).json({"status": true,});
    }
    else {
        return res.status(406).json({"status": false,"message": "not authenticated"});
    }
});

app.listen(9000, () => console.log("server ready"));