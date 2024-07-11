def main(): #problema I
	palavra = input().upper().strip().replace(' ','')
	listapalavra = list(palavra)
	medidor = len(palavra)
	listapares = []
	listaimpar = []
	contador = 0
	while contador < medidor:
		if listapalavra.count(listapalavra[contador]) % 2 == 1:
			listaimpar.append(listapalavra[contador])
			contador+=1
		else:
			listapares.append(listapalavra[contador])
			contador+=1
	if medidor % 2 == 0:
		if len(listaimpar) != 0:
			print("FALSO")
		else:
			print("VERDADEIRO")
	else:
		if len(listaimpar)  == 1:
			print("VERDADEIRO")
		else:
			print("FALSO")

main()