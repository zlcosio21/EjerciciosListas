#Dada dos listas (lista1 y lista2), de como resultado la suma entre lista1 y lista2, y otra de la resta.

lista1 = []
lista2 = []
suma_listas = 0
resta_listas = 0

cant_lista1 = int(input("Ingrese la cantidad de elementos a agregar en la lista 1: "))
cant_lista2 = int(input("Ingrese la cantidad de elementos a agregar en la lista 2: "))

if cant_lista1 >= 1 and cant_lista2 >= 1:
    for i in range(1, cant_lista1 + 1):
        elem_lista1 = int(input(f"Ingrese el valor {i} para la lista 1: "))    
        lista1.append(elem_lista1)
    for e in range(1, cant_lista2 + 1):
        elem_lista2 = int(input(f"Ingrese el valor {e} para la lista 2: "))
        lista2.append(elem_lista2)
else:
    print("Ambos numeros digitados deben positivos")

for suma_resta in lista1:
    suma_listas += suma_resta
    resta_listas += suma_resta
for suma_resta in lista2:
    suma_listas += suma_resta
    resta_listas -= suma_resta

print(f"La suma entre las dos listas es {suma_listas}")
print(f"La resta entre las dos listas es {resta_listas}")
