const { openBrowser, scrape, download } = require("./scraper");

async function main() {
    const ppt = await openBrowser();
    const link = await scrape(ppt.page);
    await download(link);
    await ppt.browser.close();
}

main();