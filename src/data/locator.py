from selenium.webdriver.common.by import By

class LoginPageLocators:
  SIGN_IN_BUTTON = (By.LINK_TEXT, "Sign in")
  LOGIN_BUTTON   = (By.XPATH, '//button[contains(text(), "Login")]')
  ID_INPUT = (By.ID, 'login-email')
  PW_INPUT = (By.ID, 'login-password')

class OrderPageLocators:
  ORDER_ITEMS   = (By.CSS_SELECTOR, 'div.order-item')
  SHIPPING_TIME = (By.CSS_SELECTOR, 'span.shipping-time')
  ORDER_STATUS  = (By.CSS_SELECTOR, 'div.order-status')


class MenuPageLocators:
  PRODUCT_ITEMS = (By.CLASS_NAME, "product-item")
  PRODUCT_TITLE = (By.CLASS_NAME, "product-title")
  ADD_BUTTON    = (By.CLASS_NAME, "svg-icon")

class CheckoutPageLocators:
  PLACE_ORDER_BUTTON = (By.XPATH, '//*[@id="app"]/app-checkout/div/div/div[2]/nz-spin/div/app-checkout-fee/div/div/button')
  CONFIRM_BUTTON     = (By.XPATH, '/html/body/app-root/st-modal-box/div/div/div[2]/div[1]/button[2]')