from selenium import webdriver
from selenium.webdriver.firefox.options import Options

options=Options()
options.headless=True
driver = webdriver.Firefox(options=options)

driver.get('https://www.guvi.in')
data = [driver.title, driver.current_url,driver.page_source]
print(data)
response = driver.get('https://www.guvi.in')
data =driver.page_source
with open('assn1.txt', 'w') as a:
    a.write(data)
    a.close()


driver.quit()