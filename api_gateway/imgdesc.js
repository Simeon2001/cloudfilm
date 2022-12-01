const axo = require('./axo');

// function for sending buffer images and get details
const desc_image = async (req,res) => {
    const files  = req.file.mimetype.split('/')[0];
    if (files != "image" | files === null ) {
        return res.status(400).json({"status": false, "message": "upload an image"}); 
    } else{
        img_buf = req.file.buffer
        img_name = req.file.originalname
        img_resp = await axo.img_post(img_buf)
        infos = img_resp.data.tags
       
        console.log(infos)
        
        return res.status(200).json({"status": true,});
    }

}

module.exports = {
    desc_image: desc_image
    
}
