const axios = require("axios")

// get function to communicate with internal microservice api
const get = async (auth,url) => {
    const config = {
        method: 'get',
        url: url,
        headers: {'Authorization': auth},
    }
    let resp = await axios(config);
    return resp 
}


//  post function to communicate with internal microservice api
const post = async (auth,url,data,name) => {
    const config = {headers: {'Authorization': auth},};
    up_data = {"imgbase":data,"imgname":name}
    let resp = await axios.post(url,up_data,config);
    return resp
}


// post function that communicate with external api
const img_post = async (data) => {
    const key = process.env.AZURE_KEY
    const azure_url = process.env.AZURE_URL 
    const config = {headers:{"Content-Type":"application/octet-stream", 
                            "Ocp-Apim-Subscription-Key": key}}
    
    const img_data = data
    let resp = await axios.post(azure_url,img_data,config)
    return resp
    
}

module.exports = {
    get: get,
    post: post,
    img_post: img_post
}
