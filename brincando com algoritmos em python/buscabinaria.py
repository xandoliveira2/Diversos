#busca binaria
import random
def gerarlistaorganizada(): 
    minhalista = [random.randint(1,100000) for i in range(0,99)]
    meunovoespaco = list('-'*len(minhalista))# 1° passo: criar uma lista com o tanto de items que vai ser analisado para reservar um espaço na memoria
    # para o tanto de itens que eu vou ter que colocar organizado nessa string, pois se eu nao fizer isso, não vou conseguir adicionar itens na lista, pois por exemplo
    # se eu so declarar o espaço da lista, como eu adiciono um item na posição 6 (por exemplo) em uma lista que nem itens tem? não teria como, então eu preciso ja 
    # preencher esses espaços
    limite = len(meunovoespaco)
    # 2° passo: identificando qual número é maior doque quanto outros números para sabermos dele a posiçao na lista
    #essa primeira etapa é apenas para 
    for i in minhalista:
        cont = 0
        for j in minhalista:
            if i > j:
                cont += 1 # cada vez que rodar esse loop e comparar que ele é maior que outro, vai aumentar a posição dele na lista, onde, quanto maior o número
                #que ele acumular aqui, representa que ele é o 'cont' número maior de toda minha lista
            else:
                pass
        meunovoespaco.insert(cont,i) #aqui é o 3° passo logo após o segundo, o qual estou colocando ele na minha nova lista preenchida com "-" na posição que
        #consta a variavel cont
        valocal=1 # essa variavel vai servir apenas para identificarmos o proximo item de '-' para removermos eventualmente, é essencial declararmos que o valor
        #dela aqui será 1, pois estaremos eventualmente analisando qual o próximo item na lista é um '-' para removermos, constando que, para cada item que eu
        #insiro no passo 3, preciso remover um '-' que serve apenas para reservar o local que esse número ficara, ou seja, em uma atribuicao mais simples é como 
        # se eu fosse retirar um prato de aperitivo para colocar o almoço
        while True: # 4° passo: esse loop ele vai acontecer até que encontre o próximo item '-' na lista
            for i in meunovoespaco: #então vamos começar percorrendo minha lista
                #OBS DO FUTURO: tinha uma linha de código aqui que era inutil, olha as vantagens de ir passar a limpo depois 
     
                    if meunovoespaco[cont+valocal] == '-': # meu cont está ainda armazenado do 2° passo, pois ainda estamos na sequencia do primeiro for loop
                        #entao aqui eu a primeira instancia estou acessando diretamente o proximo espaço da minha lista e perguntando se é igual a '-',e se
                        # caso for:
                        meunovoespaco.pop(cont+valocal) # vai ser removido
                        break
                    else:#senão
                        valocal +=1#vai ir aumentando até achar o proximo item que seja, pois se um foi adicionado e empurrou outro numero para frente (que é oque
                        #acontece com o insert) nem sempre o nosso proximo item vai ser uma '-', entao aqui estou procurando o proximo item que representa a 
                        # variavel que serve apenas para guardar espaço (que no caso é o '-')
            break #ok, encerro o 4° passo que é minha primeira etapa ainda
    #pronto, realizado aqui, comeca a dar um problema quando aparece itens repetidos (se for um range muito grande de items é dificil acontecer esse problema, porém
    #quanto menos items tiver no range {ou seja, quanto mais repetidos tiver} maiores serão a quantidade de dados errada na lista} que é aparecer '-' a mais, ou seja
    # no meu exemplo, os 100 items são criados, porém conforme repete os números as vezes acaba passando '-' que estejam antes do numero repetido colocado, e meu 
    #codigo não faz a correção para trás, então para corrigir isso vamos aumentar um pouco o código para a 5° etapa:
    while True: #esse pequeno while loop vai apenas fazer a correcao do problema acima, como eu já tratei todos os numeros em sequencia, agora só basta tirar os '-'
        #que sobraram pois os items ja estão alinhados, porém queremos tirar todo espaço reservado anteriormente
        # então o 1° passo da 2° etapa é: 
        if limite == len(meunovoespaco): #verificar se houve erro, como eu faço isso? lendo o tamanho da minha lista, foi criado 100 items, então tudo que for acima
            #desse número, é um erro, no caso do codigo está perguntando se for igual, se for igual
            break # apenas encerre pois não precisara ser feito nada
        else: #se nao for igual
            meunovoespaco.remove('-') # basta remover os '-' que sobraram,
            #nao tem break, então assim que ele executar isso vai voltar no comeco do loop e se perguntar denovo, então vamos supor que tenhamos em um primeiro teste
    #102 items, vai entrar no else, e vai remover 1 dado de: '-', o len agora vai ser 101, que nao vai se encaixar denovo no primeiro if e cair no else que vai remover
    #mais 1, que ao voltar pela 3° vez no loop vai cair pois vai estar 100 = 100
    return meunovoespaco # depois de corrigir quaisquer dados com erros, finaliza a funcao me devolvendo a lista criada de números sortidos do range especificado
    # nas primeiras linhas (que nesse caso é 100 items que variam de numeros inteiros de 1 a 100


#bom, fiz algo que me cria uma lista com 100 numeros aleatorios entre 1 e 100, porém isso é para praticar com busca binária
lst = gerarlistaorganizada()# então aqui vou criar uma variavel para armazenar essa minha primeira lista aleatoria

print(lst) # aqui eu exibo ela apenas para ir conferindo visualmente, não existe uma real necessidade de imprimir, é apenas para me ajudar visualmente para q eu confira
#os dados pessoalmente nos testes

def buscabinaria(item:list,busca:int): # aqui vou começar a funcao de busca binaria que praticamente é procurar em lista muito grande sem ter que percorrer todos
    #items, pois imagine que a lista seja IMENSA, gastaria muita memoria percorrer tudo um por um, a busca binaria em sí é pesquisando na lista por exemplo, o meio
    # da lista, se o numero q a gente tiver procurando for maior que o do meio, então nosso numero se tiver vai estar na segunda parte (OBS: importante que a lista
    # esteja ordenada)
    
    var = list() # bom, começo primeiramente declarando uma variavel do tipo list para que possamos armazenar a lista que nos passaram de parametro para fazer
    #uma verificação se tá organizada
    var = item.copy()  # aqui eu copio a lista nessa variavel
    var.sort() # aqui eu uso um metodo pronto do python para organizar nessa nova lista (eu poderia ter aproveitado parte do meu codigo acima para servir como 
    #metodo, porém como ele cria uma lista e organiza, eu nao posso usar aqui, se ele so organizasse eu poderia usar ele)
    if item != var: # aqui eu apenas faço a comparacao do item que ele me passou bruto com o item que eu organizei, se eles forem diferentes
        raise "Erro! A lista precisa estar ordenada" # vai exibir erro e explicando o motivo do erro
    else: # se forem iguais, então ele vai prosseguir para a busca
        lefti=0 # onde lefti é meu index da esquerda
        righti= len(item)-1 #meu righti é meu index da direita, como sabemos uma lista comeca no index 0, então para definir o index da direita a gente tem que 
        #subtrair um do total de items que a lista tem
        meioi= len(item) // 2 # e meu meioi é meu index do meio, que em primeira instancia vai ser o tamanho da minha lista e divisão inteira por 2

        contador = 0
        while True:
            contador+=1
            if int(item[meioi]) == busca:

                return meioi
            elif int(item[meioi])  > busca:
                righti = meioi 


            elif int(item[meioi])  < busca:

                lefti = meioi 

            elif int(item[meioi]-1==busca):

                return meioi - 1
            elif int(item[meioi]+1==busca):

                return meioi + 1
            
            meioi = (righti + lefti) // 2
            if contador == 20:
                return None
                          





print(buscabinaria(lst,70))

