import os
import pathlib
"""
import programa #--> verificar sobre import ainda
"""
# import programa.logistica

importar = ''

def verificar(arquivo:str,split:str='.'):
    try:
        if arquivo.split(split)[1] == 'py':
            return arquivo.split(split)[0]
    except:
        pass
    return None

arquivos = os.listdir('programa')
for arquivo in arquivos:
    if verificar(arquivo) != None:
        arquivos = arquivo.split('.')[0]
print(arquivos)
importar = f'programa\\{arquivo}'
exercicios = os.listdir('exercicios')
for pasta in exercicios:
    if pasta.split('_')[1] == arquivos:
        diretorio = f'exercicios\\{pasta}'
        break

##att proximo vez ---> usar como iterador, len(os.listdir()) e puxar onde o index - vai ser inLogistica1.txt etc...



inputs = [i for i in os.listdir(diretorio+"\\in")]
outputs =  [i for i in os.listdir(diretorio+"\\out")]

def tudoigual(lista):
    padrao = len(lista[0])
    for item in lista:
        if len(item) != padrao:
            return False
    return True
 
def organizar(lista:list[str]) -> list[str]:
    if tudoigual(lista):
        copia = list('-'*len(lista))
        for item in lista:
            contador = 0
            for outro in lista:
                if int(item[-5]) > int(outro[-5]):
                    contador +=1
            copia.insert(contador,item)
            print(copia)
            remover(copia,contador)
        return copia
    else:
        dicionario = {}
        for item in lista:
            dicionario[item] = int(pegarnumerico(item))
        copiadic = sorted(dicionario.values())
        retorno = {}
        for valor in copiadic:
            retorno[procurar(dicionario,valor)]=valor
        copiadic = []
        for chave in retorno:
            copiadic.append(chave)
        return copiadic
def procurar(dicionario:dict,valorkey):
    for chave in dicionario:
        if dicionario[chave] == valorkey:
            return chave
def pegarnumerico(frase:str):
    import re
    padrao = re.compile(r'[0-9]+')
    return padrao.search(frase).group()
    
def remover(lista:list,index,argumento='-'):
    for i in range(index,len(lista)):
        if lista[i] == argumento:
            lista.pop(i)
            return lista

            

inputs = organizar(inputs)
outputs = organizar(outputs)
def retirar(linha:str):
    # linha = list(linha)
    # linha.remove('\n')
    return linha.strip()

def filtrar(linha:str, argumento = '\n'):
    lista = linha.split(argumento)
    novalista = []
    for string in lista:
        if string != '':
            novalista.append(string.strip())
    return novalista


import sys
import io
importar = 'programa.logistica'
for index in range(len(inputs)):
    import programa.logistica
    originalsysin = sys.stdin
    originalsysout = sys.stdout
    capturaoutput = io.StringIO('')
    limpar = io.StringIO('')
    entrada = []
    saida = []
    
    sys.stdin= originalsysin
    sys.stdout = originalsysout
    try:
        with open(f'{diretorio}\\in\\{inputs[index]}','r') as inp: # in     
            with open(f'{diretorio}\\out\\{outputs[index]}','r') as out:  #out
                for linha in out.readlines(): # out
                    saida.append(retirar(linha)) # out
                sys.stdin = inp # in
                sys.stdout = capturaoutput
                programa.logistica.main()
                 # in
                entrada.append(capturaoutput.getvalue()) # in
    except EOFError as motivo:
        pass
    finally:           
        capturaoutput.close()
        sys.stdout = originalsysout
        sys.stdin = originalsysin
    nentrada = filtrar(entrada[0])
    
    
    if nentrada != saida:
        print('WRONG ANSWER')     
        quit()
    sys.modules.pop(f'programa.logistica',None)
print("CORRECT ANSWER")
