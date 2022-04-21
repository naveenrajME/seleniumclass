from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options


class first:
    d = webdriver.Firefox()

    # fetch the title of the web page
    def get_title(self, url):
        self.d.get(url)
        return (self.d.title)

    # fetch the URL of the web page
    def browser_url(self,url):
        self.d.get(url)
        return (self.d.current_url)
    
    def auto(self,username, password):
        user_name=username
        password=password
        self.d.get('http://bounce.esmito.com:8084/cms/index.jsp')
        element=self.d.find_element_by_id('username')
        element.send_keys(user_name)
        element=self.d.find_element_by_id('password')
        element.send_keys(password)
        element.send_keys(Keys.RETURN)
        

    # fetch the entire webpage using Selenium Automation
    def get_data(self,url):
        self.d.get(url)
        return(self.d.page_source)


s = first()
s.auto('bounce','bounce@123')

# url = 'http://bounce.esmito.com:8084/cms'

# print(s.get_data(url))