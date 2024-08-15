#teste coment
print("ue")
print('ue2')
print('ok, não precisa de ponto e virgula')
print("Talvez identação?")
numero = 4
print(numero)
if (numero > 5) {
    print('oi')
}else{ # tomar cuidado com uso de else, ele só pode ser aceito logo após o fechamento } de if, ou seja, se eu quebrasse uma linha antes vai surgir erro
    print('sem oi p você')
}
# nome <- readline(prompt = "Digite seu nome: ")
# print(nome)
#4 formas de declarar variavel:
variavel1 = "nome A"
variavel2 <- "nome B"
"nome C" -> variavel3
variavel4 <- variavel1 # esse aqui praticamente está criando uma cópia do nome 1
print(variavel1)
print(variavel2)
print(variavel3)
print(variavel4)
vari = c(variavel1,variavel2,variavel3,variavel4)
?str_c #nao existe ainda
#baixar em: www.rdocumentation.org
?summary
# install.packages("stringr")
print(vari)
# oi = str_c(variavel1,variavel2)
# print(oi)
library(stringr) #-> carrega o 'package' para usar, é praticamente usar o import em python, porém ela só precisa ser carregada uma vez por terminal

oi1 = str_c(variavel1,variavel2)
.variaveltmb <- 'sopade monkey'
print(.variaveltmb)
print(oi1)
num <- 10
flt <- 10.53
lnh <- 'linha'

print(typeof(num)) # -> double
print(typeof(flt)) # -> double
print(typeof(lnh)) # -> character
print(class(num))  # -> numeric
print(class(flt))  # -> numeric
print(class(lnh))  # -> character
inteiro = 0
i = 10
comp <- 3+2i
print(class(comp)) # -> complex (obs: mas oque diabos é um complex? preciso pesquisar na matematica)
  
###### DIFERENTES TIPOS DE DADOS ##########
x <- 100  #-> isso vai ser lido como um double
#para vermos ele inteiro temos q colocar o L no final
print(typeof(x)) # -> double
y <- 100L #-> isso faz ele reconhecer como um inteiro e não um double
print(typeof(y)) # -> integer

#existem tipos de dados 'complex' (até em python existe) e 'raw' (acho q só em R? porém fica a dúvida doque é esse tipo de arquivo 'cru'?)

#### OPERADORES LOGICOS #####
#nada de novo eu diria
print(10<20) # -> true
print(10>20) # -> false
print(10>20 || 20>10) # -> true  ( || como or )
print(10>5 && 5 > 7) # -> false ( && como and )
print(!10<5) # -> true

#### OPERADORES ARITMETICOS ####
#conhecidos e que permanecem iguais:
print(100 + 100)
print(100 - 100)
print(100 * 100)
print(100 / 100)
print(10**5) # -> fica com notação cientifica '1e+05'
print(10^5) # -> funciona da mesma maneira
print(10*(2+3)) #-> executa porcentagem primeiro tmb
#diferente
print(100%%2) # -> usa dois sinais de porcentagem

# linha <- read.csv("C:\\Users\\User\\Desktop\\testedados.csv")
print(linha)
váriavel <- "sopa de monkey brother"
print(váriavel)



