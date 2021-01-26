from selenium import webdriver 
from selenium.webdriver.common.keys import Keys

class Navigation:

    def __init__(self,username,password):
        self.driver = webdriver.Chrome()
        self.username = username
        self.password = password

    def navigateToUrl(self,url):
        self.driver.get(url)

    def loginToLinkedIn(self):
        u_name = self.driver.find_element_by_name('session_key')
        u_name.send_keys(self.username)
        pwd =  self.driver.find_element_by_name('session_password')
        pwd.send_keys(self.password)

    def getListOfQueryPages(self,query):
        temp_ = self.driver.find_element_by_name('q')
        temp_.send_keys(query)
        temp_.send_keys(Keys.RETURN)
        elems = self.driver.find_elements_by_css_selector(".AaVjTc [href]")
        links = [elem.get_attribute('href') for elem in elems]
        return links

    def findProfileLinks(self,pageQuery):
        self.driver.get(pageQuery)
        elems = self.driver.find_elements_by_css_selector(".yuRUbf [href]")
        user_links = [elem.get_attribute('href') for elem in elems]
        return user_links
