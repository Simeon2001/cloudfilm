const axo = require('./axo');

// function for sending buffer images and get details
const desc_image = async (req,res) => {
    if (req.headers.authorization == process.env.AUTH_TOKEN){
        const desp = [];
        if (!req.file){
            return res.status(400).json({"status": false, "message": "nothing was uploaded"});
        }
        const files  = req.file.mimetype.split('/')[0];
        if (files != "image" | files === null ) {
            return res.status(400).json({"status": false, "message": "upload an image"}); 
        } else{
            img_buf = req.file.buffer
            img_name = req.file.originalname
            try{
                img_resp = await axo.img_post(img_buf)
                infos = img_resp.data.tags
                color = img_resp.data.color.dominantColors
                caption = img_resp.data.description.captions[0].text
                desp.push(caption)
            desp.push(color.toString())
                for (value in infos){
                    tags = infos[value].name
                    desp.push(tags)
                }
                console.log(desp.toString())
                
                
                return res.status(200).json({"status": true,"result":desp.toString()});  
            } catch (err) {
                if (err.response){
                    return res.status(400).json({"status":false, "message":"image not uploaded"});
                } else if (err.request) {
                    return res.status(500).json({"status": false,"message": "internal server error"});
                } else {
                    console.log("error");
                }
            }
            
        }
    } else {
        return res.status(406).json({"status": false,"message": "not authenticated"});
    }
}

module.exports = {
    desc_image: desc_image
    
}
