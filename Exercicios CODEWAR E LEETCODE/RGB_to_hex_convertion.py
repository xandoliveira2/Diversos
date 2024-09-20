# take an integer number and convert it to hexadecimal
# obs: over 255 turns FF and under 0 turns 00
def convertion(number):
        values = {
            10 : 'A',
            11 : 'B',
            12 : 'C',
            13 : 'D',
            14 : 'E',
            15 : 'F',
        }
        if number <= 0:
            return '00'
        elif number >= 255:
            return 'FF'
        elif number <10:
            return f'0{number}'
        else:   
            try:
                first_number =  values[number//16]
            except:
                first_number = str(number//16)
            try :
                second_number = values[number%16]
            except:
                second_number = str(number%16)
            return first_number + second_number
def rgb(r, g, b):
    r = convertion(r)
    g = convertion(g)
    b = convertion(b)
    return f'{r}{g}{b}'

