#import the selenium modle package

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# create a new chrome session
driver = webdriver.Chrome("C:\\Users\\admin\\AppData\\Local\\Temp\\Temp1_chromedriver_win32.zip\\chromedriver.exe")
driver.get("https://www.blogger.com")
driver.maximize_window()
driver.implicitly_wait(15)
print("The title of the page is :")
print(driver.title)
print("The URL is :")
print(driver.current_url)

#Sing in the blogger page
a= driver.find_element_by_link_text("SIGN IN").send_keys(Keys.ENTER)

#Enter the email and password
input = driver.find_element_by_id('identifierId')
input.send_keys("nithya123bs@gmail.com")
input.send_keys(Keys.ENTER)
driver.implicitly_wait(5)
input = driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input')
input.send_keys("Mgtech@123")
input.send_keys(Keys.ENTER)

# Login sucessfully
print("Login Sucessfully")
driver.implicitly_wait(5)

#open blogger page and Create new post
a = driver.find_element_by_link_text("New post").click()
print("New Post open Sucessfully")

#link for insert image
driver.find_element_by_id('image').click()
print("Iamge link sucessfully open")

#upload the image in download list

#upload the image in download list
picture = "C:\\Users\\admin\\Downloads\\IMAGEDOWNLOAD\\image5.jpg"
#inputfile=driver.find_element(By.XPATH,'//*[@id="doclist"]/div/div[3]/div[2]/div/div[2]/div/div/div[1]/div[1]/div[1]/div[1]').send_keys(picture)

driver.find_element_by_tag_name('input').send_keys(picture)
print("upload  Sucessfully")
#//*[@id="doclist"]/div/div[3]/div[2]/div/div[2]/div/div/div[1]/div[1]/div[1]/div[1]

#add the image in folder
driver.find_elements_by_id('picker:ap:0').click()
print("Add image s sucessfully")
driver.implicitly_wait(15)
driver.refresh()
print("SUCESSFULLY RUNNING")

#close your webdriver page
driver.close()

