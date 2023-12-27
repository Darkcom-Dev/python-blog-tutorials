myArray = [5,4,1,0,0,6,2,0,4,5,2,0,9,8,7,6]

def get_separated_num(myArray):

    num_string = ''.join(str(num) for num in myArray)
    num_string = num_string.replace('0', ' ')
    num_string = num_string.replace('  ', 'X')

    return num_string.split()

def get_str_sorted(lista):

    lista_string = []
    for item in lista:

        #print(type(item), item)
        if type(item) == str:
            
            lista_numeros = list(item)
            lista_numeros.sort()
            lista_string.append(''.join(lista_numeros))
        else:
            for i in range(len(item)):
                lista_string.append(item[i])
                if i < len(item) - 1:
                    lista_string.append('X')
            
    return lista_string


lista = get_separated_num(myArray)

for i in range(len(lista)):
    if 'X' in lista[i]:
        lista[i] = get_str_sorted(lista[i].split('X'))


lista = ' '.join(get_str_sorted(lista))
print(lista)





