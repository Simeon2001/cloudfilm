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

const post = async (auth,url,data) => {
    const config = {
        method: 'post',
        url: url,
        data: data,
        headers: {'Authorization': auth},
    }
    let resp = await axios(config);
    return resp
}

module.exports = {
    get: get,
    post: post
}
