README sobre o arquivo exunix.py
-----------------------DOCUMENTAÇÂO-----------------------------


FUNÇÕES
bissexto(ano) #linhas 4 à 7#-> apenas retorna se aquele ano é bissexto ou não
unixtime(data,horario,UTC) #linhas 10 à 37-> retorna o unix time baseando na sua data atual, horario atual e UTC local onde:

OBS: codigo converte o tempo para dias totais, multiplica segundos por dia * dias e soma com segundos de horas:minutos:segundos 

linha 11 : dicionario com numero do mes e seus respectivos dias que são diferentes de 31 (#explicação: existem maior numero de meses com 31 dias, então considerar 31 padrão e tudo além disso botar em um dicionário de 'excessões')
linha 12 : variavel reservada para segundos decorridos desde 1970
linha 14 : variavel reservada para dias decorridos desde 1970
linha 15 - 19 : loop responsavel por adicionar numeros de dias decorridos por ano antes do ano determinado pelo parametro data da função unixtime, ele faz comparação para adicionar 366 dias em anos bissextos e 365 em anos não bissextos
linha 20 - 26 : loop responsavel por adicionar numeros de dias decorridos por mês até o mês anterior determinado pelo parametro data da função unixtime, onde ele faz comparações como:
        21 & 22- se o mês é fevereiro e ele é bissexto -> aumenta 29 dias
        23 & 24- se ele estiver no dicionario (linha 11), pegue o valor de dias correspondentes ao mês
        25 & 26- caso contrário adicione 31
linha 27 : adicionamos aos dias totais, os dias passados no mês, e removemos 1 pois o dia atual ainda não passou, ele está em andamento e é onde começa, às meia-noites (00:00)
linha 28 : variavel de segundos (linha 12) desde a data estipulada, até essa linha do código ele sempre retornará valor unix time do dia especificado na função as 00💯
linha 30 - 36 : loop responsável por somar segundos passados da 00:00 do dia atual até o horário atual onde:
        linha 31 & 32 : ??
