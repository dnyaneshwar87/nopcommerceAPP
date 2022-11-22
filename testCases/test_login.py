from pageObjects.LoginPage import LoginPage
from selenium import webdriver
from utilities.readProperties import ReadConfig
from utilities.Customlogger import LogGen

class Test_001_Login:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    logger = LogGen.logGen()

    def test_homePageTitle(self, setup):
        self.logger.info("****************Test_001_login****************")
        self.logger.info("****************Varify Home Page Title****************")

        self.driver = setup
        self.driver.get(self.baseURL)
        print(self.driver.title)
        act_title = self.driver.title
        if act_title == "Your store. Login":
            assert True
            self.logger.info("**************** Home Page Title passed****************")
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshot\\"+"test_homePageTitle.png")
            self.logger.error("**************** Home Page Title Failed****************")
            self.driver.close()
            assert False


    def test_login(self, setup):
        self.driver = setup
        self.logger.info("****************verify login page****************")
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.SetUsername(self.username)
        self.lp.SetPassword(self.password)
        self.lp.ClickLogin()
        act_title = self.driver.title
        print(self.driver.title)
        if act_title == "Dashboard / nopCommerce administration":
            assert True
            self.logger.info("**************** login page Passed****************")
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshot\\"+"test_homePageTitle.png")
            self.logger.error("**************** login page Failed****************")
            self.driver.close()
            assert False


