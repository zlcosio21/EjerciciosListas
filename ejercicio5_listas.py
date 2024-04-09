#De una lista de números, identifique el que más se repite.

n = int(input("Ingrese la cantidad de elementos de la lista: "))
     
lista = []
numrepetido = []
norepetido = []

for i in range(1, n + 1):
  elemen_lista = int(input(f"Ingrese el valor del elemento {i} de la lista: "))
  lista.append(elemen_lista)

for i in lista:
  if i not in norepetido:
    norepetido.append(i)
  else:
    numrepetido.append(i)

print(f"El numero que mas se repite en la lista es el numero {numrepetido}")
