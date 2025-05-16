insert = """
nome, idade, cidade
"""
parametros = """
:nome, :idade, :cidade <-
"""
insert = insert.split(',')
parametros = parametros.split(',')

for i in range(len(insert)):
    if '<-' in parametros[i]:
        print(insert[i])
        break
