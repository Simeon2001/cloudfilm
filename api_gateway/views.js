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


const viewimage = async (req,res, hashes, db) => {
    const enc_privkey = await db.findOne({ 
        where: { enc_private: hashes}});
    if (enc_privkey === null){
        return res.status(406).json({"status": false,"message": "invalid authentication token"});
    } else{
        const token = enc_privkey.token;
        return res.status(200).json({"status": true, "message": token});
    }
}


const postviewimage = async (req,res, hashes, db) => {
    const enc_privkey = await db.findOne({ 
        where: { enc_private: hashes}});
    if (enc_privkey === null){
        return res.status(406).json({"status": false,"message": "invalid authentication token"});
    } else{
        const images  = req.body.file;
        const token = enc_privkey.token;
        return res.status(200).json({"status": true, "message": token});
    }
}
module.exports = {
    savekey:savekey,
    viewimage:viewimage
}