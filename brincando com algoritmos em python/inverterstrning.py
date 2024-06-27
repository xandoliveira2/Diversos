#objetivo: inverter uma string e verificar se é um palindromo (obs: não existe um controle muito bom nesse codigo, então funciona apenas se todas letras forem 
# inteiramente de um certo tipo (maiuscula ou minuscula) e que não haja acentos como ç, ~, ´...)
def inverter(texto:str): # funcao inverter recebe de parametro uma variavel do tipo string
    lst = texto.strip().split(' ') # eu retiro espaços vazios usando .strip() e depois separo as palavras por espaço em uma lista que eu declarei o nome de lst
    texto = ''.join(lst) #dps minha variavel texto vai ser uma string apenas para conjunção das palavras, ou seja, vamos supor 'academia de girafa', vai ficar 
    #dps do split como ['academia','de','girafa'], e apois o join eles vai se juntar tudo ficando academiadegirafa
    palin = list('-'*len(texto)) # aqui eu uso o mesmo conceito de organizar uma lista com números inteiros, eu crio a variavel palin que vai receber o tanto de
    #numeros q minha palavra possui, então academiadegirafa tem 16 caracteres, então vou ter uma lista com 16 elementos '-' que eu boto apenas para reservar o espaco
    num = len(texto) - 1 # aqui vai ser o responsavel por lançar do ultimo index ao primeiro para inveter a palavra ou seja, num == meu ultimo index
    for i in texto: #entao aqui estou falando para cada letra em texto
        palin.insert(num,i) # na minha lista reservada, eu vou adicionar a primeira letra no ultimo espaço
        # quando acontece o insert na minha lista preenchida com '-', o meu 'item' entra no index daquele '-' e empurra ele para o proximo index
        palin.pop(num+1) # então eu posso remove-lô diretamente assim depois de cada comando
        num-=1 # e aqui declaro p ele ir dimunuindo o index gradualmente 
    var = ''.join(palin) #e finalizo montando minha string invertida que declarei o nome de variavel var
    return var #funcao inverter me devolve essa string invertida

def main(texto:str): # esse main é apenas o comparador
    var = texto.strip().split(' ')# ou seja, ele vai fazer o mesmo processo, vai remover espaços em branco a direita e a esquerda com o strip() e logo apos vai
    #separar em uma lista
    texto = ''.join(var) # vou concatenar os itens dessa lista 
    if texto == inverter(texto): # depois vou comparar com o mesmo texto porém invertido, e caso seja igual
        return 'palindromo' # volta que é um palindromo
    else: #caso contrario
        return 'não palindromo' #não é
print(main('subi no onibus')) # repare que como eu dei return, para que seja exibido na tela preciso de um print, poderiamos trocar da linha 22 até a 25 por isso tmb:
    #if texto == inverter(texto): 
        #print('palindromo')
    #else: #caso contrario
        #print('não palindromo')
#main('subi no onibus) <- sem o print
