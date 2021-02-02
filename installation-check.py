from selenium import webdriver 
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome() 
# get google.co.in 
driver.get('https://www.linkedin.com')


username= "aashish2096@gmail.com"
password = "nokiax200"
#LinkedIn login
u_name = driver.find_element_by_name('session_key')
u_name.send_keys(username)
pwd =  driver.find_element_by_name('session_password')
pwd.send_keys(password)

button =  driver.find_elements_by_class_name('sign-in-form__submit-button')
# #driver.find_elements_by_xpath('/html/body/main/section[1]/div[2]/form/button')
print(button)
button[0].click()

#Generic Query in Google for Specific Data
driver.get('https://www.google.com')
search_query = driver.find_element_by_name('q')
search_query.send_keys('site:linkedin.com/in/ AND "University of Toronto" AND "Canada" AND "MSc" AND "ML"')
search_query.send_keys(Keys.RETURN)


#Filtering profile Links
elems = driver.find_elements_by_css_selector(".yuRUbf [href]")
links = [elem.get_attribute('href') for elem in elems]

print(len(links))
print(links[0])
driver.get(links[0])
print(driver.page_source())

#Filtering WebPage Links

elems = driver.find_elements_by_css_selector(".AaVjTc [href]")
links = [elem.get_attribute('href') for elem in elems]

print(len(links))
print(links[3])