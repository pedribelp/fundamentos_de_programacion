texto = "Jesucristo es el mismo ayer hoy y siempre"

# 1) Retornar todo el texto en mayúsculas
texto_mayusculas = texto.upper()
print("Texto en mayúsculas:", texto_mayusculas)

# 2) Retornar todo el texto en minúsculas
texto_minusculas = texto.lower()
print("Texto en minúsculas:", texto_minusculas)

# 3) Retornar los dos primeros caracteres del texto
dos_primeros_caracteres = texto[:2]
print("Dos primeros caracteres:", dos_primeros_caracteres)

# 4) Retornar los dos últimos caracteres del texto
dos_ultimos_caracteres = texto[-2:]
print("Dos últimos caracteres:", dos_ultimos_caracteres)

# 5) Retornar la cantidad de veces que se repite el último caracter
ultimo_caracter = texto[-1]
cantidad_repeticiones_ultimo_caracter = texto.count(ultimo_caracter)
print("Cantidad de veces que se repite el último caracter:", cantidad_repeticiones_ultimo_caracter)

# 6) Retornar el texto invertido
texto_invertido = texto[::-1]
print("Texto invertido:", texto_invertido)
