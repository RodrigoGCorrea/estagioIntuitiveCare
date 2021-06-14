const fs = require('fs')
const iconvlite = require('iconv-lite');
const { headers } = require('./mapping');


function ParseData(csvPath) {
  const table = []
  // ler arquivo na memória
  const content = fs.readFileSync(csvPath);
  const raw = iconvlite.decode(content, 'latin1');
  // dividir pela quebra de linha
  const rawtable = raw.split('\n');
  rawtable.forEach((rawrow) => {
    // dividir pelo ;
    const row = rawrow.split(';');
    let element = {}
    headers.forEach((key, i) => element[key] = row[i]);
    table.push(element);
  })
  return table;
}

const res = ParseData('Relatorio_cadop.csv');
fs.writeFileSync('Relatorio_cadop.json', JSON.stringify(res), 'latin1');