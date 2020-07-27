const puppeteer = require('puppeteer');

(async () => {
    const url = 'http://trafi2.stat.fi/PXWeb/pxweb/fi/TraFi/TraFi__Katsastuksen_vikatilastot/010_kats_tau_101.px/';
    const browser = await puppeteer.launch();
    await downloadFile(browser, url, 'FileTypeCsvWithHeadingAndTabulator');
    await browser.close();
})();

async function downloadFile(browser, url, fileType) {
    const page = await browser.newPage();
    await page.goto(url, {waitUntil: 'networkidle2'});

    const selector = 'input[title="Valitse kaikki"]';
    await page.waitForSelector(selector);
    const selectAllButtons = await page.$$(selector);
    for (const button of selectAllButtons) {
        await button.click();
    }

    const dropdown = await page.$('.variableselector_outputformats_dropdown')
    await dropdown.select(fileType);

    const submit = await page.$('.variableselector_continue_button');

    await page._client.send('Page.setDownloadBehavior',
        { behavior: 'allow', downloadPath: '/tmp' });

    await Promise.all([
        submit.click(),
        page.waitFor(5000),
    ]);
}
