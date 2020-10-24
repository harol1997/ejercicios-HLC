from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys

#necesitan instalar el chrome driver
driver = webdriver.Chrome('chromedriver.exe')
driver.get('https://web.whatsapp.com/')
print("Enter your code QR")
sleep(5)
print("El programa ha finalizado correctamente")
search_user = driver.find_element_by_class_name("_3FRCZ")
user = input("Ingrese el usuario: ")
search_user.send_keys(user)
search_user.send_keys(Keys.RETURN)#enter
sleep(3)
element_send = driver.find_element_by_xpath('//footer')
element_send_message = element_send.find_element_by_class_name("_3FRCZ")
message = input("Ingrese el mensaje: ")
for i in range(10):
    element_send_message.send_keys(message)
    element_send_message.send_keys(Keys.RETURN)#enter
#driver.close()#cerrar el chrome
