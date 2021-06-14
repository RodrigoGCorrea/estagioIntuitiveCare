const fs = require('fs');
const iconvlite = require('iconv-lite');

function PrepareData() {
    const file = fs.readFileSync('./api/data/Relatorio_cadop.json');
    const rawdata = iconvlite.decode(file, 'latin1');
    const data = JSON.parse(rawdata);
    return data;
}

module.exports = {
    PrepareData
}