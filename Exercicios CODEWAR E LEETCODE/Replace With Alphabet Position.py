def alphabet_position(text):
    text = text.lower()
    import string
    frase = string.ascii_lowercase
    retornar = []
    for i in text:
        for j in range(len(frase)):
            if frase[j] == i:
                retornar.append(j+1)
    retornar = map(str,retornar)
    return ' '.join(retornar)
    
