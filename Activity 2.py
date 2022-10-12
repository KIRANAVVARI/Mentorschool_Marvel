#Importing the libraries required
import numbers
import pandas as pd
import json
from pandas.io.json import json_normalize
import requests
import datetime
import hashlib
import string

#Calling API to get name starts with A
namestartswith='a'
timestamp = datetime.datetime.now().strftime('%Y-%m-%d%H:%M:%S')
pub_key = '884a44db34b29d23db0d741475f0057d'
priv_key = '8fcb21f35a3d1e0bf9c13efe3ceed05aa57aba17'
limit='100'

def hash_params():
    hash_md5 = hashlib.md5()
    hash_md5.update(f'{timestamp}{priv_key}{pub_key}'.encode('utf-8'))
    hashed_params = hash_md5.hexdigest()

    return hashed_params

params = {'nameStartsWith':namestartswith,'limit':limit,'ts': timestamp, 'apikey': pub_key, 'hash': hash_params()};
res = requests.get('https://gateway.marvel.com:443/v1/public/characters?',
                    params=params)

char=list(string.ascii_lowercase)
df1=pd.DataFrame()
score=[]
for start in char:
    params['nameStartsWith']=start
    res1= requests.get('https://gateway.marvel.com:443/v1/public/characters?',
                    params=params)

    res1.json()
    data1=json.loads(res1.text)
    df2=pd.json_normalize(data1,record_path=['data','results'])
    score.append(len(df2.index))
    df1=pd.concat([df1,df2])
    del params['nameStartsWith']

total_characters=df1.loc[:,['name','comics.available','series.available','stories.available','events.available','id']].set_index('name')
print(total_characters)