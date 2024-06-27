def main(): #problema F
	vendas = int(input())
	listavalores = []
	for i in range(0,vendas):
		valores = input().split(' ')
		listavalores.append(float(valores[1])*int(valores[0]))
	valortotal = float()
	for i in listavalores:
		valortotal+=i
	# se necessario:
	#valortotal.replace(',','.')
	print(f"{valortotal:.2f}")
main()