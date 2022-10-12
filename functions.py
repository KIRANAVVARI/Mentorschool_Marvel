from ctypes.wintypes import CHAR
import pandas as pd
import json
from pandas.io.json import json_normalize
import requests
import datetime
import hashlib
import os
import argparse

parser = argparse.ArgumentParser(description='Gettinf characters of Marvel Using API')
parser.add_argument('api_key',type=CHAR,help='public_key')
parser.add_argument('hash',type=CHAR,help='private_key')
parser.add_argument('namestartswith',type=CHAR,help='starting letter')
args = parser.parse_args
def calling_API(api_key,hash,name_starts_with):
    try:
        
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
        print(characters_name)
    except TypeError:
        print('oops!Either of Api_key or Hash is not entered.Check again!')
    except ValueError:
        print('Entered invalid arguments!Check again!!')
if __name__=='__main__':
    print (calling_API(args.api_key,args.hash,args.namestartswith))


def Filtering_characters(data,column,condition,value):
    if condition=='>':
        required_data = data[data[column.capitalize()]>value]
    elif condition=='<':
        required_data = data[data[column.capitalize()]<value]
    elif condition =='=':
        required_data = data[data[column.capitalize()]==value]
    elif condition == ('<=' or '=<'):
        required_data = data[data[column.capitalize()]<=value]
    elif condition == ('>=' or '=>'):
        required_data = data[data[column.capitalize()]<=value]
        
    return required_data