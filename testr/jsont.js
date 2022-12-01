const axios = require("axios")
url = "http://127.0.0.1:8000/api/banks"
const response = async () => {
    return await axios.get(url);
}  
try {
    king = response()

    console.log(king);
}catch (err){
    console.log("error");
}

