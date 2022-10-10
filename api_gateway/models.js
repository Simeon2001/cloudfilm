module.exports = (sequelize, DataTypes) => {
    const Keys = sequelize.define("keys", {
        enc_private : {
            type: DataTypes.STRING
        },
        enc_public : {
            type: DataTypes.STRING
        },
        token : {
            type: DataTypes.STRING
        }

    });
    return Keys;
}