#Iterar lista de nombres e imprimir los que tengan tres o más vocales.

vocales=["a", "e", "i", "o", "u"]
nombres= input ("Ingrese el nombre:")
numero_vocales=0

for item in list(nombres): 
 if item in vocales: 
   numero_vocales+= 1
   
if numero_vocales >=3:
  print(nombres)
else:  
  print("No es correcto, no tiene 3 vocales")

