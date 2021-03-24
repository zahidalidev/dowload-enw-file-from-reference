from selenium import webdriver
# from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome('chromedriver')
browser.get("https://scholar.google.com/")

searchFeild = browser.find_element_by_id("gs_hdr_tsi")
searchFeild.send_keys("Melville, N., Kraemer, K., & Gurbaxani, V. (2004). Information technology and organizational performance: An integrative model of IT business value. MIS quarterly, 28(2), 283-322.")
searchFeild.submit()

menueBar = browser.find_element_by_id("gs_hdr_mnu")
menueBar.click()

browser.implicitly_wait(1)

settingButton = browser.find_element_by_partial_link_text("Settings")
settingButton.click()

l = browser.find_element_by_xpath("//input[@value='yes']")
l.click()

inut = browser.find_element_by_id("gs_settings_import-bl")
inut.click()

inut2 = browser.find_element_by_xpath("//a[contains(text(), 'EndNote')]")
inut2.click()

# browser.quit()  # to close the browser
