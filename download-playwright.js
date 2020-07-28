const fs = require('fs');
const playwright = require('playwright');

(async () => {
    const url = 'http://trafi2.stat.fi/PXWeb/pxweb/fi/TraFi/TraFi__Katsastuksen_vikatilastot/010_kats_tau_101.px/';
    //const params = { headless: false, slowMo: 50 };
    const params = { };

    const browser = await playwright['chromium'].launch(params);
    const context = await browser.newContext({ acceptDownloads: true });
    const page = await context.newPage();
    await page.goto(url);

    for (const button of await page.$$('input[title="Valitse kaikki"]')) {
        await button.click();
    }

    await page.selectOption('.variableselector_outputformats_dropdown',
                            'FileTypeCsvWithHeadingAndTabulator');

    const [ download ] = await Promise.all([
        page.waitForEvent('download'),
        page.click('.variableselector_continue_button')
    ]);
    const path = await download.path();

    fs.copyFile(path, '/tmp/foo.csv', err => {});

    await browser.close();
})();

