from selenium.webdriver.support import expected_conditions as EC

from pages.base import BasePage
from data.locator import CheckoutPageLocators

class CheckoutPage(BasePage):
  saltalk_url = 'https://www.saltalk.com/checkout'
  def __init__(self, driver, wait):
    super().__init__(driver, wait)
    self.locator = CheckoutPageLocators

  def open_checkout_page(self):
    self.driver.get(self.saltalk_url)

  def click_place_order_button(self):
    # wait for element to be clickable
    self.wait.until(EC.element_to_be_clickable(self.locator.PLACE_ORDER_BUTTON))

    # click place order button
    order_button = self.driver.find_element(*self.locator.PLACE_ORDER_BUTTON)
    order_button.click()

  def click_confirm_button(self):
    # wait for element to be clickable
    self.wait.until(EC.element_to_be_clickable(self.locator.CONFIRM_BUTTON))

    # click confirm button
    confirm_button = self.driver.find_element(*self.locator.CONFIRM_BUTTON)
    confirm_button.click()