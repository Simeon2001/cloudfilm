require("dotenv").config({path: '../.env'})
const express = require('express');
const crypto = require('crypto');
const app = express();
const { Sequelize, DataTypes } = require('sequelize');
const sequelize = new Sequelize(process.env.POSTGRES_URL)
const views = require('./views');
const imgdesc = require('./imgdesc');
const multer = require('multer');

app.use(express.json());


// multer code for uploading
const storage = multer.memoryStorage();
const uploads = multer({storage});
const image_stream = uploads.single('imagez');


// sequalize code to connect with postgres db
try {
    sequelize.authenticate();
    console.log('database connected');
}   catch (error) {
        console.error('not connected', error);

}

const db = require("./models")(sequelize,DataTypes);
(async() => {
    db.sync();
})();


// function for hashing
hash = (key) => crypto.createHash('sha256').update(String(key)).digest('hex');


// request function for getting images base on id
app.get('/api/images/:idd', (req,res) => {
    b = req.headers.authorization;
    const { idd } = req.params;
    hashes = hash(b);
    views.viewimage(req, res, hashes, db, idd);
    console.log(b   , hash(b), idd );
});


// request function to add images 
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


// request function to save apikeys
app.post('/api/savekeys', (req, res) => {
    views.savekey(req, res, db);  
});


// request function to update apikeys
app.put('/api/savekeys', (req, res) => {
    views.putkey(req, res, db);
});


// request function to receive image and send to main ML api
app.post('/api/imagedeploy', (req, res) => {
    image_stream(req, res, (err) => {
        if (err instanceof multer.MulterError){
            return res.status(400).json({"status":false,"message":"invalid fieldname or error from your side"}); 
        } else if (err) {
            console.log(err);
        }
        imgdesc.desc_image(req, res);
    });
});


// request function to check your remaining space
app.get('/api/mymetric', (req,res) => {
    b = req.headers.authorization;
    hashes = hash(b);
    views.metrics(res,hashes,db);

});

app.listen(9000, () => console.log("server ready"));