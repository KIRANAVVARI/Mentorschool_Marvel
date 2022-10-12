#Importing the libraries required
import pandas as pd
import json
from pandas.io.json import json_normalize
import requests
import datetime
import hashlib

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

res.json()

#Creating a Data Frame using Pandas
data=json.loads(res.text)
df=pd.json_normalize(data,record_path=['data','results'])
df

#Fetching the column names in created DataFrame
for col in df.columns:
    print (col)

#Creating required Data Frame with required columns
characters_a=df.loc[:,['name','comics.available','series.available','stories.available','events.available','id']].set_index('name')
characters_a

#Fetching all charecters usin loops
import string

char=list(string.ascii_letters)
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
total_characters

#Creating a function with pub key, private key and starting letter as input
from logging import exception


def calling_API(api_key,hash,name_starts_with):
    try:
        import pandas as pd
        import json
        from pandas.io.json import json_normalize
        import requests
        import datetime
        import hashlib

        #Calling API to get name starts with A
        namestartswith=name_starts_with
        timestamp = datetime.datetime.now().strftime('%Y-%m-%d%H:%M:%S')
        pub_key = api_key
        priv_key = hash
        limit='100'

        def hash_params():
            hash_md5 = hashlib.md5()
            hash_md5.update(f'{timestamp}{priv_key}{pub_key}'.encode('utf-8'))
            hashed_params = hash_md5.hexdigest()

            return hashed_params


        params = {'nameStartsWith':namestartswith,'limit':limit,'ts': timestamp, 'apikey': pub_key, 'hash':hash_params()};
        res = requests.get('https://gateway.marvel.com:443/v1/public/characters?',
                        params=params)

        res.json()

        #Creating a Data Frame using Pandas
        data=json.loads(res.text)
        df=pd.json_normalize(data,record_path=['data','results'])

        #Creating required Data Frame with required columns
        characters_name=df.loc[:,['name','comics.available','series.available','stories.available','events.available','id']].set_index('name')
        return characters_name
    except KeyError:
        print('oops!Either of Api_key or Hash is not entered.Check again!')
    except ValueError:
        print('Entered invalid arguments!Check again!!')

#Function to filter data frames based on column condition
def filter_character(dataframe,column,condition):
    required_character=dataframe.loc[condition]
    return required_character
#Utilising functions with arguments-Examples
filter_character(total_characters,'comics.available',(total_characters['comics.available']>=2))
filter_character(total_characters,'events.available',(total_characters['events.available']==2))
