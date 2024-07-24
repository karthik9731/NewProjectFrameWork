from selenium import webdriver
from time import sleep

# driver = webdriver.Chrome()
class Register:
    main_register_button_xpath = "//a[text()='Register']"
    gender_radio_button_xpath = '//div[@class="gender"]/.//input[@id="gender-male"]'
    first_name_textfield_xpath = '//input[@id="FirstName"]'
    last_name_textfield_xpath = '//input[@id="LastName"]'
    email_textfield_xpath = '//input[@id="Email"]'
    password_textfield_xpath = '//input[@id="Password"]'
    confirm_password_textfield_xpath = '//input[@id="ConfirmPassword"]'
    register_button_xpath = '//input[@id="register-button"]'

    def __init__(self,driver):
        self.driver = driver

    def Registers(self):
        self.driver.find_element("xpath",self.main_register_button_xpath).click()

    def Select_Gender(self):
        self.driver.find_element("xpath",self.gender_radio_button_xpath).click()

    def First_name(self,firstname):
        # self.driver.find_element
        self.driver.find_element("xpath",self.first_name_textfield_xpath).send_keys(firstname)

    def Last_name(self,lastname):
        self.driver.find_element("xpath",self.last_name_textfield_xpath).send_keys(lastname)

    def Email(self,email):
        self.driver.find_element("xpath",self.email_textfield_xpath).send_keys(email)

    def Password(self,password):
        self.driver.find_element("xpath",self.password_textfield_xpath).send_keys(password)

    def Confirm_Password(self,conf_pas):
        self.driver.find_element("xpath",self.confirm_password_textfield_xpath).send_keys(conf_pas)

    def Click_register(self):
        self.driver.find_element('xpath',self.register_button_xpath).click()
