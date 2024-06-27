def main():
    emp_qtd = input().split(' ')
    empresas = int(emp_qtd[0])
    qPadrao = int(emp_qtd[1])
    diasTotais = int(input())
    diaAtual = 1
    matrixtotal = []
    resultado = []
    for i in range(0,empresas):
        lista = []
        for j in range(0,empresas):
            lista.append(0)
            if j == empresas-1:
                matrixtotal.append(lista)
    while diaAtual < diasTotais+1:
        diaAtual +=1
        entrada = input()
        if 'dia' in entrada.lower(): 
            for i in range(0,empresas):
                for j in range(0,empresas):
                    if i == j:
                        pass
                    else:
                        entrada2 = input().split()
                        matrixtotal[i][j] += int(entrada2[-1]) 
        resultado.append(f"Final dia {diaAtual-1}")
        contador = 0
        for i in range(0,empresas):
            for j in range(0,empresas):
                if matrixtotal[i][j] >= qPadrao and matrixtotal[j][i] >=qPadrao:
                    viajem1= 1
                    viajem2 =1
                    matrixtotal[i][j] -= qPadrao
                    matrixtotal[j][i] -=qPadrao
                    while True:
                        if matrixtotal[i][j] >=qPadrao:
                            viajem1 += 1
                            matrixtotal[i][j] -= qPadrao
                        elif matrixtotal[j][i] >=qPadrao:
                            viajem2 += 1
                            matrixtotal[j][i] -=qPadrao
                        else:
                            break
                    resultado.append(f'  Trocas entre {i+1}({viajem1}v) e {j+1}({viajem2}v)')
                else:
                    contador +=1
                if contador == empresas*empresas:
                    resultado.append('  Sem Trocas')
    for i in resultado:
        print(i)
main()

