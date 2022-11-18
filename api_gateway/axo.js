const axios = require("axios")

const get = async (auth,url) => {
    const config = {
        method: 'get',
        url: url,
        headers: {'Authorization': auth},
    }
    let resp = await axios(config);
    return resp 
}

const post = async (auth,url,data,name) => {
    const config = {headers: {'Authorization': auth},};
    up_data = {"imgbase":data,"imgname":name}
    let resp = await axios.post(url,up_data,config);
    return resp
}

module.exports = {
    get: get,
    post: post
}
