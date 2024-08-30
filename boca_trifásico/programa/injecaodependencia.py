import sys #será usado o exit para encerrar o programa e não afetar meu o122


def increase_list(dictionary:dict,key_element:str|int,increment_argument:str|int) -> None:
    local_returnable_list = *dictionary[key_element],increment_argument
    dictionary[key_element] = local_returnable_list
    
def increase_empty_values(dictionary:dict,used_letters:list):
    for letter in used_letters:
        try:
            if dictionary[letter]:
                pass
        except KeyError:
            dictionary[letter] = tuple()
def verify_letters(letter_list:list,argument:list):
    for letter in argument:
        if letter not in letter_list:
            letter_list.append(letter)
def verify_all_dependencies(dictionary:dict):
    for keys in dictionary:
        if dictionary[keys] == tuple():
            return True
    # print("usar injecao tardia")
    return "usar injecao tardia"
    
def main_verification(dictionary:dict):

    for keys in dictionary:
 
        for values in dictionary[keys]:
           
            value_key_index = 0
            
            while True:

                try:
                    if dictionary[values][value_key_index] == keys:
                        # print('usar injecao tardia')
                        return 'usar injecao tardia'

                except IndexError:
                    break
                value_key_index+=1
            
    # print('ok')
    return 'ok'
dictonary_master = dict()
loops = int(input())
letters = []
for i in range(loops):
    dependencies = input().split(' ')
    verify_letters(letters,dependencies)
    try:
        if dictonary_master[dependencies[0]]:
            increase_list(dictonary_master,dependencies[0],dependencies[1])

    except KeyError:
        dictonary_master[dependencies[0]] = (dependencies[1])
increase_empty_values(dictonary_master,letters)

if verify_all_dependencies(dictonary_master) != True:
    print(verify_all_dependencies(dictonary_master))
else:
    print(main_verification(dictonary_master))

