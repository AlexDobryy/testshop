#######4#######
# from selenium import webdriver
# driver = webdriver.Chrome()
# driver.get("http://practice.automationtesting.in/")
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# driver.implicitly_wait(5)
# driver.maximize_window()
#
# my_account = driver.find_element(By.LINK_TEXT, "My Account")
# my_account.click()
# email = driver.find_element(By.ID, "username")
# email.send_keys("test@ya.ru")
# password = driver.find_element(By.ID,"password")
# password.send_keys("1qaz2WSX3edc!@!")
# LOGIN_btn = driver.find_element(By.NAME,"login")
# LOGIN_btn.click()
# shop_tab = driver.find_element(By.LINK_TEXT,"Shop")
# shop_tab.click()
# html_5_book = driver.find_element(By.CSS_SELECTOR, ".post-181 > a > h3")
# html_5_book.click()
# book_title = WebDriverWait(driver, 10).until(
# EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".product_title"), 'HTML5 Forms'))
#
# driver.quit()

#######5#######
# from selenium import webdriver
# driver = webdriver.Chrome()
# driver.get("http://practice.automationtesting.in/")
# from selenium.webdriver.common.by import By
# driver.implicitly_wait(5)
# driver.maximize_window()
# my_account = driver.find_element(By.LINK_TEXT, "My Account")
# my_account.click()
# email = driver.find_element(By.ID, "username")
# email.send_keys("test@ya.ru")
# password = driver.find_element(By.ID,"password")
# password.send_keys("1qaz2WSX3edc!@!")
# LOGIN_btn = driver.find_element(By.NAME,"login")
# LOGIN_btn.click()
# shop_tab = driver.find_element(By.LINK_TEXT,"Shop")
# shop_tab.click()
# html_cat = driver.find_element(By.LINK_TEXT,"HTML")
# html_cat.click()
# items = driver.find_elements(By.CSS_SELECTOR,"a > h3")
# if len(items) == 3:
#     print("3 товара")
# else:
#     print("Количество товаров: " + str(len(items)))
#
# driver.quit()

#######6#######
# from selenium import webdriver
# driver = webdriver.Chrome()
# driver.get("http://practice.automationtesting.in/")
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.select import Select
#
#
# driver.implicitly_wait(5)
# driver.maximize_window()
# my_account = driver.find_element(By.LINK_TEXT, "My Account")
# my_account.click()
# email = driver.find_element(By.ID, "username")
# email.send_keys("test@ya.ru")
# password = driver.find_element(By.ID,"password")
# password.send_keys("1qaz2WSX3edc!@!")
# LOGIN_btn = driver.find_element(By.NAME,"login")
# LOGIN_btn.click()
# shop_tab = driver.find_element(By.LINK_TEXT,"Shop")
# shop_tab.click()
# selector = driver.find_element(By.NAME,"orderby")
# selector_default = selector.get_attribute("value")
# if selector_default == "menu_order":
#     print("Выбрана сортировка по умолчанию")
# else:
#     print("Выбрана сортировка НЕ по умолчанию")
#
# select = Select(selector)
# select.select_by_value("price-desc")
# selector = driver.find_element(By.NAME,"orderby")
# selector_low = selector.get_attribute("value")
# if selector_low == "price-desc":
#     print("Выбрана сортировка по убыванию")
# else:
#     print("Выбрана сортировка НЕ по убыванию")
#
# driver.quit()

#######7#######
# from selenium import webdriver
# driver = webdriver.Chrome()
# driver.get("http://practice.automationtesting.in/")
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# driver.implicitly_wait(5)
# driver.maximize_window()
# my_account = driver.find_element(By.LINK_TEXT, "My Account")
# my_account.click()
# email = driver.find_element(By.ID, "username")
# email.send_keys("test@ya.ru")
# password = driver.find_element(By.ID,"password")
# password.send_keys("1qaz2WSX3edc!@!")
# LOGIN_btn = driver.find_element(By.NAME,"login")
# LOGIN_btn.click()
# shop_tab = driver.find_element(By.LINK_TEXT,"Shop")
# shop_tab.click()
#
# android_quick_book = driver.find_element(By.CSS_SELECTOR, ".post-169 h3")
# android_quick_book.click()
# book_old_price = driver.find_element(By.CSS_SELECTOR,".price > del > span")
# book_old_price_text = book_old_price.text
# book_new_price = driver.find_element(By.CSS_SELECTOR, ".price > ins > span")
# book_new_price_text = book_new_price.text
# assert book_old_price_text == "₹600.00"
# assert book_new_price_text == "₹450.00"
#
# book_cover = WebDriverWait(driver, 10).until(
# EC.element_to_be_clickable((By.CSS_SELECTOR, ".images > a")))
# book_cover.click()
# book_cover_close = WebDriverWait(driver, 10).until(
# EC.element_to_be_clickable((By.CSS_SELECTOR, ".pp_close")))
# book_cover_close.click()
#
# driver.quit()


#######8#######
# import time
# from selenium import webdriver
# driver = webdriver.Chrome()
# driver.get("http://practice.automationtesting.in/")
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# driver.implicitly_wait(5)
# driver.maximize_window()
# shop_tab = driver.find_element(By.LINK_TEXT,"Shop")
# shop_tab.click()
# Mastering_JavaScript_book = driver.find_element(By.CSS_SELECTOR,".post-165 > a h3")
# Mastering_JavaScript_book.click() #книги в задании не было в наличии
# add_basket=driver.find_element(By.CSS_SELECTOR,".single_add_to_cart_button")
# add_basket.click()
# time.sleep(5)
# basket_item_value = driver.find_element(By.CSS_SELECTOR,".wpmenucart-contents .cartcontents")
# basket_item_value_text = basket_item_value.text
# assert basket_item_value_text == "1 Item"
# basket_price_value = driver.find_element(By.CSS_SELECTOR,".wpmenucart-contents .amount")
# basket_price_value_text = basket_price_value.text
# assert basket_price_value_text == "₹350.00"
# basket_btn = driver.find_element(By.CLASS_NAME,"wpmenucart-contents")
# basket_btn.click()
# subtotal_price = WebDriverWait(driver, 10).until(
# EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".cart-subtotal .woocommerce-Price-amount"), "₹350.00"))
# total_price = WebDriverWait(driver, 10).until(
# EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".order-total .woocommerce-Price-amount"), "₹357.00"))
#
# driver.quit()

#######9#######
# import time
# from selenium import webdriver
# driver = webdriver.Chrome()
# driver.get("http://practice.automationtesting.in/")
# from selenium.webdriver.common.by import By
#
# driver.implicitly_wait(5)
# driver.maximize_window()
# shop_tab = driver.find_element(By.LINK_TEXT,"Shop")
# shop_tab.click()
# driver.execute_script("window.scrollBy(0, 300);")
# Mastering_JavaScript_book = driver.find_element(By.CSS_SELECTOR,".post-165 > a h3")
# Mastering_JavaScript_book.click() #доступна только 1 книга
# add_basket=driver.find_element(By.CSS_SELECTOR,".single_add_to_cart_button")
# add_basket.click()
# time.sleep(3)
# basket_btn = driver.find_element(By.CLASS_NAME,"wpmenucart-contents")
# basket_btn.click()
# time.sleep(2)
# remove_btn = driver.find_element(By.CLASS_NAME,"remove")
# remove_btn.click()
# undo_btn = driver.find_element(By.LINK_TEXT,"Undo?")
# undo_btn.click()
# quantity = driver.find_element(By.CSS_SELECTOR,"tbody > tr:nth-child(1) .product-quantity input")
# quantity.clear()
# quantity.send_keys("3")
# update = driver.find_element(By.NAME,"update_cart")
# update.click()
# quantity = driver.find_element(By.CSS_SELECTOR,"tbody > tr:nth-child(1) .product-quantity input")
# quantity_value = quantity.get_attribute("value")
# assert quantity_value == '3'
# time.sleep(5)
# apply_coupon = driver.find_element(By.NAME, "apply_coupon")
# apply_coupon.click()
# error = driver.find_element(By.CSS_SELECTOR,".woocommerce-error")
# error_text = error.text
# assert error_text == 'Please enter a coupon code.'
#
# driver.quit()

####10####
import time
from selenium import webdriver
driver = webdriver.Chrome()
driver.get("http://practice.automationtesting.in/")
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver.implicitly_wait(10)
driver.maximize_window()


shop_tab = driver.find_element(By.LINK_TEXT,"Shop")
shop_tab.click()
driver.execute_script("window.scrollBy(0, 300);")
Mastering_JavaScript_book = driver.find_element(By.CSS_SELECTOR,".post-165 .add_to_cart_button")
Mastering_JavaScript_book.click()

basket_btn = driver.find_element(By.CLASS_NAME,"wpmenucart-contents")
basket_btn.click()
checkout_btn = WebDriverWait(driver, 10).until(
EC.element_to_be_clickable((By.CLASS_NAME, "checkout-button")))
checkout_btn.click()

first_name = WebDriverWait(driver, 10).until(
EC.element_to_be_clickable((By.ID, "billing_first_name")))
first_name.send_keys("Alex")
last_name = WebDriverWait(driver, 10).until(
EC.element_to_be_clickable((By.ID, "billing_last_name")))
last_name.send_keys("testet")
email = driver.find_element(By.ID,"billing_email")
email.send_keys("test@ya.ru")
phone = driver.find_element(By.ID,"billing_phone")
phone.send_keys("89999999999")
country = driver.find_element(By.ID,"s2id_billing_country")
country.click()
country_search = driver.find_element(By.ID, "s2id_autogen1_search")
country_search.send_keys("Russia")
country_enter = driver.find_element(By.CLASS_NAME, "select2-match")
country_enter.click()
address = driver.find_element(By.ID,"billing_address_1")
address.send_keys("testetetet")
city = driver.find_element(By.ID,"billing_city")
city.send_keys("Moscow")
state = driver.find_element(By.ID, "billing_state")
state.send_keys("state test")
zipcode = driver.find_element(By.ID, "billing_postcode")
zipcode.send_keys("14242433")
driver.execute_script("window.scrollBy(0, 600);")
time.sleep(5)

payment_check = driver.find_element(By.ID,"payment_method_cheque")
payment_check.click()
place_order_btn = driver.find_element(By.ID,"place_order")
place_order_btn.click()

message = WebDriverWait(driver, 10).until(
EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".woocommerce-thankyou-order-received"),
"Thank you. Your order has been received."))

payment_method_message = WebDriverWait(driver, 10).until(
EC.text_to_be_present_in_element((By.CSS_SELECTOR, "tfoot > tr:nth-child(3) > td"), "Check Payments"))
driver.quit()