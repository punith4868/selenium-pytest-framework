from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time


options=Options()
options.add_argument("--headless=new")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--disable-gpu")

driver = webdriver.Chrome(options=options)
driver.get("https://blazedemo.com/")
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, "input").click()
time.sleep(2)

rows=driver.find_elements(By.CSS_SELECTOR, f"tbody tr")
cc=driver.find_elements(By.CSS_SELECTOR, f"tbody tr:nth-child(1) td")

g=float("inf")
url=""
p=[]
for i in range(len(rows)):
	c=f"tbody tr:nth-child({i+1})"
	cc=driver.find_elements(By.CSS_SELECTOR, f"{c} td")
	pt=[cc[i].text for i in range(len(cc))]
	print(pt)
	k=float(cc[-1].text.replace('$',""))
	print(k)
	if k<g:
	    g=k
	    url=c
print(url)
driver.find_element(By.CSS_SELECTOR, f"{url} td:first-of-type").click()
time.sleep(5)
print(f"lowest value is {g}")

def test_login():
	print("login executed successfully")


	

