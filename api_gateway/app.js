const express = require('express');
const crypto = require('crypto');
const app = express();
const { Sequelize, DataTypes } = require('sequelize');
require("dotenv").config({path: '../.env'})
const sequelize = new Sequelize(process.env.POSTGRES_URL)
const views = require('./views');
const multer = require('multer');

app.use(express.json());
const storage = multer.memoryStorage();
const uploads = multer({storage});
const image_stream = uploads.single('imagez');

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


hash = (key) => crypto.createHash('sha256').update(String(key)).digest('hex');

app.get('/api/images/:idd', (req,res) => {
    b = req.headers.authorization;
    const { idd } = req.params;
    hashes = hash(b);
    views.viewimage(req, res, hashes, db, idd);
    console.log(b   , hash(b), idd );
});


app.post('/api/images/:idd', (req, res) => {
    image_stream(req, res, (err) => {
        if (err instanceof multer.MulterError){
            return res.status(400).json({"status":false,"message":"invalid fieldname or error from your side"}); 
        } else if (err) {
            console.log(err);
        }
        b = req.headers.authorization;
        const { idd } = req.params;
        hashes = hash(b);
        views.postviewimage(req, res, hashes, db, idd);
        console.log( b, hash(b), idd );
    })
   
});


app.post('/api/savekeys', (req, res) => {
    views.savekey(req, res, db);  
});

app.put('/api/savekeys', (req, res) => {
    views.putkey(req, res, db);
});


app.listen(9000, () => console.log("server ready"));