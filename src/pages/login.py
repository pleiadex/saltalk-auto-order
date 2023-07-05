import os
from selenium.webdriver.support import expected_conditions as EC

from pages.base import BasePage
from data.locator import LoginPageLocators

class LoginPage(BasePage):
  saltalk_url = 'https://www.saltalk.com/welcome'
  def __init__(self, driver, wait):
    super().__init__(driver, wait)
    self.id = os.getenv("SALTALK_ID")
    self.pw = os.getenv("SALTALK_PASSWORD")
    self.locator = LoginPageLocators

  def open_login_page(self):
    # open saltalk home page
    self.driver.get(self.saltalk_url)

    # wait for element to be clickable
    sign_in_button = self.driver.find_element(*self.locator.SIGN_IN_BUTTON)
    
    # click sign in button
    sign_in_button.click()

  def input_id_pw(self):
    # wait for element to be clickable
    self.wait.until(EC.element_to_be_clickable(self.locator.ID_INPUT))
    self.wait.until(EC.element_to_be_clickable(self.locator.PW_INPUT))

    # input id and pw
    id_input = self.driver.find_element(*self.locator.ID_INPUT)
    id_input.send_keys(self.id)
    pw_input = self.driver.find_element(*self.locator.PW_INPUT)
    pw_input.send_keys(self.pw)

  def click_login_button(self):
    # wait for element to be clickable
    self.wait.until(EC.element_to_be_clickable(self.locator.LOGIN_BUTTON))
    
    # click login button
    login_button = self.driver.find_element(*self.locator.LOGIN_BUTTON)
    login_button.click()
