from os import listdir
from re import compile
import sys
from io import StringIO
from importlib import import_module
from shutil import rmtree
import threading
sinal = 0
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
    try:
        if pasta.split('_')[1] == arquivos:
            diretorio = f'exercicios\\{pasta}'
            break
    except IndexError:
        if str(pasta) == arquivos:
            diretorio = f'exercicios\\{str(pasta)}'
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
                if pegarnumerico(item) > pegarnumerico(outro):
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
    return int(padrao.search(frase).group())
    
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
def rodar1():
    import_module(importar)
def teste(orig,atual):
    sys.stdout = orig
    print('sopa haha') 
    sys.stdout = atual
# def errors_time():
#     global sinal
#     if sinal == 0:
#         threading.Event.set()
#         raise Exception("TIME LIMIT EXCEEDED")
CONTADOR = 0

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
                    # n1 = threading.Timer(5,errors_time)#teste(originalsysout,sys.stdout)
                    
                    # n1.start()
                    # n2 = threading.Thread(target=rodar1(),daemon=False)
                    # n2.run()
                    # n1.cancel()

                    # global sinal
                    # sinal = 1   
                    import_module(importar)
                     # in
                    entrada.append(capturaoutput.getvalue()) # in
                    '1\n 2\n 3\n'
        except EOFError:
            pass
        finally:           
            capturaoutput.close()
            sys.stdout = originalsysout
            sys.stdin = originalsysin
        # print(entrada)
        nentrada = filtrar(entrada[0])



        print('entrance',nentrada,'\nexit',saida)
        if nentrada != saida:
            print('WRONG ANSWER')

            try:
                rmtree('programa\\__pycache__')   
            except:
                pass  
            
        else:
            global CONTADOR
            CONTADOR +=1
        sys.modules.pop(importar,None)
    print("CORRECT ANSWER")
    marcador = len(listdir(f'{diretorio}\\in'))
    print(f"Você acertou {CONTADOR} de {marcador}")


    try:
        rmtree('programa\\__pycache__') 
    except:
        pass
main()