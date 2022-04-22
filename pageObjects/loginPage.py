from selenium.webdriver.common.by import By


class LoginPage:
    textbox_username_XPATH="//div[@class='IiD88i _351hSN'][1]"
    textbox_password_XPATH="//div[@class='IiD88i _351hSN'][2]"
    click_btn_XPATH="//button[@class='_2KpZ6l _2HKlqd _3AWRsL']s"

    def __init__(self,driver):
        self.driver=driver

    def setUserName(self,username):
        self.driver.find_element(By.XPATH,"textbox_username_XPATH").clear()
        self.driver.find_element(By.XPATH,"textbox_username_XPATH").send_keys(username)

    def setpassword(self,password):
        self.driver.find_element(By.XPATH,"textbox_password_XPATH").clear()
        self.driver.find_element(By.XPATH,"textbox_password_XPATH").send_keys(password)

    def setclick(self):
        self.driver.find_element(By.XPATH, "click_btn_XPATH").click()
