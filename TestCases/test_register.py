from selenium import webdriver
import pytest
from PageObjects.RegisterPage import Register
from time import sleep
from utilities.readProperties import ReadConfig

class Test_Register:
    baseurl = ReadConfig.Get_Application()
    firstname = ReadConfig.firstname()
    lastname = ReadConfig.lastname()
    email = ReadConfig.email_id()
    password = ReadConfig.Password()
    confirm = ReadConfig.confirm_pass()

    def test_homepageTitle(self,setup):
        self.driver = setup
        self.driver.get(self.baseurl)
        sleep(5)
        actual_title = self.driver.title
        expected_title = "Demo Web Shop"
        if actual_title == expected_title:
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(r"C:\Users\ckart\PycharmProjects\pythonProject1\NewProjectFrameWork\Screenshots\home_page.png")
            self.driver.close()
            assert False

    def test_check_that_user_is_register_with_valid_credentials(self,setup):
        self.driver = setup
        self.driver.get(self.baseurl)
        self.rg = Register(self.driver)
        self.rg.Registers()
        self.rg.Select_Gender()
        sleep(2)
        self.rg.First_name(self.firstname)
        self.rg.Last_name(self.lastname)
        self.rg.Email(self.email)
        self.rg.Password(self.password)
        self.rg.Confirm_Password(self.confirm)
        self.rg.Click_register()

