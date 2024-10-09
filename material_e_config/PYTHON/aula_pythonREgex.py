# print(f'f strings aqui e '+r'r strings aqui dão \c\e\r\t\o\?','e juntando ainda de duas maneiras?')  #teste, ignore
import re
palavra = "sopa de macaco"
# . - Entende qualquer valor exceto nova linha
# \. - para buscar o caractere '.'

padrao = re.compile('sop. de ..caco') # -> onde . pode significar qualquer caractere (exceto nova linha) onde eu quero encontrar o padrao 'sop. de ..caco' onde '.' representa
#"QUALQUER CARACTERE EXCETO NOVA LINHA"
padrao1 = re.compile('sopa......caco')

check = padrao1.findall(palavra) # -> retorna uma lista com todas palavras correspondentes no 'padrao' declarado

print(check)

""" OBS> todos comandos findall() retorna uma lista"""

# ^ - irá testar o inicio da String
# [^] - irá considerar todos os caracteres EXCETO o indicado
palavra = 'sopa de macaco'
p = re.compile('^a') #-> (considerando linha->/// p = re.compile('^a')///  ) vai retornar se começar com a, então nesse caso comeca com s, vai voltar uma lista vazia [], porém se fosse a palavra 'areia' por exemplo retornaria 
#uma lista com a letra ['a'], a mesma coisa daria se fosse com parametro ('^are')
check = p.findall(palavra)
if check:
    print('comeca com a')
else:
    print('not a "a"')
print(check)
p2 = re.compile('[^sopa]') # -> retorna uma lista com todos caracteres sem o especificado, caractere por caractere
check = p2.findall(palavra)
print(check)

######### OBS 2 -> TODOS PARAMETROS QUE USAREM \ (contra-barra), DEVE-SE TER UM R MAIUSCULO OU minusculo PARA FINS DE EVITAR PROBLEMAS COM 'CHAVES RESERVADAS' COMO SERIA O CASO DO
######### \n POR EXEMPLO
######### TEORIA? usar duas contrabarras seria a solucao? \\n?
######### RESPOSTA? poderia sim resolver, só que dependendo de quantos parametros eu vá colocar vai ficar varias contra-barras, fazendo-se assim mais eficientemente escrever apenas
######### um r antes do inicio da string assim como em f-strings

# \d -> todos valores numericos
# \D -> todos valores NÂO númericos

palavra = 'sopa de macaco em 1995, 30 anos após...'
p = re.compile(r'\d') #-> retorna todos valores numericos
check = p.findall(palavra)
print(check)

p1=re.compile(r'\D') #-> retorna todos valores NÃO NUMÉRICOS 
check = p1.findall(palavra)
print(check)

######## OBS 3 -> perceba que há um padrão quando se usa contra-barras e letra que é: minusculas representam a existencia de tal condicao e maiusculas a falta de existencia de tal
######## condicao, como é o exemplo de por exemplo \r -> apenas os numericos, \R -> apenas os NÃO numéricos

# \s -> todos valores vazios
# \S -> todos valores NÂO vazios

texto = '''
vários
textos
com espaço?
i'm not sure
'''

p = re.compile(r'\s')
p1 = re.compile(r'\S')
check = p.findall(texto) #-> pega todos valores vazios, então:
#pega \n na linha 56 dps dos 3 apóstrofos, depois pega outro \n dps das palavras vários, textos, depois pega o espaço vazio de com' 'espaço?,\n no final da interrogação
# espaços de i'm" "not" "sure"\n"
check1 = p1.findall(texto) #-> retorna tudo que não seja vazio (letras,numeros,simbolos,pontuações,etc.)
print(check,'\n',check1)


# \w -> qualquer caractere que SEJA alfanumerico
# \W -> qualquer caractere que NÃO SEJA alfanumerico
palavra = 'sopa! de macac_o em #1995, 30 .;;/a-nos após...@'
p = re.compile(r'\w') #uma surpresa bem grande que _ seja alfanumerico ___> att: ele não é '-' kkk, isso é rolo do python provavelmente
p1 = re.compile(r'\W')
c = p.findall(palavra)
c1 = p1.findall(palavra)
print('\n \\w e \\W\n',c,'\n',c1)




#METODOS DE CHECAGEM
texto = 'sopa de 1macaco'
p1 = re.compile(r'a')
checkfindall = p1.findall(texto) #-> retorna uma lista com todas correspondencias do padrao
checkmatch = p1.match(texto) #-> retorna um objeto indicando de qual linha até qual ele encontrou com o padrão ##obs> do jeit que está apenas consegue dar 'match' no começo da string
#ou seja, não pega valores que não estejam no começo, deve haver alguma forma de 'adaptar' essa parte do código ou até mesmo usar outra função para isso...porém é indiferente se você
# pensar que isso pega apenas no começo, qual seria a diferença da função match para ^texto?
checksearch = p1.search(texto) #-> complementa o de cima, comentário estava correto, match pega apenas no comeco e search procura em qualquer lugar do texto
checkfinditer = p1.finditer(texto) #-> igual ao do search, porém ele retorna uma lista com todos matchs que deu, então por exemplo, com o comando ### p1 = re.compile(r'a') ###
# o search retorna 3,4 que foi onde ele encontrou o primeiro 'match', com finditer ele verifica todos que deram match, então com a deu no sopA de mAcAco, 3 match, finditer retorna
# a posição dos 3 encontrados
 
print('findall "a" =')
print(checkfindall)
print('match "a" =')
print(checkmatch)
print('search "a" =')
print(checksearch)
print('search.group "a" =')
print(checksearch.group())
print('finditer "a" =')
print(checkfinditer)
print('finditer após lista "a" =')

print(checkfinditer)


lc = []
print('checkfinditer em loop')
for i in checkfinditer:
    print(i)


palavra = """a0ZZZZZZZZZZZZZZZsopa de macaco de 1995, 30 anos após o ...
que destruiu o mundo chamado ...
'cara, para de fumar mano pqp'
"""

### [] ->character set -> grupo de caracteres -> entende que tudo dentro do [] é considerado uma coisa só


p = re.compile(r'[a-zA-Z0-9 ,.\'ó\n][0-9]') # cada conjunto de colchete [] representa uma possibilidade, então, se adicionarmos mais
# ###OBS 4 -> ele não volta para trás na comparação, então por exemplo, considerando o exemplo acima e a frase 'b7o0nde, j423s', se encaixaria nele as seguintes possibilidades:
# b7,o0,j4,42,23
# porém ele uma vez que passa pelo 4 no j4 por exemplo, ele 'descarta' ele na comparação, fazendo assim então sair :
# b7,o0,j4,23


check = p.findall(palavra)
check1 = p.match(palavra)
check2 = p.search(palavra)
check3 = p.finditer(palavra)
print(check)
print(check1)
print(check2)
contador = 0
for i in check3:
    print(i)



palavra = 'sopa de 200 reais de macaco kk'
padrao = re.compile(r'[a-z]+ [a-z]+ [0-9]+ [a-z]+ ') #-> o + significa que pode haver mais de uma letra entre essa palavra, ou seja, letras de a-z que se aparecem em uma ou mais vezes
c = padrao.finditer(palavra)
print(*c)



palavra = 'sopap dpe 200 reaispa de macaco kk'
padrao = re.compile(r'[pa]*') #-> o * representa 0 ou mais vezes aparecidas, ou seja, se tiver 'pa' nao aparecer nenhuma vez, retorna nada (''), se ele aparecer o p, ele retorna o p
#se aparecer o a, ele retorna so o a, se aparecer pa, ele retorna o pa, porem se encontrado pa uma vez, ele procurará no proximo item da string para ver se é pa tmb, entao
# por exemplo se '...compile(r'[pa]*')' na string 'bicho papão' ele verifica b não tem pa então retorna '', a mesma coisa acontece até chegar no pa, ele verifica que é pa e os proximos
# dois caracteres é pã, como ã não está no parametro, ele retorna pap desses indexes (nesse caso 7-10) e o proximo que ele vai verificar é o ã, que retornara '', o 'o' tmb e finaliza
##OBS> ele reconhece \n tmb como um caractere
c = padrao.finditer(palavra)
for i in c:
    print(i)



palavra = 'sopa de macaco'
padrao = re.compile(r'[aeiou]?') #-> ? = 1 ou 0 = sim ou não ---> retorna '' para todos que não estejam dentro do especificado, nesse caso se não for a,e,i,o ou u ele retornara ''
# caso contrario ele retorna a letra
c = padrao.finditer(palavra) 
for i in c:
    print(i)

palavra = 'sopa de mamaco'
padrao = re.compile(r'[ma]{3,4}') # -> {numero} -> quantidade exata de repeticoes, por exemplo, ter m ou a 3 vezes 
# com dois parametros como na linha 161 significa min e maximo respectivamente
c = padrao.finditer(palavra)
print(*c,sep='\n')

