const axo = require('./axo');

const savekey = async (req, res, db) => {
    if (req.headers.authorization == process.env.AUTH_TOKEN){

        const enc_private_key  = req.body.pri_key;
        const enc_public_key   = req.body.pub_key;
        const token   = req.body.token;
        if (enc_private_key.length == 0 | enc_public_key.length == 0){
            return res.status(401).json({"status": false,});
        }
        const key_data = {enc_private: enc_private_key, enc_public: enc_public_key, token: token};
        
        data = await db.create(key_data);
        return res.status(200).json({"status": true,});
        
    }
    else {
        return res.status(406).json({"status": false,"message": "not authenticated"});
    }
}


const viewimage = async (req,res, hashes, db, idd) => {
    const enc_privkey = await db.findOne({ 
        where: { enc_private: hashes}});

    if (enc_privkey === null){
        return res.status(406).json({"status": false,"message": "invalid authentication token"});
    
    } else{
        const auth = "Token" + " " + enc_privkey.token;
        const url = process.env.IMAGE_STORE + idd;

        try {
            const response = await axo.get(auth,url);

        if (response.status == 200) {
            return res.status(200).json(response.data);
        }

        } catch (err) {
            if (err.response){
                return res.status(404).json({"status":false,"message":"image album not found"});
            } else if (err.request) {
                return res.status(500).json({"status": false,"message": "internal server error"});
            } else {
                console.log("error");
            }
        }
        
        
    }
}


const postviewimage = async (req,res, hashes, db, id) => {
    const enc_privkey = await db.findOne({ 
        where: { enc_private: hashes}});
    if (enc_privkey === null){
        return res.status(406).json({"status": false,"message": "invalid authentication token"});
    }
    
    else{
        const files  = req.file.mimetype.split('/')[0];
        console.log(files);
        const token = enc_privkey.token;
        return res.status(200).json({"status": true, "message": token});
    }
}


const putkey = async(req, res, db) => {
    if (req.headers.authorization == process.env.AUTH_TOKEN){
        const enc_pri_key  = req.body.oldpriv_key;
        const enc_new_pri_key  = req.body.enc_priv_key;
        const enc_new_pub_key  = req.body.enc_pub_key;
        const enc_newkeys = await db.findOne({ 
            where: { enc_private: enc_pri_key}});
        enc_newkeys.enc_private = enc_new_pri_key;
        enc_newkeys.enc_public = enc_new_pub_key;
        await enc_newkeys.save();
        return res.status(200).json({"status": true, "message": "saved"});
    }else{
        return res.status(406).json({"status": false,"message": "not authenticated"});
    }
}
module.exports = {
    savekey:savekey,
    viewimage:viewimage,
    postviewimage:postviewimage,
    putkey:putkey
}