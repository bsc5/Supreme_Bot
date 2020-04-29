import selenium
import time
from selenium import webdriver

PATH = "C:\selenium\chromedriver"
driver = webdriver.Chrome(PATH)

data = {
    "name": "test testin",
    "email": "testemail@gmail.com",
    "tel": "3103103110",
    "addr": "1234 Demo Road",
    "addr_zip": "20811",
    "city": "Los Santos",
    "number": "12313131331",
    "ccv": "321",
}

driver.get("https://www.supremenewyork.com/")
time.sleep(0)
driver.find_element_by_xpath("/html/body/div[2]/nav/ul/li[4]/a/span").click()
time.sleep(4)
driver.find_element_by_xpath("/html/body/div[2]/div[3]/div/ul/li[8]/a/img").click()
time.sleep(2)
driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/form/fieldset[2]/input").click()
time.sleep(1)
driver.find_element_by_xpath("/html/body/div[2]/div/div[1]/div/a[2]").click()
name = driver.find_element_by_xpath("/html/body/div[2]/div[1]/form/div[2]/div[1]/fieldset/div[1]/input")\
    .send_keys(data["name"])
email = driver.find_element_by_xpath("/html/body/div[2]/div[1]/form/div[2]/div[1]/fieldset/div[2]/input")\
    .send_keys(data["email"])
tel = driver.find_element_by_xpath("/html/body/div[2]/div[1]/form/div[2]/div[1]/fieldset/div[3]/input")\
    .send_keys(data["tel"])
addr = driver.find_element_by_xpath("/html/body/div[2]/div[1]/form/div[2]/div[1]/fieldset/div[4]/div[1]/input")\
    .send_keys(data["addr"])
addr_zip = driver.find_element_by_xpath("/html/body/div[2]/div[1]/form/div[2]/div[1]/fieldset/div[5]/div[1]/input")\
    .send_keys(data["addr_zip"])
time.sleep(0)
number = driver.find_element_by_xpath("/html/body/div[2]/div[1]/form/div[2]/div[2]/fieldset/div[1]/div[2]/input")\
    .send_keys(data["number"])
ccv = driver.find_element_by_xpath("/html/body/div[2]/div[1]/form/div[2]/div[2]/fieldset/div[1]/div[3]/div[2]/input")\
    .send_keys(data["ccv"])
terms_and_conditions = driver.find_element_by_xpath("/html/body/div[2]/div[1]/form/div[2]/div[2]/fieldset/p[2]/label/div/ins").click()
proccess = driver.find_element_by_xpath("/html/body/div[2]/div[1]/form/div[3]/div[2]/input").click()

captia = input("type done when capta is finished: ")
if captia == "done":
    print("done")
else:
    print("incomplete")
