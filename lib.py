import requests
from bs4 import BeautifulSoup
import pandas as pd

URL = 'https://lib.rs/command-line-utilities'

page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')

# find all package names
divs = soup.select('.h > h4')
names=[]
for div in divs:
    names.append(div.text.strip())

# find all package downloads

metas = soup.select('.meta')
downloads=[]
for meta in metas:
    if(mytitle:=meta.find(class_='downloads')):
        parts = str(mytitle).split()[2].split('="')[1]
        downloads.append(int(parts))
    else:
        # some libraries do not have downloads class
        downloads.append(0)

# create a dataframe using pandas
data_tuples = list(zip(names,downloads))
df=pd.DataFrame(data_tuples, columns=['Name','Downloads'])
# sort by number of downloads
df = df.sort_values(by='Downloads', ascending=False)

df.head(20)

print(df)