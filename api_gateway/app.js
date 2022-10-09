const express = require('express');
const crypto = require('crypto');
const app = express();
app.use(express.json())

hash = (key) => crypto.createHash('sha256').update(String(key)).digest('hex');

app.get('/hello', (req,res) => {
    b = req.headers.authorization,
    res.send(hash(b)),
    console.log(b   , hash(b) )
});

app.post('/api/savekeys', (req,res) => {
    if (req.headers.authorization == "Bearer Helloworld"){

        const enc_private_key  = req.body.pri_key;
        const enc_public_key   = req.body.pub_key;
        if (enc_private_key.length == 0 | enc_public_key.length == 0){
            return res.status(401).json({"status": false,})
        }
        console.log(enc_private_key, enc_public_key)
        return res.status(200).json({"status": true,})
    }
    else {
        return res.status(406).json({"status": false,"message": "not authenticated"}) 
    }
});

app.listen(9000, () => console.log("server ready"));