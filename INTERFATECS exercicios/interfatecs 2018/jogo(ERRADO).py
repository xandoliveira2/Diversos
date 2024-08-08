def main():
	lista = []
	contador = 0
	letra = ''
	letras= ''
	while True:
		entrada = input()
		if contador !=1:
			letras += entrada[0:3]
			contador = 1
		if entrada == '':
			break
		else:
			lista.append(list(entrada))
	letras = list(letras)
	if letras.count(letras[0]) == 1:
		letra = letras[1]
	else:
		letra = letras[0]
	for i in range(0,len(lista)):
		for j in range(0,len(lista[0])):
			if lista[i][j] != letra:
				print(f'LINHA {i+1} COLUNA {j+1}')
				quit()
		



main()