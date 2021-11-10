import pandas as pd
import pickle
import requests
from bs4 import BeautifulSoup

df = pd.read_csv('articles.csv')
url = 'https://github.com/huseyn-guliyev/test-wflow-2/tree/main/data'
response = requests.get(url)
w_soup =  BeautifulSoup(response.text, 'html.parser')
txt = w_soup.find_all('a', attrs={'class':'js-navigation-open Link--primary'})
if len(txt) == 1:
    x = 0
else:
    x = int(txt[1].get('title').split('_')[-1])
lst = []
for i in range(x, x+400): #len(df)
    try: 
        url = 'https://az.wikipedia.org/wiki/' + df['title'].iloc[i]
        response = requests.get(url)
        w_soup =  BeautifulSoup(response.text, 'html.parser')
        txt = w_soup.find_all('p')
        s = ''
        for j in range(len(txt)):
            s += txt[j].text.replace('\n', " ")
            s += ' '
        lst.append(s)
        
    except:
        lst.append('ERROR')

with open("./data/till_{}.pickle".format(x+100), "wb") as fp:
    pickle.dump(lst, fp)
    fp.close()
