#Dada dos listas (lista1 y lista2), de como resultado dos listas resultantes, una de la suma entre lista1 y lista2, y otra de la resta.

a = int(input("Ingrese la cantidad de elementos de la lista 1: "))
b = int(input("Ingrese la cantidad de elementos de la lista 2: "))

lista1 = []
lista2 = []
suma = 0
suma_lista1 = 0
suma_lista2 = 0

for i in range(1, a + 1):
  elemento_lista1 = int(input(f"Ingrese el valor del elemento {i} para la lista 1: "))
  if i != 0:
    lista1.append(elemento_lista1)
for e in range(1, b + 1):
  elemento_lista2 = int(input(f"Ingrese el valor del elemento {e} para la lista 2: "))
  if e != 0:
    lista2.append(elemento_lista2)
for i in lista1:
  suma = suma + i
  suma_lista1 = suma_lista1 + i
for e in lista2:
  suma = suma + e
  suma_lista2 = suma_lista2 + e

resta = suma_lista1 - suma_lista2

print(f"Los valores de la lista 1 son {lista1}")
print(f"Los valores de la lista 2 son {lista2}")
print(f"La suma de las dos listas es {suma}")
print(f"La resta de las dos listas es {resta}")