from selenium import webdriver
from bs4 import BeautifulSoup as BeautifulSoup
import pandas as pd 

a=[]
driver = webdriver.Chrome(executable_path = r'E:\chromedriver.exe')
driver.get("https://www.mohfw.gov.in/")

content = driver.page_source
soup = BeautifulSoup(content)


div=soup.find('div', attrs={'class':'information_row'})

for i in div.find_all('span', attrs={'class':'icount'}) :
    a.append(i.text)

driver.quit()
a.pop(0)
a.pop()

df = pd.DataFrame([a],columns =['Active COVID 2019 cases','Cured/discharged cases', 'Death cases'])

import datetime
x = datetime.datetime.now()
d=x.strftime("%d")
t=x.strftime("%I")
m=x.strftime("%M")
p=x.strftime("%p")

df.to_csv('India_'+d+' '+t+'-'+m+p+'.csv',index=False)