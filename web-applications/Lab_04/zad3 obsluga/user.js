const { DataTypes } = require('sequelize');
const bcrypt = require('bcryptjs');

module.exports = (sequelize) => {
    const User = sequelize.define('User', {
        //user id jest automatycznie generowane i inkrementowane
        email: {
            type: DataTypes.STRING,
            unique: true,
            allowNull: false,
        },
        password: {
            type: DataTypes.STRING,
            allowNull: false,
        },
    });


    User.beforeCreate(async (user) => {
        user.password = await bcrypt.hash(user.password, 10);
    });


    User.prototype.comparePassword = async function (password) {
        return await bcrypt.compare(password, this.password);
    };

    return User;
};