from colorama import Fore, Back, Style

print(Back.GREEN + Fore.BLUE + 'Hola, Bienvenidos')

print(Fore.RED + Back.BLUE +'==============================')

print(Fore.RED + Back.GREEN)

h = input("Ingresa Tu Nombre:")

print(Fore.RED + Back.BLUE +'==============================')

u = int(input("Ingresa Tu Edad:"))

print(Fore.RED + Back.BLUE +'==============================')

print(Fore.RED + Back.GREEN)

if u > 12:
	print("Su edad Es Pasable")
else:
	print("Su edad no es permitida")
	
print(Fore.RED + Back.BLUE +'==============================')

print("Programa Iniciado")

print("\/Puedes sumar aqui\/")

p = int(input("Ingresa tu primer numero:"))

print("Perfecto")

o = int(input("Ingresa tu segundo numero"))

print("perfecto has terminado")

t = (p+o)

print('Tu resultado es:', + t)