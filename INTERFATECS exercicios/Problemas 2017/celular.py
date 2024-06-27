def main():
    dicionario = {
        'a':1,
        'b':2,
        'c':3,
        'd':1,
        'e':2,
        'f':3,        
        'g':1,
        'h':2,
        'i':3,
        'j':1,
        'k':2,
        'l':3,
        'm':1,
        'n':2,
        'o':3,
        'p':1,
        'q':2,
        'r':3,
        's':4,
        't':1,
        'u':2,
        'v':3,
        'w':1,
        'x':2,
        'y':3,
        'z':4,


        'A':4,
        'B':5,
        'C':6,
        'D':4,
        'E':5,
        'F':6,        
        'G':4,
        'H':5,
        'I':6,
        'J':4,
        'K':5,
        'L':6,
        'M':4,
        'N':5,
        'O':6,
        'P':5,
        'Q':6,
        'R':7,
        'S':8,
        'T':4,
        'U':5,
        'V':6,
        'W':5,
        'X':6,
        'Y':7,
        'Z':8,
        '#':1,
        '*':1,
        '+':2,
        ' ':1,
                }
    palavra = input()
    resultado = 0
    for i in palavra:
        resultado+=dicionario.get(i)

    print(resultado)



main()