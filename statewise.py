from selenium import webdriver
from bs4 import BeautifulSoup as BeautifulSoup
import pandas as pd 


driver = webdriver.Chrome(executable_path = r'E:\chromedriver.exe')
driver.get("https://www.mohfw.gov.in/")

content = driver.page_source
soup = BeautifulSoup(content)

div=soup.find('div', attrs={'id':'cases'})

sno=[]
name=[]
total=[]
cured=[]
death=[]
j=0
for i in div.find_all('td') :
    j+=1
    if(j==2):
        name.append(i.text)
    elif(j==3):
        a=int(i.text)
    elif(j==4):
        b=int(i.text)
        total.append(a+b)
    elif(j==5):
        cured.append(i.text)
    elif(j==6):
        death.append(i.text)
        j=0
driver.quit()
name.pop()
total.pop()
cured.pop()
death.pop()

cured = list(map(int, cured)) 
death = list(map(int, death)) 

df = pd.DataFrame(list(zip(name,total,cured,death)),columns =['Name of State', 'Total Cases', 'Cured','Deaths'])

import datetime
x = datetime.datetime.now()
d=x.strftime("%d")
t=x.strftime("%I")
m=x.strftime("%M")
p=x.strftime("%p")

df.to_csv('state_'+d+' '+t+'-'+m+p+'.csv',index=False)
