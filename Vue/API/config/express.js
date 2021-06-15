const express    = require('express');
const config     = require('config');
const cors = require('cors');

module.exports = () => {
  const app = express();

  // SETANDO VARIÁVEIS DA APLICAÇÃO
  app.set('port', process.env.PORT || config.get('server.port'));

  app.use(cors());

  // Pegar dados
  require('../api/routes/dataFetch')(app);

  return app;
};