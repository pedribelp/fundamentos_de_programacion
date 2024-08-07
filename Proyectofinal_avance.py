# Importar bibliotecas necesarias
import os
import json
from datetime import datetime

# Clase para representar una tarea
class Tarea:
    def __init__(self, titulo, descripcion, prioridad, fecha_vencimiento, categoria, etiquetas):
        self.titulo = titulo
        self.descripcion = descripcion
        self.prioridad = prioridad
        self.fecha_vencimiento = fecha_vencimiento
        self.categoria = categoria
        self.etiquetas = etiquetas
        self.completada = False

    def marcar_completada(self):
        self.completada = True

# Clase para representar la lista de tareas
class ListaTareas:
    def __init__(self):
        self.tareas = []

    def agregar_tarea(self, tarea):
        self.tareas.append(tarea)

    def eliminar_tarea(self, indice):
        del self.tareas[indice]

    def ver_tareas(self):
        for i, tarea in enumerate(self.tareas):
            print(f"{i+1}. {tarea.titulo} ({tarea.prioridad})")

    def guardar_en_archivo(self, archivo):
        with open(archivo, "w") as f:
            json.dump([tarea.__dict__ for tarea in self.tareas], f)

    def cargar_desde_archivo(self, archivo):
        if os.path.exists(archivo):
            with open(archivo, "r") as f:
                tareas = json.load(f)
                self.tareas = [Tarea(**tarea) for tarea in tareas]

# Función principal para ejecutar la aplicación
def main():
    lista_tareas = ListaTareas()

    while True:
        print("1. Agregar tarea")
        print("2. Eliminar tarea")
        print("3. Ver tareas")
        print("4. Marcar tarea como completada")
        print("5. Guardar en archivo")
        print("6. Cargar desde archivo")
        print("7. Salir")

        opcion = input("Ingrese una opción: ")

        if opcion == "1":
            titulo = input("Ingrese el título de la tarea: ")
            descripcion = input("Ingrese la descripción de la tarea: ")
            prioridad = input("Ingrese la prioridad de la tarea (alta, media, baja): ")
            fecha_vencimiento = input("Ingrese la fecha de vencimiento de la tarea (YYYY-MM-DD): ")
            categoria = input("Ingrese la categoría de la tarea: ")
            etiquetas = input("Ingrese las etiquetas de la tarea (separadas por comas): ")

            tarea = Tarea(titulo, descripcion, prioridad, fecha_vencimiento, categoria, etiquetas)
            lista_tareas.agregar_tarea(tarea)

        elif opcion == "2":
            indice = int(input("Ingrese el índice de la tarea a eliminar: "))
            lista_tareas.eliminar_tarea(indice)

        elif opcion == "3":
            lista_tareas.ver_tareas()

        elif opcion == "4":
            indice = int(input("Ingrese el índice de la tarea a marcar como completada: "))
            lista_tareas.tareas[indice].marcar_completada()

        elif opcion == "5":
            archivo = input("Ingrese el nombre del archivo para guardar: ")
            lista_tareas.guardar_en_archivo(archivo)

        elif opcion == "6":
            archivo = input("Ingrese el nombre del archivo para cargar: ")
            lista_tareas.cargar_desde_archivo(archivo)

        elif opcion == "7":
            break

if __name__ == "__main__":
    main()
