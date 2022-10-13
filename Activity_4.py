from Packaging.Marvel_API_Case.Class_OOps  import *
def Filtering_characters():
    data = input('Enter the data frame:')
    column=input('Enter column name:')
    condition=input('Enter Any condition on that column:')
    value=input('Enter the value:')
    
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

