#%%writefile typeTest.py
import typing #import Undefined
from collections import namedtuple

integer : int = 22 #int
string : str = "stringer"
float_number : float = 1.83
boolean : bool = False

anyValue : any = None

# Utilice la NewType()función auxiliar para crear tipos distintos:
UserId = typing.NewType('UserId', int)
some_id = UserId(524313)

print(boolean.to_bytes(10,'little'))

#Aqui hay conflicto en las palabras reservadas List y Tuple
# Las listas son mutables y tienen indices, permiten valores repetidos
new_list : list() = [10,20,30,10,5]
# Las tuplas NO son mutable y tienen indices, permiten valores repetidos
new_tuple : tuple() = (10,20,30,10,5)
# Los diccionarios son mutables, no tienen indices pero si llaves y no permite llaves repetidas
new_dict : dict() = {"mat":10, "prog":10, "ingles":5}
# Los sets NO son mutables, no permite llaves repetidas y no guardan un indice, pudiendo aparecer en cualquier orden.
new_set : set() = {'Venus','Marte','Tierra'}

Vector = list()

Color = namedtuple('Color',['R','G','B','A'])
print(Color)
c1 = Color(255,255,255,255)
print(type(int))


#-----------------------------------------
# Operador ternario en Python

# if condicion:
#	print("verdadero")
# else:
#	print("falso")
condicion = True
print("verdadero") if condicion else print("falso")
# Solo sirve para una instruccion y no hay elif
# El siguiente es un ejemplo asignando un valor
valor = "verdadero" if condicion else "falso"
print(f'el valor es: {valor}')

# Simplicando valores para saber si un numero está dentro de un rango
# Veremos si la edad esta entre 0 y 10
# edad = 5
# if edad >= 0 and edad <= 10: hagaAlgo
edad = 5
if 0 <= edad <= 10: print(f'La edad esta dentro del rango')


def scale(scalar: float, vector: Vector) -> Vector:
        """
        Escriba alias 
        Un alias de tipo se define asignando el tipo al alias.
        En este ejemplo, Vectory list[float]
        se tratarán como sinónimos intercambiables:
        """
        return [scalar * num for num in vector]

# typechecks; a list of floats qualifies as a Vector.


def greeting(name: str) -> str:
        '''
        En la función greeting,
        name se espera que el argumento sea ​​de tipo str
        y el tipo de retorno str.
        Los subtipos se aceptan como argumentos.
        '''
        return 'Hello ' + name

#en funciones
def suma(sumando_a : int, sumando_b : int) -> int:#-> Es el retorno
        '''
        Suma dos terminos
        Parameters
        ----
        sumando_a : int
                primer termino de la suma
        sumando_b : int
                segundo termino de la suma
        Returns
        ----
        result : int
                resultado de la suma
        '''
        return sumando_a + sumando_b

# Asi como en como funciones y metodos son lo mismo, argumentos y parametros es lo mismo, solo cambia el contexto
# Funcion cuando está fuera de una clase y metodo cuando esta dentro.
# Parametro son los nombres de variables definidos en la funcion, argumentos son sus valores
# Si no conocemos la cantidad de parametros, podemos anteponer un * al nombre del parametro
def saludando_a_todos(*nombres:tuple) -> None: #por defecto en Python seria *args
	for nombre in nombres:
		print(f'Buenos dias {nombre}!')

def imprimiendo_diccionario(**kwargs) -> None:
	for key, value in kwargs.items():
		print(f'Llave: {key}, Valor: {value}')

def cuenta_regresiva_recursiva(numero : int) -> None:
	if numero == 1:
		print(numero)
	else:
		print(numero)
		cuenta_regresiva_recursiva(numero-1)

def calcular_total(pago_sin_impuesto,impuesto):
	impuesto_neto = pago_sin_impuesto * (impuesto / 100)
	return pago_sin_impuesto + impuesto_neto

calcular_total(1000,16)

def celsius_fahrenheit(celsius):
	return 1.8 * celcius + 32
	
def fahrenheit_celsius(fahrenheit):
	return 0.5555 * fahrenheit - 32

sumatoria = suma(23,45)
cuenta_regresiva_recursiva(5)
new_vector = scale(2.0, [1.0, -4.2, 5.4])
saludando_a_todos('Pedro','Pablo','Jacinto','Jose')
imprimiendo_diccionario(IDE= 'Integrated Development Enviroment',DBMS= 'Database Managment System')# Ojo con esta manera de enviar argumentos
cuenta_regresiva_recursiva(5)
