from os import listdir
from re import compile
import sys
from io import StringIO
from importlib import import_module
from shutil import rmtree
import concurrent
import concurrent.futures

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

arquivos = listdir('programa')
for arquivo in arquivos:
    if verificar(arquivo) != None:
        arquivos = arquivo.split('.')[0]

importar = f'programa.{arquivos}'
exercicios = listdir('exercicios')
for pasta in exercicios:
    if pasta.split('_')[1] == arquivos:
        diretorio = f'exercicios\\{pasta}'
        break
##att proximo vez ---> usar como iterador, len(os.listdir()) e puxar onde o index - vai ser inLogistica1.txt etc...



inputs = [i for i in listdir(diretorio+"\\in")]
outputs =  [i for i in listdir(diretorio+"\\out")]

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
    padrao = compile(r'[0-9]+')
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


def main():
    for index in range(len(inputs)):
    
        originalsysin = sys.stdin
        originalsysout = sys.stdout
        capturaoutput = StringIO('')
        # limpar = io.StringIO('')
        entrada = []
        saida = []

        sys.stdin= originalsysin
        sys.stdout = originalsysout
        try:
            with open(f'{diretorio}\\in\\{inputs[index]}','r',encoding='UTF-8') as inp: # in     
                with open(f'{diretorio}\\out\\{outputs[index]}','r',encoding='UTF-8') as out:  #out
                    for linha in out.readlines(): # out
                        saida.append(retirar(linha)) # out
                    sys.stdin = inp # in
                    sys.stdout = capturaoutput
                    
                    try:
                        with concurrent.futures.ThreadPoolExecutor() as ex:
                            ex.submit(import_module,importar).result(5)
                            
                    except concurrent.futures.TimeoutError:
                        print("TIME LIMIT EXCEEDED")    
                    
                    #import_module(importar)   
                     # in
                    entrada.append(capturaoutput.getvalue()) # in
        except EOFError:
            pass
        finally:           
            capturaoutput.close()
            sys.stdout = originalsysout
            sys.stdin = originalsysin
        print(entrada)
        nentrada = filtrar(entrada[0])



        print('entrance',nentrada,'\nexit',saida)
        if nentrada != saida:
            print('WRONG ANSWER')
            try:
                rmtree('programa\\__pycache__')   
            except:
                pass  
            quit()
        sys.modules.pop(importar,None)
    print("CORRECT ANSWER")
    try:
        rmtree('programa\\__pycache__') 
    except:
        pass
   
main()