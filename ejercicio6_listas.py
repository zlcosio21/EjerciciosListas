#Dado un arreglo, indique si es simétrico, un arreglo es simétrico si siendo longitud par los números de la primera mitad son iguales al inverso de la otra mitad. ○ Ejemplo: El arreglo [1,2,3,3,2,1] es simétrico. En caso de que la longitud sea impar, se ignorará el elemento central y se seguirá la misma lógica anterior. ○ Ejemplo: El arreglo [3,5,7,8,7,5,3] es de longitud impar y es simétrico.


a = int(input("Ingrese la longitud del arreglo: "))


arreglo = []


for i in range(1, a + 1):
  elem_arreglo = int(input(f"Ingrese el valor del elemento {i}: "))
  arreglo.append(elem_arreglo)

if len(arreglo) % 2 == 0:
  primera_mitad = arreglo[:len(arreglo) // 2]
  segunda_mitad = arreglo[len(arreglo) // 2:]
  if primera_mitad == segunda_mitad[::-1]:
    print("Es simetrica")
  else:
    print("No es simétrica")
else:
  primera_mitad = arreglo[:len(arreglo) // 2]
  segunda_mitad = arreglo[len(arreglo) // 2:]
  if primera_mitad != segunda_mitad[1::1]:
    print("es simétrico")
  else:
    print("no es simétrico")