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

module.exports = {
    get: get
}