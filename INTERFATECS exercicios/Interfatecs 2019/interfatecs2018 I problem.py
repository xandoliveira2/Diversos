"""def main(): #problema I
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
		if len(listaimpar) % 2 == 1:
			print("VERDADEIRO")
		else:
			print("FALSO")

main()"""



numeros_testados = [False] * 100000
primos = []

def ePrimo(numero):
  numeros_testados[numero-1] = True

  if numero == 1: 
    return False

  if numero == 2:
    return True

  for primo in primos:
    if numero % primo == 0:
      return False

  return True

n = int(input())
for caso in range(1, n+1):
  num_digitos = [0] * 10
  intervalo = input().split(' ')
  inicio = int(intervalo[0])
  fim    = int(intervalo[1])

  for numero in range(inicio, fim+1):
    if not numeros_testados[numero-1]:
      if ePrimo(numero):
        primos.append(numero)

  for primo in primos:
    primo_str = str(primo)
    for i in range(0, 9+1):
      ocorrencias = primo_str.count(str(i))
      num_digitos[i] += ocorrencias

  print(f"INTERVALO {caso}")
  for digito in range(0, 9+1):
    print(f"{digito}: {num_digitos[digito]}")