import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
%matplotlib inline
from urllib.request import urlopen
from bs4 import BeautifulSoup
###
import MySQLdb
db = MySQLdb.connect(host="127.0.0.1", port=3306, user="root", passwd="Quynh307", db="PKTUY")
c = db.cursor()
a1="https://kipalog.com"
c.execute("SELECT distinct url,cp,cm FROM kypalog1 where (url like 'https://kipalog.com/posts%') order by stt")
a2=0
for url, cm,cp in c:
    #print(f'First name: {url}, Last name: {datcre}')
    if url.startswith('https://kipalog.com'):
        a2=a2+1
        db.commit()
        print(f'{a2}First name: {url}, Last name: {cm}')
        url1 = url
        html = urlopen(url)
        soup = BeautifulSoup(html, 'html.parser')
        type(soup)
        title = soup.title
        #print(title)
        text = soup.get_text()
        soup.find_all('a')
        all_links = soup.find_all("a")
        for link in all_links:
            print(link.get("href"))
            if link.get("href")!=None:
                a1=link.get("href")
                if a1.startswith('/'):
                    a1=f"https://kipalog.com{a1}"
                if len(a1)<450 or a1.startswith('https://kipalog.com'):
                    sql=f"insert into kypalog1(url) values('{a1}')"
                    c.execute(sql)
        db.commit()


#print(c.fetchone())
