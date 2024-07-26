#Ejercicio 1. Función de Saludo.
def holaConNombre(name):
  print("Hello " + name + "!")
nombre_usuario = input("Por favor, ingresa tu nombre: ")
holaConNombre(nombre_usuario) 

#Ejercicio 2. Función de Suma.
def suma(a, b):
  return a + b
numero1 = float(input("Ahora, vamos a sumar. Por favor, ingresa el primer número: "))
numero2 = float(input("Por favor, ingresa el segundo número: "))
result = suma(numero1, numero2)
print("La suma es:", result)

#Ejercicio 3. Función de área de un rectángulo.
def areaRectangulo(base, altura):
  return base * altura
base = float(input("Ahora, buscaremos el área de un rectángulo. Por favor, ingresa la base del rectángulo: "))
altura = float(input("Por favor, ingresa la altura del rectángulo: "))
resultado = areaRectangulo(base, altura)
print("El área del rectángulo es:", resultado)

#Ejercicio 4. Número Par o Impar
def esPar(numero):
  if numero % 2 == 0:
    return True
  else:
    return False
numero = int(input("Seguimos, vamos a determinar si un número es par o impar. Por favor, ingresa un número: "))
if esPar(numero):
  print(f"El número {numero} es par.")
else:
  print(f"El número {numero} es impar.")

#Ejercicio 5. Pedir al usuario que ingrese la temperatura en grados Celsius
def celsiusAFahrenheit(celsius):
  return celsius * 9/5 + 32
celsius = float(input("Por favor, ingresa la temperatura en grados Celsius: "))
fahrenheit = celsiusAFahrenheit(celsius)
print(f"{celsius} grados Celsius son {fahrenheit} grados Fahrenheit.")

#Ejercicio 6. Máximo de tres númmeros
def maximoDeTres(a, b, c):
 return max(a, b, c)
numero1 = float(input("Por favor, ingresa el primer número: "))
numero2 = float(input("Por favor, ingresa el segundo número: "))
numero3 = float(input("Por favor, ingresa el tercer número: "))
maximo = maximoDeTres(numero1, numero2, numero3)
print(f"El máximo de los tres números es: {maximo}")

#Ejercicio 7. Palíndromo
def esPalindromo(palabra):
  return palabra == palabra[::-1]
palabra = input("Por favor, ingresa una palabra: ")
if esPalindromo(palabra):
  print(f"La palabra '{palabra}' es un palíndromo.")
else:
  print(f"La palabra '{palabra}' no es un palíndromo.")

#Ejercicio 8. Factorial
def factorial(n):
  if n == 0:
      return 1
  else:
      return n * factorial(n - 1)
numero = int(input("Por favor, ingresa un número para calcular su factorial: "))
resultado = factorial(numero)
print(f"El factorial de {numero} es {resultado}.")


#Ejercicio 9. Contar Vocales
def contarVocales(cadena):
  vocales = "aeiouAEIOU"
  contador = 0
  for letra in cadena:
      if letra in vocales:
          contador += 1
  return contador
cadena = input("Por favor, ingresa una cadena de texto: ")
numero_de_vocales = contarVocales(cadena)
print(f"La cadena '{cadena}' tiene {numero_de_vocales} vocales.")


#Ejercicio 10. Números Primos
def esPrimo(numero):
    if numero <= 1:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True
numero = int(input("Por favor, ingresa un número: "))
if esPrimo(numero):
    print(f"El número {numero} es primo.")
else:
    print(f"El número {numero} no es primo.")
