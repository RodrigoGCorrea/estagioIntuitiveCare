module.exports = () => {
    const { PrepareData } = require('../data/data');
    const data = PrepareData();
    const controller = {};

    controller.listData = (req, res) => {
        const filters = req.query;
        filteredUsers = data.filter(user => {
            let isValid = true;
            for(key in filters) {
                isValid = isValid && user[key].toLowerCase().includes(filters[key].toLowerCase());
            }
            return isValid;
        })
        res.status(200).json(filteredUsers);
    };

    return controller;
}