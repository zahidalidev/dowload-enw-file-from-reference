from selenium import webdriver
# from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome('chromedriver')
browser.get("https://scholar.google.com/")

# find search feild and then search
# search_feild = browser.find_element_by_id("gs_hdr_tsi")
# search_feild.send_keys("Melville, N., Kraemer, K., & Gurbaxani, V. (2004). Information technology and organizational performance: An integrative model of IT business value. MIS quarterly, 28(2), 283-322.")
# search_feild.submit()

# click menue icon
menue_bar = browser.find_element_by_id("gs_hdr_mnu")
menue_bar.click()

# wait for 1 sec
browser.implicitly_wait(1)

# open setting
setting_button = browser.find_element_by_partial_link_text("Settings")
setting_button.click()

# select radio button
l = browser.find_element_by_xpath("//input[@value='yes']")
l.click()

# option options
inut = browser.find_element_by_id("gs_settings_import-bl")
inut.click()

# select option of end note
end_note_option = browser.find_element_by_xpath("//a[contains(text(), 'EndNote')]")
end_note_option.click()

# save setting
end_note_option = browser.find_element_by_xpath("//span[contains(text(), 'Save')]")
end_note_option.click()


### use loop here to download multiple files

# find search feild and then search
search_feild = browser.find_element_by_id("gs_hdr_tsi")
search_feild.send_keys("Melville, N., Kraemer, K., & Gurbaxani, V. (2004). Information technology and organizational performance: An integrative model of IT business value. MIS quarterly, 28(2), 283-322.")
search_feild.submit()

# downloading file
import_to_endNote = browser.find_element_by_partial_link_text("Import into EndNote")
import_to_endNote.click()


# browser.quit()  # to close the browser
