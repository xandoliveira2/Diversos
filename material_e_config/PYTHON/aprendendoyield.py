#1°obs> iterador e generator parece ter a mesma função em python 
# para que serve yield:
# para evitar armazenar grandes quantidades de dados na memória, não é meu caso ainda mas é bom aprender
# então vamos supor que eu vá abrir um arquivo com 1.000.000 de dados, armazenar esses 1.000.000 de dados em uma lista na memória do python pode não ser possivel
# então é ai que entra o yield
#####OBS >> código aqui meramente ilustrativo, não irei rodar ele porém vou deixar comentado cada linha de código

def ler_muitos_dados(diretorio_do_arquivo):
    for linha in open(diretorio_do_arquivo,'r'): # para cada linha dentro do seu arquivo ('importante que o arquivo tenha varias linhas')
        yield linha # yield (tradução livre = coleta) vai coletar dados por vez
    #o que o yield faz basicamente é ao invés de criar uma lista com todos os itens, (parte tecnica a partir de agora é achismo) ele pega apenas o primeiro e bota um ponteiro no próximo, algo como uma
    # lista encadeada talvez, onde cada lista só tem 1 elemento e está em formato de lista p poder iterar? fazendo esse processo ao invés dele ter que armazenar 1.000.000 de dados na memoria ele apenas
    # armazena 1 dado, 1 ponteiro e uma estrutura para fazer esse código executar
    # a função iter parece fazer a mesma coisa, porém eu creio que não faz muita lógica que você use o iter em uma lista já armazenada (a não ser que você vá remover essa lista eventualmente p liberar
    #espaço)
    # você pode usar a função next() para 'iterar' sobre cada item de um generator, porém ao meu ver parece que for faz mais sentido, a não ser q você queira comparar alguma coisa muito especifico mas 
    # é bom deixar anotado
    ##OBS 3 > iterator ele vai jogar onde ele já passou fora, então eu não consigo percorrer todos os itens duas vezes por exemplo com o mesmo iterador, uma lista simplesmente encadeada talvez?
    ##OBS 4 > você pode criar condições para coleta de um dado, porém caso você queira percorrer todos os itens com iterator onde não vai haver condicional, você pode simplesmente usar o comando:
    ## yield from lista
    # nesse caso como é um arquivo, a gente pdoeria colocar open direto nele:
    ## yield from open(diretorio_do_arquivo,'r')
    ...

## créditos > https://www.youtube.com/watch?v=2wUuWcfK--8