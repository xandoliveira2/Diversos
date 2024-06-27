#validador de senha onde>
#1- nao pode conter caracteres especiais 
#2- tem que ter ao menos 1 letra maiuscula, 1 minuscula e 1 numero
#3- tem que ter entre 6 a 15 digitos
#4- nao pode ser em sequencia, então, nao pode ser: AB ou 12 ou ab
import os
os.system('cls')
class solucao:
    m1 = bool()
    m2 = bool()
    m3 = bool()
    m4 = bool()
    minhavariavel = bool()
    rt1 = 0
    rt2 = 0
    rt3 = 0
    try:
        codificador = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
        proibidos = '!,.;/:><?-_=+\|\'"áéíóúÀÈÌÒÙÁÉÍÓÚàèìòù'
        def pegarindex(x:str) -> int:
            for i in solucao.codificador:
                if i == x:
                    return solucao.codificador.index(i)

        def validador(x:str):
            cont = 0
            maiusculas = 0
            minusculas = 0
            numeros = 0
            if len(x) < 6:
                print(f'Erro! A senha deve conter no minimo 6 letras ({len(x)} letras inseridas) ')
                solucao.m4 = False
                pass
            elif len(x)>15:
                print(f'Erro! A senha deve conter no maximo 15 letras ({len(x)} letras inseridas) ')
                solucao.m4 = False
                pass  
            else:
                print('Conter entre 6 - 15 letras: OK')
                solucao.m4 = True 

            for i in x:
                for c in solucao.codificador:  
                    if c == i:
                        try:
                            if solucao.rt1 == 1:
                                break
                            if x[x.index(i)+1] == solucao.codificador[solucao.codificador.index(c)+1]:
                                print('Erro! Letras seguidas')
                                solucao.m1 = False
                                solucao.rt1 = 1
                                break 
                            else:
                                if solucao.rt3 == 1:
                                    break
                                else:
                                    print('Sem letras consecutivas: ok')
                                    solucao.m1 = True
                                    solucao.rt3 = 1
                        except IndexError:
                            pass
                
                if i in solucao.proibidos:
                   print('Erro! Caractere especial identificado. ')
                   solucao.m2 = False
                   break
                else:
                    cont += 1

                if i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
                    maiusculas += 1
                elif i in "abcdefghijklmnopqrstuvwxyz":
                    minusculas += 1
                elif i in "0123456789":
                    numeros += 1
            if cont == len(x):
                print('Senha não contém caracteres especiais: OK')
                solucao.m2 = True
            if numeros and maiusculas and minusculas != 0:
                print('Conter ao menos 1 maiuscula, 1 minuscula e 1 numero: OK')
                solucao.m3 = True
            if numeros == 0:
                print('Erro! Senha não possui numero')
                solucao.m3 = False
               # raise 'erro numero'
            if maiusculas == 0:
                print('Erro! Senha não possui letras maiusculas')
                solucao.m3 = False
               # raise 'erro maiuscula'
            if minusculas == 0:
                print('Erro! Senha não possui letras minusculas')
                solucao.m3 = False            
                #raise 'erro minuscula'
            solucao.minhavariavel = solucao.m1 and solucao.m2 and solucao.m3 and solucao.m4
            print(solucao.m1,solucao.m2,solucao.m3,solucao.m4)
            return solucao.minhavariavel
    finally:
        pass

       

print(solucao.validador('1294821'))



