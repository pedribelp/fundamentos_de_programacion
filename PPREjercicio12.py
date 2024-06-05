#Leer dos números enteros y si la diferencia entre los dos números es par mostrar en pantalla la suma de los dígitos de los números, si dicha diferencia es un número primo menor que 10 entonces mostrar en pantalla el producto de los dos números y si la diferencia entre ellos terminar en 4 mostrar en pantalla todos los dígitos por separado.

print("Juego (Ejercicio 12): Me daras dos numeros de esos sacare su diferencia si: Su resultado es un numero par te mostrare la suma entre los 2 numeros Si su resultado es un numero primo te mostrare su producto Si termina en cuatro el resultado te mostrare los digitos de los numeros")

num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))


if num1 and num2 <= 0 or num1 and num2 >= 100 or num1 and num2 < 10:

    quit("El numero dado es mayor a 2 digitos o es negativo.")

else:
    resultado = abs(num1 - num2)

    if resultado %2 == 0: 
        primerDigito = int(num1/10) 
        segundoDigito = num1%10 
        tercerDigito = int(num2/10)
        cuartoDigito = num2%10
        print("El numero es un numero par: » La suma de los digitos es: ", primerDigito + segundoDigito + tercerDigito + cuartoDigito)
    else:
        print("El resultado no es un numero par...")

    if resultado == 2 or resultado == 3 or resultado == 5 or resultado == 7:
        print("Este numero es un numero primo menor a 10 » La multiplicacion de los numeros es: ", num1*num2)
    else:
        print("El resultado no es un numero primo...")
    if resultado%10 == 4: 
        print("La diferencia de los numeros", num1, "y ", num2, " terminan en 4 te mostrare los digitos por separado de cada numero:")

        print("Digitos del primero numero (", num1, "): ")
        for digitos in str(num1):
            print(digitos)
        print("Digitos del segundo numero (", num2, "): ")
        for digitos in str(num2):
            print(digitos)
    else:
        print("El numero no termina en 4...")
