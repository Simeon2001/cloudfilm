const axo = require('./axo');

const desc_image = async (req,res) => {
    const files  = req.file.mimetype.split('/')[0];
    if (files != "image" | files === null ) {
        return res.status(400).json({"status": false, "message": "upload an image"}); 
    } else{
        img_buf = req.file.buffer
        img_name = req.file.originalname
        img_base = img_buf.toString('base64')
        await axo.img_post(img_base)
    }

}

module.exports = {
    desc_image: desc_image
    
}
