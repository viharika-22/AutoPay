from selenium import webdriver
from time import sleep
driver= webdriver.Chrome('C:/Users/Ram Karthik/Downloads/chromedriver_win32/chromedriver')
driver.get("https://paytm.com/electricity-bill-payment")
message_box= driver.find_element_by_xpath("//*[@id='app']/div/div[4]/div[1]/div[1]/div/div[2]/div[2]/ul/li/div/div/input")
message_box.send_keys("Andhra Pradesh")
sleep(1)
board= driver.find_element_by_xpath("//*[@id='app']/div/div[4]/div[1]/div[1]/div/div[2]/div[2]/ul/li[2]/div/div/input").send_keys("Eastern Power Distribution Company of Andhra Pradesh Ltd. (APEPDCL)")
consumer_number= "116518V026247080"
sleep(2)
driver.find_element_by_xpath("//*[@id='app']/div/div[4]/div[1]/div[1]/div/div[2]/div[2]/ul/li[3]/div[1]/input").send_keys(consumer_number)
sleep(2)
driver.find_element_by_xpath("//*[@id='app']/div/div[4]/div[1]/div[1]/div/div[2]/div[5]/button").click()
input("enter any key after reading QR:")
sleep(7)
amount= input("enter amount")
driver.find_element_by_xpath("//*[@id='app']/div/div[4]/div[1]/div[1]/div/div[2]/div[2]/ul/li[5]/div[1]/div/input").send_keys(amount)
sleep(2)
driver.find_element_by_xpath("//*[@id='app']/div/div[4]/div[1]/div[1]/div/div[2]/div[5]/button").click()
sleep(5)
driver.find_element_by_xpath("//*[@id='app']/div/div[4]/div[2]/div/div[1]/div/ul/div[2]/li[2]/button").click()