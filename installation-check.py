from selenium import webdriver 
from selenium.webdriver.common.keys import Keys


username = str(input("Enter Email"))
password  = str(input("Enter Password"))

driver = webdriver.Chrome() 
# get google.co.in 
driver.get('https://www.linkedin.com')


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
with open('profile.txt','w') as f:
    f.write('\n'.join(links))
    f.close()
print(links[0])

#Filtering WebPage Links


# elems = driver.find_elements_by_css_selector(".AaVjTc [href]")
# links = [elem.get_attribute('href') for elem in elems]

# print(len(links))
# print(links[3])
driver.get(links[0])
val_source = driver.page_source
sect = driver.find_elements_by_class_name ("pv-profile-section__section-info section-info")
print(sect)

# print(val_source)
# with open('source.txt','w') as fs:
#     fs.write(val_source)
#     fs.close()
#print(driver.page_source)