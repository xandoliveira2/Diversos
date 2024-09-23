""" VERSION ONE - ALMOST THERE"""
def card_game(n):
    # NOT AVAILABLE TO "PERFORMACE RANDOM TESTS"
    alice_points = 0
    for i in range(100000):
        if n <= 0:
            break
        if n % 2 == 1:  
            alice_points+=1
            n-=1
            if n/2 == 2:
                alice_points+=1
                break
            elif (n/2)%2==0:
                n = n -1
            else:
                n = (n/2)
       
        else:
            if n/2 == 2:
                alice_points+=3
                break
            elif (n/2) % 2 == 0:
                alice_points+=1
                n = n - 2
            else:
                alice_points+=int(n/2)
                n =(n/2)-1

    return alice_points
import sys
sys.set_int_max_str_digits(1000000)
import math
def zeros(n:int):
    a = str(math.factorial(n))
    contador = 0
    for i in a[::-1]:
        if i == '0':
            contador+=1
        else:
            break
    return contador

