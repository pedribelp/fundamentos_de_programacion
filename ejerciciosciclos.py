#Ejercicio 1. Leer un numero entero y mostrar todos los enteros comprendidos entre 1 y el numero leido
while True:
    numero = input("Ejercicio 1. Leer un numero entero y mostrar todos los enteros comprendidos entre 1 y el numero leido. Ingresa un número entero: ")
    if numero.lstrip('-').isdigit():
        numero = int(numero)
        break
    else:
        print("Entrada no válida. Por favor, ingresa un número entero.")

for i in range(1, numero + 1):
    print(i)
#Ejercicio 2. Leer un numero entero y mostrar todos los pares comprendidos entre 1 y el numero leido
while True:
    numero = input("Ejercicio 2. Leer un numero entero y mostrar todos los pares comprendidos entre 1 y el numero leido. Ingresa un número entero: ")
    if numero.lstrip('-').replace('.', '', 1).isdigit() and numero.count('.') == 0:
        numero = int(numero)
        break
    else:
        print("Entrada no válida. Por favor, ingresa un número entero.")

for i in range(1, numero + 1):
    if i % 2 == 0:
        print(i)
#Ejercicio 3. Leer un numero entero y mostrar todos los divisores exactos del numero comprendidos entre 1 y el numero leido
while True:
    numero = input("Ejercicio 3. Leer un numero entero y mostrar todos los divisores exactos del numero comprendidos entre 1 y el numero leido. Ingresa un número entero: ")
    if numero.lstrip('-').replace('.', '', 1).isdigit() and numero.count('.') == 0:
        numero = int(numero)
        break
    else:
        print("Entrada no válida. Por favor, ingresa un número entero.")

for i in range(1, numero + 1):
    if numero % i == 0:
        print(i)
#Ejercicio 4. Leer dos números y mostrar todos los enteros comprendidos entre ellos
while True:
    numero1 = input("Ejercicio 4.Leer dos números y mostrar todos los enteros comprendidos entre ellos.  Ingresa el primer número entero: ")
    numero2 = input("Ingresa el segundo número entero: ")
    if (numero1.lstrip('-').replace('.', '', 1).isdigit() and numero1.count('.') == 0) and \
       (numero2.lstrip('-').replace('.', '', 1).isdigit() and numero2.count('.') == 0):
        numero1 = int(numero1)
        numero2 = int(numero2)
        break
    else:
        print("Entrada no válida. Por favor, ingresa números enteros.")

for i in range(numero1, numero2 + 1):
    print(i)
#Ejercicio 5. Leer dos números y mostrar todos los números terminados en 4 comprendidos entre ellos
while True:
    numero1 = input("Ejercicio 5.Leer dos números y mostrar todos los números terminados en 4 comprendidos entre ellos. Ingresa el primer número entero: ")
    numero2 = input("Ingresa el segundo número entero: ")
    if (numero1.lstrip('-').replace('.', '', 1).isdigit() and numero1.count('.') == 0) and \
       (numero2.lstrip('-').replace('.', '', 1).isdigit() and numero2.count('.') == 0):
        numero1 = int(numero1)
        numero2 = int(numero2)
        break
    else:
        print("Entrada no válida. Por favor, ingresa números enteros.")

for i in range(numero1, numero2 + 1):
    if i % 10 == 4:
        print(i)
#Ejercicio 6. Leer un número entero de tres dígitos y mostrar todos los enteros comprendidos entre 1 y cada uno de los dígitos. 
print("Ejercicio 6: Leer un número entero de tres dígitos y mostrar todos los enteros comprendidos entre 1 y cada uno de los dígitos. ")
while True:
    numero = input("Ingresa un número entero de tres dígitos: ")
    if numero.lstrip('-').replace('.', '', 1).isdigit() and len(numero) == 3 and numero.count('.') == 0:
        break
    else:
        print("Entrada no válida. Por favor, ingresa un número entero de tres dígitos.")

for digito in numero:
    digito = int(digito)
    for i in range(1, digito + 1):
        print(i)
 #Ejercicio 7. Mostrar en pantalla todos los enteros comprendidos entre 1 y 100.
print("Ejercicio 7: Mostrar en pantalla todos los enteros comprendidos entre 1 y 100.")
for i in range(1, 101):
    print(i)

   #Ejercicio 8. Mostrar en pantalla todos los pares comprendidos entre 20 y 200
print( "Ejercicio 8: Mostrar en pantalla todos los pares comprendidos entre 20 y 200")
for i in range(20, 201):
    if i % 2 == 0:
        print(i)
   #Ejercicio 9. Mostrar en pantalla todos los números terminados en 6 comprendidos entre 25 y 205
print( "Ejercicio 9: Mostrar en pantalla todos los números terminados en 6 comprendidos entre 25 y 205")
for i in range(25, 206):
    if i % 10 == 6:
        print(i)
   #Ejericio 10. Leer un número entero y determinar a cuánto es igual la suma de todos los enteros comprendidos entre 1 y el número leído
while True:
    numero = input("Ejercicio 10. Leer un número entero y determinar a cuánto es igual la suma de todos los enteros comprendidos entre 1 y el número leído. Ingresa un número entero: ")
    if numero.lstrip('-').replace('.', '', 1).isdigit() and numero.count('.') == 0:
        numero = int(numero)
        break
    else:
        print("Entrada no válida. Por favor, ingresa un número entero.")

suma = sum(range(1, numero + 1))
print(f"La suma de todos los enteros comprendidos entre 1 y {numero} es: {suma}") 
#Ejercicio 11. Leer un número entero de dos dígitos y mostrar en pantalla todos los enteros comprendidos entre un dígito y otro.
while True:
    numero = input("Ejercicio 11. Leer un número entero de dos dígitos y mostrar en pantalla todos los enteros comprendidos entre un dígito y otro. Ingresa un número entero de dos dígitos: ")
    if numero.lstrip('-').isdigit() and len(numero) == 2:
        numero = abs(int(numero))
        break
    else:
        print("Entrada no válida. Por favor, ingresa un número entero de dos dígitos.")

digito1 = int(str(numero)[0])
digito2 = int(str(numero)[1])

for i in range(min(digito1, digito2), max(digito1, digito2) + 1):
    print(i)
#Ejercicio 12.Leer un número entero de 3 dígitos y determinar si tiene el dígito 1.
while True:
    numero = input("Ejercicio 12.Leer un número entero de 3 dígitos y determinar si tiene el dígito 1.  Ingresa un número entero de tres dígitos: ")
    if numero.lstrip('-').isdigit() and len(numero) == 3:
        numero = int(numero)
        break
    else:
        print("Entrada no válida. Por favor, ingresa un número entero de tres dígitos.")

if '1' in str(abs(numero)):
    print("El número tiene el dígito 1.")
else:
    print("El número no tiene el dígito 1.")
#Ejercicio 13.  Leer un entero y mostrar todos los múltiplos de 5 comprendidos entre 1 y el número leído.
while True:
    numero = input("Ejercicio 13. Leer un entero y mostrar todos los múltiplos de 5 comprendidos entre 1 y el número leído. Ingresa un número entero: ")
    if numero.lstrip('-').isdigit():
        numero = int(numero)
        break
    else:
        print("Entrada no válida. Por favor, ingresa un número entero.")

for i in range(5, numero + 1, 5):
    print(i)
    
#Ejerciico 14.  Mostrar en pantalla los primeros 20 múltiplos de 3.
print("Ejericicio 14. Mostrar en pantalla los primeros 20 múltiplos de 3.")
for i in range(1, 21):
    print(i * 3)
    
#Ejercicio 15. Escribir en pantalla el resultado de sumar los primeros 20 múltiplos de 3.
print("Ejercicio 15.  Escribir en pantalla el resultado de sumar los primeros 20 múltiplos de 3.")
suma = sum(i * 3 for i in range(1, 21))
print(f"La suma de los primeros 20 múltiplos de 3 es: {suma}")
#Ejercicio 16. Promediar los x primeros múltiplos de 2 y determinar si ese promedio es mayor que los y primeros múltiplos de 5 para valores de x y y leídos.
print("Ejercicio 16. Promediar los x primeros múltiplos de 2 y determinar si ese promedio es mayor que los y primeros múltiplos de 5 para valores de x y y leídos. ")
while True:
    x = input("Ingresa el valor de x (número entero): ")
    y = input("Ingresa el valor de y (número entero): ")
    if x.lstrip('-').isdigit() and y.lstrip('-').isdigit():
        x = int(x)
        y = int(y)
        break
    else:
        print("Entrada no válida. Por favor, ingresa números enteros.")

promedio_multiplos_2 = sum(i * 2 for i in range(1, x + 1)) / x
promedio_multiplos_5 = sum(i * 5 for i in range(1, y + 1)) / y

if promedio_multiplos_2 > promedio_multiplos_5:
    print("El promedio de los primeros", x, "múltiplos de 2 es mayor que el promedio de los primeros", y, "múltiplos de 5.")
else:
    print("El promedio de los primeros", y, "múltiplos de 5 es mayor que el promedio de los primeros", x, "múltiplos de 2.")

#Ejercicio 17.Leer números hasta que digiten 0 y determinar a cuánto es igual el promedio de los números terminados en 5.
numeros_terminados_en_5 = []
print("Ejercicio 17.Leer números hasta que digiten 0 y determinar a cuánto es igual el promedio de los números terminados en 5. ")
while True:
    numero = input("Ingresa un número entero (0 para terminar): ")
    if numero.lstrip('-').isdigit():
        numero = int(numero)
        if numero == 0:
            break
        if abs(numero) % 10 == 5:
            numeros_terminados_en_5.append(numero)
    else:
        print("Entrada no válida. Por favor, ingresa un número entero.")

if numeros_terminados_en_5:
    promedio = sum(numeros_terminados_en_5) / len(numeros_terminados_en_5)
    print(f"El promedio de los números terminados en 5 es: {promedio}")
else:
    print("No se ingresaron números terminados en 5.")
#Ejercicio 18. Generar los números del 1 al 10 utilizando un ciclo que vaya de 10 a 1. 
print("Ejercicio 18. Generar los números del 1 al 10 utilizando un ciclo que vaya de 10 a 1. ")
for i in range(10, 0, -1):
    print(11 - i)
#Ejercicio 19. Leer un número entero y mostrar en pantalla su tabla de multiplicar.
print("Ejercicio 19. Leer un número entero y mostrar en pantalla su tabla de multiplicar")
while True:
    numero = input("Ingresa un número entero: ")
    if numero.lstrip('-').isdigit():
        numero = int(numero)
        break
    else:
        print("Entrada no válida. Por favor, ingresa un número entero.")

for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")
#Ejercicio 20. Leer un número entero y calcular a cuánto es igual la sumatoria de todas las factoriales de los números comprendidos entre 1 y el número leído.
print("Ejercicio 20. Leer un número entero y calcular a cuánto es igual la sumatoria de todas las factoriales de los números comprendidos entre 1 y el número leído. ")
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

while True:
    numero = input("Ingresa un número entero: ")
    if numero.lstrip('-').isdigit():
        numero = int(numero)
        break
    else:
        print("Entrada no válida. Por favor, ingresa un número entero.")

sumatoria_factoriales = sum(factorial(i) for i in range(1, numero + 1))
print(f"La sumatoria de todas las factoriales de los números comprendidos entre 1 y {numero} es: {sumatoria_factoriales}")
