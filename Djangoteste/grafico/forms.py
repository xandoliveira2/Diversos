from django import forms
import pymongo as pm
import pandas as pd

class DensityFilterForm(forms.Form):
    client = pm.MongoClient('mongodb://localhost:27017/')
    db = client['teste']
    collection = db['simlulandodados1']
    df = pd.DataFrame(collection.find())
    df['data'] = pd.to_datetime(df['data'],format='%d/%m/%Y') 
    df['data'] = df['data'].dt.strftime('%d/%m/%Y') 
    df = df.sort_values('data')
    data_choices = [(data, data) for data in df['data'].unique()]

    dia = forms.ChoiceField(choices=data_choices)