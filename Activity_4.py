from __init__ import *
from Activity_2 import *
def Filtering_characters(data,column,condition,value):
    if condition=='>':
        required_data = data[data[column]>value]
    elif condition=='<':
        required_data = data[data[column]<value]
    elif condition =='=':
        required_data = data[data[column]==value]
    elif condition == ('<=' or '=<'):
        required_data = data[data[column]<=value]
    elif condition == ('>=' or '=>'):
        required_data = data[data[column]<=value]
        
    return required_data

Filtering_characters(total_characters,'comics.available','>=',50)