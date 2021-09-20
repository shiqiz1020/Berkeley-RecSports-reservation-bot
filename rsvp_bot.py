import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class RSVP:
    def __init__(self):
        # options = webdriver.ChromeOptions()
        # options.add_argument("user-data-dir=/Users/shiqizhang/Library/Application Support/Google/Chrome")
        self.PATH = "/usr/local/bin/chromedriver"
        self.driver = webdriver.Chrome(self.PATH)
        # self.driver = webdriver.Chrome(executable_path='/Applications/Google Chrome.app/Contents/MacOS/Google Chrome')
        # self.driver = webdriver.Chrome(chrome_options=options)
        self.driver.get("https://shop.rs.berkeley.edu/Account/Login?ReturnUrl=%2Fbooking%2F8e4a4640-3b33-4848-808c-4d8b03875e77#")
        button = self.driver.find_element_by_xpath('//*[@id="divLoginOptions"]/div[2]/div[2]/div/button')
        button.click()
        self.CalNetLogIn('shiqiz', 'Key#20001020')

    def CalNetLogIn(self, CalNet_ID, Passphrase):
        self.driver.get('https://auth.berkeley.edu/cas/login?service=https%3A%2F%2Fshib.berkeley.edu%2Fidp%2FAuthn%2FExternal%3Fconversation%3De1s1%26entityId%3Dhttps%3A%2F%2Fshop.rs.berkeley.edu%2Fshibboleth')
        time.sleep(1)
        CalNet_ID_input = self.driver.find_element_by_xpath('//*[@id="username"]')
        CalNet_ID_input.send_keys(CalNet_ID)
        Passphrase_input = self.driver.find_element_by_xpath('//*[@id="password"]')
        Passphrase_input.send_keys(Passphrase)
        button = self.driver.find_element_by_xpath('//*[@id="submit"]')
        button.click()
        time.sleep(1)
        # if self.driver.current_url == 'https://shop.rs.berkeley.edu/booking/8e4a4640-3b33-4848-808c-4d8b03875e77':
            # self.reserve()
        # button2 = self.driver.find_element_by_xpath('/html/body/div/div/div[1]/div/form/div[1]/fieldset/div[1]/button')
        # button2.click()

    def reserve(self):
        self.driver.get('https://shop.rs.berkeley.edu/booking/8e4a4640-3b33-4848-808c-4d8b03875e77')
        time.sleep(1)
        date_button = self.driver.find_element_by_xpath('//*[@id="divBookingDateSelector"]/div[2]/div[2]/button[4]')
        date_button.click()
        slot_button = self.driver.find_element_by_xpath('//*[@id="divBookingSlots"]/div[2]/div[7]/div/button')
        slot_button.click()
        

if __name__ == "__main__":
    RSVP_bot = RSVP()