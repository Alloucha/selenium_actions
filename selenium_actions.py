"""
Basic level:
1. Fill all fields in forms except "picture" 
2. Click on [Submit] button
3. Validate inputed data in modal window
Site: https://demoqa.com/automation-practice-form"""


from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://demoqa.com/automation-practice-form")
driver.find_element_by_css_selector("#firstName").send_keys("Yulia")
driver.find_element_by_css_selector("#lastName").send_keys("Alloucha")
driver.find_element_by_css_selector("#userEmail").send_keys("pomelochka23@gmail.com")
driver.find_element_by_css_selector("[for=gender-radio-2]").click()
driver.find_element_by_css_selector("#userNumber").send_keys("0664852689")
driver.find_element_by_css_selector("#dateOfBirthInput").click()
driver.find_element_by_css_selector("#dateOfBirthInput").send_keys(Keys.CONTROL, 'a')
driver.find_element_by_css_selector("#dateOfBirthInput").send_keys("10/07/2020")
driver.find_element_by_css_selector("#dateOfBirthInput").send_keys(Keys.TAB)
driver.find_element_by_css_selector("#subjectsInput").send_keys("Com")
driver.find_element_by_css_selector("#subjectsInput").send_keys(Keys.ENTER)
driver.find_element_by_xpath('//*[@id="hobbiesWrapper"]/div[2]/div[1]/label').click()
driver.find_element_by_css_selector('[for="hobbies-checkbox-2"]').click()
driver.find_element_by_css_selector('[for="hobbies-checkbox-3"]').click()
driver.find_element_by_css_selector("#currentAddress").send_keys("Kharkiv")
driver.find_element_by_css_selector("#currentAddress").send_keys(Keys.TAB)
driver.find_element_by_xpath('//*[@id="state"]').click()
driver.find_element_by_xpath('//*[@id="react-select-3-input"]').send_keys('NCR', Keys.ENTER)
driver.find_element_by_xpath('//*[@id="city"]/div/div[1]/div[1]').click()
driver.find_element_by_xpath('//*[@id="react-select-4-input"]').send_keys("Noida", Keys.ENTER)
driver.find_element_by_xpath('//*[@id="submit"]').click()