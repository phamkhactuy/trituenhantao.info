#Extract to HTML
import urllib
import pandas as pd 
from bs4 import BeautifulSoup
url = "https://thefullsnack.com/"
req = urllib.request.Request(url, headers={'User-Agent' : "Magic Browser"}) 
con = urllib.request.urlopen( req )
soup = BeautifulSoup(con, 'html.parser')
type(soup)
title = soup.title
print(title.get_text())
text = soup.get_text()
soup.find_all('a')
all_links = soup.find_all("a")
df1 = df = pd.DataFrame({"a":["1"]}) 
for link in all_links:
    if link.get("href").startswith('/posts/') :
        if link.get("href").find("sketches")<0 :
            print("https://thefullsnack.com"+link.get("href"))
            url1 = "https://thefullsnack.com"+link.get("href")
            req1 = urllib.request.Request(url1, headers={'User-Agent' : "Magic Browser"}) 
            con1 = urllib.request.urlopen( req1 )
            soup1 = BeautifulSoup(con1, 'html.parser')
            type(soup1)
            title1 = soup1.title
            print(title1.get_text())
            text1 = soup1.get_text()
            soup1.find_all('a')
            all_links1 = soup1.find_all("div" , {"class": "container"})
            for link1 in all_links1:
                #print(link1.get_text())
                df2 = pd.DataFrame({"a":[link1]}) 
                df1=df1.append(df2)
                #print(df1, "\n") 
    #print(link.get("href"))
    #a1=link.get("href")
df1.to_csv(r'E:\thefullsnack_20191109html.txt', header=None, index=None, sep=' ', mode='a')
