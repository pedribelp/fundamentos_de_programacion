#Programa, parcial de fundamentos de programacion.
sistema = "S"

while sistema == "S": 
  estudiantes = {"Nombre" : "", "Matricula" : ""}

  estudiantes["Nombre"] = input("Ingrese el nombre del estudiante: ")
  estudiantes["Matricula"] = input("Ingrese su matricula: ")
  print(estudiantes)
  letras = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
  primera_nota = int(input("Ingrese la primera nota: "))
  segunda_nota = int(input("Ingrese la segunda nota: "))
  tercera_nota = int(input("Ingrese la tercera nota: "))
  cuarta_nota = int(input("Ingrese la cuarta nota: "))

  notas = []
  notas.append(primera_nota)
  notas.append(segunda_nota)
  notas.append(tercera_nota)
  notas.append(cuarta_nota)
  if notas[0] < 0 or notas[0] > 100 or notas[0] in letras or notas[1] < 0 or notas[1] > 100 or notas[1] in letras or notas[2] < 0 or notas[2] > 100 or notas[2] in letras or notas[3] < 0 or notas[3] > 100 or notas[3] in letras:
    print("Las notas deben ser mayores o iguales a 0 y menores o iguales a 100")
    break
  else:
    promedio = sum(notas)/len(notas )



    print("El promedio de ", estudiantes["Nombre"], " es de ", promedio)
  sistema = input("Desea hacer lo mismo con otro estudiante? (S/N): ")
