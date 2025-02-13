while True:
    divida = round(float(input().replace(",",".")),2)
    if divida == 0:
        break
    entrada = input()
    if ',' in entrada:
        entrada.replace(',','.')
    pagamento = round(float(entrada),2)
    ValoresDisponiveis = [100,50,20,10,5,2,1,0.5,0.25,0.10,0.05]

    if divida - pagamento == 0:
        print("Não há troco, o valor pago é o valor da dívida")
    elif divida - pagamento > 0 or pagamento > divida:
        resposta = dict()
        falta = abs(round((divida - pagamento),2))
        indexValoresDisponiveis = 0
        while falta != 0:
    
            if round(falta - ValoresDisponiveis[indexValoresDisponiveis],2) >= 0.00:
                if resposta.get(ValoresDisponiveis[indexValoresDisponiveis]) != None:
                    resposta[ValoresDisponiveis[indexValoresDisponiveis]] +=1
                    falta = round((falta - ValoresDisponiveis[indexValoresDisponiveis]),2)
                
                else:
                    resposta[ValoresDisponiveis[indexValoresDisponiveis]] = 1
                    falta = round((falta - ValoresDisponiveis[indexValoresDisponiveis]),2)
                    
            else:
                indexValoresDisponiveis +=1
        
        print("\t_____________________________________________")
        print(f"\t|{"Notas / Moedas":^30}\t|{"Quantidade":^11}|")
        print("\t---------------------------------------------")
        for chave,valor in resposta.items():
            if chave == int(chave):
                if int(chave) == 5 or int(chave) == 2 or int(chave) == 1:
                    print(f"\t|{F"R$ {chave},00":^15}\t\t|{valor:^11}|")
                    print("\t---------------------------------------------")
                else: 
                    print(f"\t|{F"R${chave},00":^15}\t\t|{valor:^11}|")
                    print("\t---------------------------------------------")
                
            else:
                if chave == 0.1 or chave == 0.5:
                    print(f"\t|{F"R$ {chave}0":^15}\t\t|{valor:^11}|")
                    print("\t---------------------------------------------")
                else:    
                    print(f"\t|{F"R$ {chave}":^15}\t\t|{valor:^11}|")
                    print("\t---------------------------------------------")
    # elif pagamento > divida:
    #     print()
    else:
        print(f"O saldo de {pagamento} é insuficiente para a divida de {abs(divida)}")
        
    