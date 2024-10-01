conta_bancaria = 0
limite_saques = 3
extratos = []
controle = True
from time import sleep
while controle:
    print('-'*50)
    print('Bem vindo ao Banco\n')
    print('O que deseja fazer?')
    print('1 - Depositar')
    print('2 - Sacar')
    print('3 - Ver saldo atual')
    print('4 - Ver extrato')
    print('0 - Sair\n')
    print('-'*50)
    opcao_usuario = int(input())
    match opcao_usuario:
        case 1:
            valor_deposito  = int(input('Insira o valor para depósito: '))
            if valor_deposito>0:
                conta_bancaria+= valor_deposito
                extratos.append(f'Depósito realizado no valor de R${valor_deposito},00')
                print(f'\n\n\n\n\n\nDepósito realizado no valor de R${valor_deposito},00\n\n\n\n\n\n')
            else: 
                print('\n\n\n\n\n\nOperação cancelada!\nValor de depósito não pode ser negativo\n\n\n\n\n')
                extratos.append('Operação cancelada : Valor negativo para depósito')
            sleep(3)
        case 2:
            if limite_saques == 0:
                print('\n\n\n\n\n\nLimite de saques atingido, tente novamente amanhã\n\n\n\n\n\n')
                extratos.append('Operação cancelada : Limite de saque atingido')
                sleep(3)
            else:    
                valor_saque = int(input('Digite valor para saque: '))
                
                if valor_saque < 0: #Controle para garantir que o número sempre será positivo
                    valor_saque = -valor_saque
                if valor_saque> 500:
                    print('\n\n\n\n\nOperação cancelada : Saque não deve ultrapassar R$500,00\n\n\n\n\n')
                    extratos.append('Operação cancelada : Saque ultrapassou limite')
                else:
                    if  conta_bancaria - valor_saque>=0:
                        conta_bancaria-= valor_saque
                        extratos.append(f'Saque no valor de R${valor_saque},00')
                        limite_saques-=1
                        print(f'\n\n\n\n\nSaque no valor de R${valor_saque},00\nSaldo atual R${conta_bancaria},00\n\n\n\n\n') 
                    else: 
                        print('\n\n\n\n\n\nOperação cancelada!\nVocê não possui saldo suficiente\n\n\n\n\n\n')
                        extratos.append('Operação cancelada : Saldo insuficiente para saque')
                sleep(3)
        case 3:
            print(f'\n\n\n\n\n\nSaldo atual R${conta_bancaria},00\n\n\n\n\n\n')
            sleep(3)
        case 4:
            if not extratos:
                print('\n\n\n\n\nSem Dados de histórico\n\n\n\n\n\n')
            for texto in extratos:
                print(texto)  
            input('\n\nPressione enter para continuar')
        case 0:
            controle = False
            print('\n\n\n\n\n\nEncerrando programa\n\n\n\n\n\n')
            sleep(3)

        case _:
            print('\n\n\n\n\n\nOpção inválida\n\n\n\n\n\n')
            sleep(1.8)
            
               
