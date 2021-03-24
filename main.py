from selenium import webdriver
# from selenium.webdriver.common.keys import Keys

# browser = webdriver.Chrome()
browser = webdriver.Chrome('chromedriver')
browser.get("https://github.com")

sign_link = browser.find_element_by_link_text("Sign in")
sign_link.click()
