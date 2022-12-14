from Packaging.Marvel_API_Case.Class_OOps import *
from keys import *
import json

def calling_API():
    api_key = input('Enter api_key')
    priv_key = input('Enter private key')
    limit='100'
    namestartswith=input('Enter namestartswith')
    try:
        timestamp = datetime.datetime.now().strftime('%Y-%m-%d%H:%M:%S')

        def hash_params():
            hash_md5 = hashlib.md5()
            hash_md5.update(f'{timestamp}{priv_key}{api_key}'.encode('utf-8'))
            hashed_params = hash_md5.hexdigest()

            return hashed_params


        params = {'nameStartsWith':namestartswith,'limit':limit,'ts': timestamp, 'apikey': api_key, 'hash':hash_params()};
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

calling_API()