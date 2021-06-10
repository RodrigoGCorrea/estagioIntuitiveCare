const puppeteer = require("puppeteer-extra");
const axios = require('axios');
const path = require('path');
const fs = require('fs');


async function openBrowser() {
  // Inicializando o browser
  const browser = await puppeteer.launch({
    headless: true,
  });
  const page = await browser.newPage();

  return {
    page: page,
    browser: browser
  };
}

async function scrape(page) {
  try {
    // Abre a pagina 
    await page.goto('http://www.ans.gov.br/prestadores/tiss-troca-de-informacao-de-saude-suplementar', {
      waitUntil: 'networkidle2'
    });
    // Procura e clica no link do padrão TISS por meio do XPath
    const TISSRecente = await page.$x('/html/body/div[9]/div/div[2]/div[2]/div[2]/a');
    await TISSRecente[0].click();
    // Espera a página terminar de carregar, procura o link de download e o retorna
    await page.waitForXPath('/html/body/div[9]/div/div[2]/div[2]/div[2]/table/tbody/tr[1]/td[3]');
    const link = await page.evaluate(el => el.href, (await page.$x('/html/body/div[9]/div/div[2]/div[2]/div[2]/table/tbody/tr[1]/td[3]/a'))[0])
    // Feedback para saber se a operação deu certo
    console.log("link de download foi coletado");
    return link;

  } catch (e) {
    console.log(e);
  }
}

async function download(link) {
  // seta o path para terminar o download
  const downloadPath = path.resolve("../Python", 'Componente Organizacional.pdf');
  // faz o download do arquivo
  const response = await axios({
    method: 'GET',
    url: link,
    responseType: 'stream'
  });
  response.data.pipe(fs.createWriteStream(downloadPath));
  // Feedback para saber se a operação deu certo, informando o path em que o arquivo foi armazenado
  console.log("download finalizado em " + downloadPath);

}
  
function delay(time) {
  return new Promise(function (resolve) {
    setTimeout(resolve, time*1000);
  });
}

module.exports = {
  openBrowser,
  scrape,
  download
}
