#Programa que calcula el indice de masa corporal de una persona

unidad = input("¿Quieres introducir tu peso en kilogramos o libras? (kg/lb): ")

if unidad == "kg":
    peso = float(input("Introduce tu peso en kilogramos: "))
elif unidad == "lb":
    peso = float(input("Introduce tu peso en libras: "))
    peso = peso / 2.2
else:
    print("Unidad no válida. Por favor, introduce 'kg' o 'lb'.")
    exit()

altura = float(input("Introduce tu altura en metros: "))

imc = round(peso / (altura ** 2))
print("Tu Índice de Masa Corporal (IMC) es:", imc)
