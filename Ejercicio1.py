#Ejercicio 1 de la practica 
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Filtrar números pares
numeros_pares = [num for num in numeros if num % 2 == 0]
print("Números pares:", numeros_pares)

# Filtrar números impares
numeros_impares = [num for num in numeros if num % 2 != 0]
print("Números impares:", numeros_impares)
