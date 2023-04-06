#Operadores

#Aritméticos:
my_float = 2.5 * 2

my_int_to_int = int(my_float)


print(3 + 4)
print(3 - 4)
print(3 * 4)
print(3 / 4)
print(10 % 3) #modulo 1 - resto de una division
print(10 // 3)# floor division - acerca el resultado a un numero entero
print(2 ** 3 + 3 - 7 / 1 // 4) # potenciacion

print("Hola " + "Python" + " Que tal?")
print("Hola" + str(5))
print("Hola" * 5)
print("Hola" * my_int_to_int)
print("Hola" * (2 ** 3))

#Operadores Comparativos:

print(3 > 4)
print(3 < 4)
print(3 >= 4)
print(3 <= 4)
print(4 == 4)
print(3 != 4)
print(3 != 4)
print(3 > 4 == 2)


print("Hola" > "Python")
print("Hola" < "Python")
print("aaaa" >= "AAAA") # Ordenación alfabetica por ASCII
print(len("aaaa") >= len("aaaa")) # Cuenta caracteres
print("Hola" <= "Python")
print("Hola" == "Hola")
print("Hola" != "Python")

#Operadores Lógicos:

print('Operadores Lógicos')

print(3 > 4 and "Hola" > "Python")
print(3 < 4 or "Hola" > "Python")
print(3 < 4 and "Hola" < "Python")
print(3 < 4 or "Hola" > "Python" and( 4 == 4))
print(not(3 < 4))