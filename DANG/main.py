from selenium import webdriver
driver = webdriver.Chrome()

driver.get('https://pioneer.particle.network/en/point')
driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/nav/header/ul[3]/li/a').click()
