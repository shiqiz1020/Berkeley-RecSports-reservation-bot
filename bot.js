const puppeteer = require('puppeteer');

const gym_url = "https://shop.rs.berkeley.edu/Account/Login?ReturnUrl=%2Fbooking%2F8e4a4640-3b33-4848-808c-4d8b03875e77#";

async function loadPage() {
    // const browser = await puppeteer.launch({headless: false, executablePath: "/Applications/Google\ Chrome\ Canary.app/Contents/MacOS/Google\ Chrome\ Canary"});
    const browser = await puppeteer.launch({headless: false, executablePath: "/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome"});
    const page = await browser.newPage();
    return page;
}

async function logIn(page) {
    await page.goto(gym_url);
    await page.waitForSelector("button[class='loginOption btn btn-lg btn-block btn-social btn-soundcloud']");
    await page.click("button[class='loginOption btn btn-lg btn-block btn-social btn-soundcloud']", elem => elem.click());
    CalNetAuthentication(page);
}

async function CalNetAuthentication(page) {
    var auth_url = "https://auth.berkeley.edu/cas/login?service=https%3A%2F%2Fshib.berkeley.edu%2Fidp%2FAuthn%2FExternal%3Fconversation%3De1s1%26entityId%3Dhttps%3A%2F%2Fshop.rs.berkeley.edu%2Fshibboleth";
    page.goto(auth_url);
    await page.waitForNavigation();
    await page.waitForTimeout(1000);
    await page.type("input[id='username'", 'ENTER YOUR USERNAME');
    await page.waitForTimeout(500);
    await page.type("input[id='password'", 'ENTER YOUR PASSWORD');
    await page.waitForTimeout(1000);
    await page.evaluate(() => document.getElementsByClassName('button')[0].click())
}

async function reserve() {
    var page = await loadPage();
    page = await logIn(page);
}

reserve();
