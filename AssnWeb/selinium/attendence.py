
from lib2to3.pgen2 import driver
from select import select
from tkinter.tix import Select
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

 
def auto(username, password,latereason):
    user_name=username
    password=password
    reason=latereason
    d=webdriver.Firefox()
    d.get('http://hrm.rtbi.in')
    element=d.find_element_by_id('email')
    element.send_keys(user_name)
    element=d.find_element_by_id('pwd')
    element.send_keys(password)
 
    element.send_keys(Keys.RETURN)
    
    select = Select(d.find_element_by_xpath('//*[@id="Waiting"]'))

    
    element=d.find_element_by_id('latereason')
    select.select_by_visible_text('Afternoon session')
    element.send_keys(reason)
 
auto('naveens@tenet.res.in','15440','Traffic')
 