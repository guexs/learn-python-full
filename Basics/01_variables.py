# Variables

#forma incorrecta
MyVariable = 'Algo Interesante'
print(MyVariable)

#formas correctas
myvariable = "Algo super interesante como Python"
print(myvariable)

my_super_variable = 'Algo que tambien es super interesante'
print(my_super_variable)

#malas pracitcas
"""
"""

my_int_variable = 5
print(my_int_variable)

my_bool_variable = True
print(my_bool_variable)

#Concatenacion de variables
my_name = 'Santiago Guex'
print('Hello ', my_name, '!')
print(my_int_variable, my_bool_variable, myvariable)

#str()
print(my_int_variable, type(my_int_variable))
my_int_to_string = str(my_int_variable)
print(my_int_to_string, type(my_int_to_string))


#int()
string = "12"
my_str_to_int = int(string) 
print(my_str_to_int, type(my_str_to_int))

#len()
my_surname = 'Guex' #ojo con los espacios
print('Surname: ', my_surname)
print('Surname length: ', len(my_surname))

#type() al print() = <class 'NoneType'>
my_print = type(print('Hola amigo'))
#print(my_print)

print('Este es el valor de: ', my_bool_variable)

#Variables en una sola linea
num1, num2, num3, num4, num5, num6, num7, num8, num9, num10 = float(1), 2, [1, 2, 3], 4, 5, 6, 7, 8, 9, 10
print(num1)
print(num2)
print(num3)
print(num4)
print(num5)
print(num6)
print(num7)
print(num8)
print(num9)
print(num10)

#Input - input()
"""
first_name = input('Como te llamas: ')
age = input('Tu edad: ')

print(first_name)
print(age)
"""

#¿Forzamos el tipo?
adress: str = "Mi direccion"
adress: int = 32
print(type(adress))