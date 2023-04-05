#Dado un arreglo de números (numbers) y un número entero n, determine si n se encuentra en el arreglo. El programa debe imprimir True o False como corresponda.

n = int(input("Ingrese un numero entero: "))
a = int(input("Ingrese la cantidad de elementos del arreglo: "))

arreglo = []

for i in range(1, a + 1):
  elementos_arreglo = int(input(f"Ingrese el valor del elemento {i} del arreglo: "))
  arreglo.append(elementos_arreglo)

for e in range(len(arreglo)):
  if n == arreglo[e]:
    print(True)
    print(f"{n} se encuentra en el arreglo")
    break
  else:
    print(False)