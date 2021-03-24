from selenium import webdriver
# from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome('chromedriver')
browser.get("https://scholar.google.com/")

search_feild = browser.find_element_by_id("gs_hdr_tsi")
search_feild.send_keys("Melville, N., Kraemer, K., & Gurbaxani, V. (2004). Information technology and organizational performance: An integrative model of IT business value. MIS quarterly, 28(2), 283-322.")
search_feild.submit()

menue_bar = browser.find_element_by_id("gs_hdr_mnu")
menue_bar.click()

browser.implicitly_wait(1)

setting_button = browser.find_element_by_partial_link_text("Settings")
setting_button.click()

l = browser.find_element_by_xpath("//input[@value='yes']")
l.click()

inut = browser.find_element_by_id("gs_settings_import-bl")
inut.click()

end_note_option = browser.find_element_by_xpath("//a[contains(text(), 'EndNote')]")
end_note_option.click()

end_note_option = browser.find_element_by_xpath("//span[contains(text(), 'Save')]")
end_note_option.click()

# browser.quit()  # to close the browser
