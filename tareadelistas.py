#Ejercicio 1 
my_lista = [10, 26, 38, 46, 54, 68, 72, 84, 91, 12]
mayor = max(my_lista)
posicion_mayor = my_lista.index(mayor)
print(f"Ejercicio 1: El valor mayor es: {mayor} y está en la posición {posicion_mayor}.")

#Ejercicio 2. Leer 10 enteros, almacenarlos en una lista y determinar en qué posición del arreglo está el mayor número par leído.
my_lista = [10, 26, 38, 46, 54, 68, 72, 84, 91, 12]
numeros_pares = [num for num in my_lista if num % 2 == 0]
if numeros_pares:
    mayor_par = max(numeros_pares)
    posicion_mayor_par = my_lista.index(mayor_par)
    print(f"Ejercicio 2: El mayor número par es: {mayor_par} y está en la posición {posicion_mayor_par}.")
else:
    print("Ejercicio 2: No se ingresaron números pares.")

#Ejercicio 3. Leer 10 enteros, almacenarlos en una lista y determinar en qué posición del arreglo está el mayor número primo leído.
def es_primo(n):
  if n <= 1:
      return False
  for i in range(2, int(n**0.5) + 1):
      if n % i == 0:
          return False
  return True

my_lista = [10, 26, 38, 46, 54, 67, 72, 84, 91, 12]
numeros_primos = [num for num in my_lista if es_primo(num)]
if numeros_primos:
  mayor_primo = max(numeros_primos)
  posicion_mayor_primo = my_lista.index(mayor_primo)
  print(f"Ejercicio 3: El mayor número primo es: {mayor_primo} y está en la posición {posicion_mayor_primo}.")
else:
  print("Ejercicio 3: No se ingresaron números primos.")
  
#Ejercicio 4. Leer 10 números enteros, almacenarlos en una lista y determinar cuántos números de los almacenados en dicho arreglo comienzan en dígito primo.
def es_primer_digito_primo(n):
  primer_digito = int(str(abs(n))[0])
  return es_primo(primer_digito)

my_lista = [60, 86, 38, 71, 54, 68, 72, 84, 91, 22]
cantidad_primer_digito_primo = sum(1 for num in my_lista if es_primer_digito_primo(num))
print(f"Ejercicio 4: Cantidad de números que comienzan con un dígito primo: {cantidad_primer_digito_primo}")

#Ejercicio 5. Leer 10 números enteros, almacenarlos en una lista y determinar en qué posición se encuentra el número primo con mayor cantidad de dígitos pares.
def cantidad_digitos_pares(n):
  return sum(1 for digito in str(abs(n)) if int(digito) % 2 == 0)

my_lista = [10, 11, 38, 46, 55, 65, 78, 84, 97, 12]
numeros_primos = [num for num in my_lista if es_primo(num)]
if numeros_primos:
  primo_mayor_digitos_pares = max(numeros_primos, key=cantidad_digitos_pares)
  posicion_primo = my_lista.index(primo_mayor_digitos_pares)
  print(f"Ejercicio 5: El número primo con mayor cantidad de dígitos pares es: {primo_mayor_digitos_pares} y está en la posición {posicion_primo}.")
else:
  print("Ejercicio 5: No se ingresaron números primos.")
  
#Ejercicio 6. Leer 10 números enteros, almacenarlos en una lista y determinar en qué posiciones se encuentran los números con más de 3 dígitos.
my_lista = [10, 26, 384, 468, 54, 68, 72, 84, 91, 12]
posiciones_mas_de_tres_digitos = [i for i, num in enumerate(my_lista) if len(str(abs(num))) >= 3]
print(f"Ejercicio 6: Los números con más de 3 dígitos se encuentran en las posiciones: {posiciones_mas_de_tres_digitos}.")

#Ejercicio 7. Leer 10 números enteros, almacenarlos en una lista y determinar a cuánto es igual el promedio entero de los datos de la lista.
my_lista = [10, 26, 38, 46, 54, 68, 72, 84, 91, 12]
promedio = sum(my_lista) // len(my_lista)
print(f"Ejercicio 7: El promedio entero de los datos de la lista es: {promedio}.")

#Ejercicio 8. Leer 10 números enteros, almacenarlos en una lista y determinar cuántos números negativos hay.
my_lista = [10, 26, -38, 46, 54, 68, -72, 84, 91, 12]
cantidad_negativos = sum(1 for num in my_lista if num < 0)
print(f"Ejercicio 8: Cantidad de números negativos: {cantidad_negativos}")

#Ejercicio 9. Leer 10 números enteros, almacenarlos en una lista y calcular la factorial a cada uno de los números leídos almacenándolos en otra lista.
import math
my_lista = [4, 8, 3, 6, 9, 7, 2, 14, 31, 12]
factoriales = [math.factorial(num) for num in my_lista]
print(f"Ejercicio 9: Las factoriales de los números leídos son: {factoriales}.")

#Ejercicio 10. Leer 10 números enteros, almacenarlos en una lista. Luego leer un entero y determinar cuántos divisores exactos tiene este último número entre los valores almacenados en la lista.
my_lista = [10, 26, 38, 46, 54, 68, 72, 84, 91, 12]
n = int(input("Ingrese otro número entero: "))
divisores_exactos = sum(1 for num in my_lista if n % num == 0)
print(f"Ejercicio 10: El número {n} tiene {divisores_exactos} divisores exactos en la lista.")
