import os
import pandas as pd
import numpy as np

caminhoConverter = os.path.join(os.path.dirname(__file__),"converter")
caminhoConvertido = os.path.join(os.path.dirname(__file__),"convertido")

arquivosAConverter = os.listdir(caminhoConverter)

for arquivo in arquivosAConverter:
    if arquivo.split('.')[-1].lower() != 'csv':
        continue
    df = pd.read_csv(os.path.join(caminhoConverter,arquivo),sep=";",header=None)
    print(df)
    df = df.map(lambda x : f'"{x}"' if pd.notna(x) else f'""')
    print(df)
    df.to_csv(os.path.join(caminhoConvertido,arquivo),header=False, index = False,sep=";")
    print(f"Arquivo {arquivo} convertido. [OBS -> Todos campos agora vão estar \"entre aspas\".]")