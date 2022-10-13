from Total_Functions import *
from Activity_3 import calling_API
import argparse
from Packaging.Marvel_API_Case.Class_OOps import *

parser = argparse.ArgumentParser(description='Gettinf characters of Marvel Using API')
parser.add_argument('api_key',type=str,help='provide the api_key/public_key')
parser.add_argument('hash',type=str,help='provide the hash/private_key')
parser.add_argument('namestartswith',type=str,help='provide starting letter')
timestamp = datetime.datetime.now().strftime('%Y-%m-%d%H:%M:%S')
args =parser.parse_args
api_key = getattr(args,'api_key')
hash=getattr(args,'hash')
name_starts_with=getattr(args,'namestartswith').lower()
limit='100'
Marvel_Characters = calling_API(api_key,hash,name_starts_with)
print(Marvel_Characters)
