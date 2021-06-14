module.exports = app => {
    const controller = require('../controllers/dataController')();

    app.route('/').get(controller.listData);
}