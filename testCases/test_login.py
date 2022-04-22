import pytest
from selenium import webdriver
from webdrivermanager.chrome import  ChromeDriverManager
from pageObjects.loginPage import LoginPage

class Test_001_Login:
    baseurl="https://www.flipkart.com/"
    username="chilakanaveenoo9@gmail.com"
    password="8801769206"

    def test_homePageTitle(self):
        self.driver=webdriver.Chrome(ChromeDriverManager.install())
        self.driver.get(self.baseurl)
        act_title=self.driver.title
        self.driver.close()
        if act_title=="Online Shopping Site for Mobiles, Electronics, Furniture, Grocery, Lifestyle, Books & More. Best Offers!":
            assert True
        else:
            assert False
    def test_Login(self):
        self.driver=webdriver.Chrome(ChromeDriverManager.install())
        self.driver.get(self.baseurl)
        self.lp=LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setpassword(self.password)
        self.lp.setclick()
        title=self.driver.title
        # if title=="":
        #     assert True
        # else:
        #     assert False
