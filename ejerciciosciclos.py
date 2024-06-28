#Ejercicio 1. Leer un numero entero entero y mostrar todos los enteros comprendidos entre 1 y el numero leido
while True:
    numero = input("Ingresa un número entero: ")
    if numero.lstrip('-').isdigit():
        numero = int(numero)
        break
    else:
        print("Entrada no válida. Por favor, ingresa un número entero.")

for i in range(1, numero + 1):
    print(i)
#Ejercicio 2. Leer un numero entero y mostrar todos los pares comprendidos entre 1 y el numero leido
while True:
    numero = input("Ingresa un número entero: ")
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
    numero = input("Ingresa un número entero: ")
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
    numero1 = input("Ingresa el primer número entero: ")
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
    numero1 = input("Ingresa el primer número entero: ")
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
print("Ejercicio 6:")
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
print("Ejercicio 7:")
for i in range(1, 101):
    print(i)

   #Ejercicio 8. Mostrar en pantalla todos los pares comprendidos entre 20 y 200
print( "Ejercicio 8:")
for i in range(20, 201):
    if i % 2 == 0:
        print(i)
   #Ejercicio 9. Mostrar en pantalla todos los números terminados en 6 comprendidos entre 25 y 205
print( "Ejercicio 9:")
for i in range(25, 206):
    if i % 10 == 6:
        print(i)
   #Ejericio 10. Leer un número entero y determinar a cuánto es igual la suma de todos los enteros comprendidos entre 1 y el número leído
while True:
    numero = input("Ingresa un número entero: ")
    if numero.lstrip('-').replace('.', '', 1).isdigit() and numero.count('.') == 0:
        numero = int(numero)
        break
    else:
        print("Entrada no válida. Por favor, ingresa un número entero.")

suma = sum(range(1, numero + 1))
print(f"La suma de todos los enteros comprendidos entre 1 y {numero} es: {suma}")
