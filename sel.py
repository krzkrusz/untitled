from selenium.webdriver import Firefox

#C:\Users\u112877\Downloads\geckodriver
url = "https://www.igame.com/eye-test/"

driver = Firefox()

driver.get(url)

driver.switch_to.frame(driver.find_element_by_tag_name('Iframe'))



for i in range(0,1000):
    el=driver.find_element_by_class_name("thechosenone")
    el.click()


