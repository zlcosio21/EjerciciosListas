#Dada una lista de 10 números enteros, se requiere imprimir esos números en orden inverso al que fueron ingresados.

lista = []

for i in range(1, 10 + 1):
  n = int(input(f"Ingrese el valor del elemento {i} de la lista: "))
  lista.append(n)

print(lista)

for e in range(len(lista)-1,-1,-1):
  print(lista[e])