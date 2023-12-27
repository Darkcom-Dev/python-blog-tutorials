
n=5

def get_renglon(pares, impares, rango):
    renglon = []
    for i in rango:
        if i%2 ==0:
            renglon.append(pares)
        else:
            renglon.append(impares)
    
    return ''.join(renglon)

def get_page(_rango):
    for j in _rango:
        if j%2 == 0:
            print(get_renglon('X', '_', _rango))
        else:
            print(get_renglon('_', 'X', _rango))

if n<=10 and n>0:
    get_page(range(1,n+1))
elif n < 1:
    print("error")
else:
    get_page(range(1,6))



    





