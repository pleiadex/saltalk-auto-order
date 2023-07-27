import time
from datetime import datetime, timedelta
from utils.load_config import load_config
from selenium.webdriver.support import expected_conditions as EC

from pages.base import BasePage
from data.locator import MenuPageLocators

class MenuPage(BasePage):

  def __init__(self, driver, wait, n_days_later):
    super().__init__(driver, wait)
    self.n_days_later = n_days_later
    self.locator = MenuPageLocators
  
  def _get_n_days_later(self):
    return (datetime.today() + timedelta(days=self.n_days_later)).strftime("%Y-%m-%d")

  def _get_saltalk_url(self):
    return f'https://www.saltalk.com/?date={self._get_n_days_later()}&shippingTime=Lunch'
  
  def _get_favorite_orders(self):
    return load_config()["orders"]

  def _scroll_down_page(self, speed=1):
    current_scroll_position, new_height= 0, 1
    while current_scroll_position <= new_height:
        current_scroll_position += speed
        self.driver.execute_script("window.scrollTo(0, {});".format(current_scroll_position))
        new_height = self.driver.execute_script("return document.body.scrollHeight")

  def open_menu_page(self):
    self.saltalk_url = self._get_saltalk_url()
    self.driver.get(self.saltalk_url)

  def add_favorite_orders_to_cart(self):
    favorite_orders = self._get_favorite_orders()

    self.driver.implicitly_wait(10) # seconds
    self.wait.until(lambda driver: driver.execute_script('return document.readyState') == 'complete') # this doesn't wait for the page to be fully loaded
    time.sleep(60) # have padding time for the page to be fully loaded
    # self._scroll_down_page(10)
    product_items = self.wait.until(EC.presence_of_all_elements_located(self.locator.PRODUCT_ITEMS))
    
    order_count = 0
    for product_item in product_items:
      product_title = product_item.find_element(*self.locator.PRODUCT_TITLE).text
                                                                                            
      for favorite_order in favorite_orders[order_count:]:
        if favorite_order["title"] == product_title:
          product_item.find_element(*self.locator.PRODUCT_IMAGE).click()

          modal = self.wait.until(EC.element_to_be_clickable(self.locator.PRODUCT_DETAIL_MODAL))

          # TODO: (Youn) iframe is blocking the click event, need to switch to iframe

          add_button = modal.find_element(*self.locator.ADD_BUTTON)
          add_button.click()

          # TODO: (Sisi) select options

          order_count += 1

      if order_count == len(favorite_orders):
        return
    
    print('The menu are not found in the menu page.')
