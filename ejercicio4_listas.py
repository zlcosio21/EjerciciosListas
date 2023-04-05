#Dada dos listas de caracteres, se requiere contar las diferencias entre ellas y mostrar dicho conteo. ○ Ejemplo: Si se tienen las listas [“A”, “B”, “C”] y [“A”, “E”, “H”], entonces el conteo sería 2 ya que hay dos diferencias. Nota: Las listas deben ser de igual longitud y esto debeser validado.

lista1 = []
lista2 = []
cont_diferencias = 0

cant_lista1 = int(input("Ingrese la cantidad de elementos de la lista 1: "))
cant_lista2 = int(input("Ingrese la cantidad de elementos de la lista 2: "))

for i in range (1, cant_lista1 + 1):
  elem_lista1 = input(f"Ingrese el valor del elemento {i} para la lista 1: ")
  lista1.append(elem_lista1)
for e in range (1, cant_lista2 + 1):
  elem_lista2 = input(f"Ingrese el valor del elemento {e} para la lista 2: ")
  lista2.append(elem_lista2)
print(f"lista 1 = {lista1}")
print(f"lista 2 = {lista2}")

if len(lista1) == len(lista2):
   for i in range(len(lista1)):
    if lista1[i] != lista2[i]:
      cont_diferencias += 1
else:
  print("Las 2 listas deben tener la misma longitud")

print(f"Se encontraron {cont_diferencias} diferencias entre las 2 listas")