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

"""Advanced level:
Check next test cases:
1. Pagination 
2. Rows count selection
3. Add new worker
4. Delete worker
5. Delete all worker
6. Find worker in search field and edit it
7. Validate data in worker row after creating worker
8. Check search by all column values. https://demoqa.com/webtables
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://demoqa.com/webtables")

# Add new worker
driver.find_element_by_css_selector('#addNewRecordButton').click()
driver.find_element_by_css_selector('#firstName').send_keys('Olga')
driver.find_element_by_css_selector('#lastName').send_keys('Alloucha')
driver.find_element_by_css_selector('#userEmail').send_keys('pomelochka@gmail.com')
driver.find_element_by_css_selector('#age').send_keys('22')
driver.find_element_by_css_selector('#salary').send_keys('15000')
driver.find_element_by_css_selector('#department').send_keys('QA')
driver.find_element_by_css_selector('#submit').click()
driver.find_element_by_css_selector('#addNewRecordButton').click()
driver.find_element_by_css_selector('#firstName').send_keys('Olga')
driver.find_element_by_css_selector('#lastName').send_keys('Shapoval')
driver.find_element_by_css_selector('#userEmail').send_keys('pomelochk@gmail.com')
driver.find_element_by_css_selector('#age').send_keys('27')
driver.find_element_by_css_selector('#salary').send_keys('25000')
driver.find_element_by_css_selector('#department').send_keys('Java developer')
driver.find_element_by_css_selector('#submit').click()
driver.find_element_by_css_selector('#addNewRecordButton').click()
driver.find_element_by_css_selector('#firstName').send_keys('Kristi')
driver.find_element_by_css_selector('#lastName').send_keys('Baby')
driver.find_element_by_css_selector('#userEmail').send_keys('kitty@gmail.com')
driver.find_element_by_css_selector('#age').send_keys('19')
driver.find_element_by_css_selector('#salary').send_keys('25000')
driver.find_element_by_css_selector('#department').send_keys('UI/UX')
driver.find_element_by_css_selector('#submit').click()

# Rows count selection
driver.find_element_by_xpath(
    '//*[@id="app"]/div/div/div[2]/div[2]/div[1]/div[3]/div[2]/div/div[2]/span[2]/select/option[1]').click()

# delete worker
driver.find_element_by_xpath('//*[@id="delete-record-1"]/svg/path').click()

# find worker in search field and edit it

driver.find_element_by_css_selector('#searchBox').send_keys('Yu', Keys.ENTER)
driver.find_element_by_css_selector('#edit-record-4').click()
driver.find_element_by_css_selector('#age').send_keys(Keys.CONTROL, 'a')
driver.find_element_by_css_selector('#age').send_keys('28')
driver.find_element_by_css_selector('#submit').click()