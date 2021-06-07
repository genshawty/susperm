const puppeteer = require('puppeteer');
const path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe'
async function open() {
    const browser = await puppeteer.launch({executablePath:path, headless: false});
    const [page] = await browser.pages();
    await page.goto('https://www.supremenewyork.com/shop/tops-sweaters/jmqsjoxe5/x2y3lk890');
    page.evaluate(() => document.querySelector('.button').click())
}
open();