from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class naveen:
    drv = webdriver.Firefox()

    def click_link_by_id(self, link_id,url):
        try:
            self.drv.get(url)
            link_id=self.drv.find_element(by=By.ID, value=link_id)
            if link_id:
                time.sleep(4)
                link_id.click()
        except:
            print('error:ID not found !')
a = naveen()

id_1="w3loginbtn"
url ="https://www.w3schools.com/"

a.click_link_by_id(id_1,url)
