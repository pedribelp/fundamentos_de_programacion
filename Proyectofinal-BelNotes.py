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
        self.proyectos = {}
        self.historial = []

    def agregar_tarea(self, tarea):
        self.tareas.append(tarea)

    def eliminar_tarea(self, indice):
        if 0 <= indice < len(self.tareas):
            self.historial.append(self.tareas[indice])
            del self.tareas[indice]
        else:
            print("Índice de tarea no válido.")

    def ver_tareas(self):
        if not self.tareas:
            print("No hay tareas en la lista.")
        for i, tarea in enumerate(self.tareas):
            estado = "Completada" if tarea.completada else "Pendiente"
            print(f"{i + 1}. {tarea.titulo} ({tarea.prioridad}) - {estado}")

    
    def editar_tarea(self, indice):
        if 0 <= indice < len(self.tareas):
            tarea = self.tareas[indice]
            print(f"Editando tarea: {tarea.titulo}")
            tarea.titulo = input(f"Ingrese el nuevo título de la tarea (actual: {tarea.titulo}): ") or tarea.titulo
            tarea.descripcion = input(f"Ingrese la nueva descripción (actual: {tarea.descripcion}): ") or tarea.descripcion
            tarea.prioridad = self.solicitar_prioridad(tarea.prioridad)
            tarea.fecha_vencimiento = input(f"Ingrese la nueva fecha de vencimiento (actual: {tarea.fecha_vencimiento}): ") or tarea.fecha_vencimiento
            tarea.categoria = input(f"Ingrese la nueva categoría (actual: {tarea.categoria}): ") or tarea.categoria
            tarea.etiquetas = input(f"Ingrese las nuevas etiquetas (actual: {tarea.etiquetas}): ") or tarea.etiquetas
        else:
            print("Índice de tarea no válido.")


    
    def solicitar_prioridad(self, valor_actual):
        prioridades_validas = ['alta', 'media', 'baja']
        while True:
            prioridad = input(f"Ingrese la prioridad de la tarea ({', '.join(prioridades_validas)}): ").strip().lower()
            if prioridad in prioridades_validas:
                return prioridad
            else:
                print(f"Prioridad inválida. Por favor, ingrese una prioridad válida: {', '.join(prioridades_validas)}")

    def solicitar_fecha(self):
        while True:
            fecha = input("Ingrese la fecha de vencimiento (YYYY-MM-DD): ")
            try:
                datetime.strptime(fecha, '%Y-%m-%d')
                return fecha
            except ValueError:
                print("Formato de fecha inválido. Por favor, ingrese la fecha en el formato YYYY-MM-DD.")

    def guardar_en_archivo(self, archivo):
        with open(archivo, "w") as f:
            json.dump([tarea.__dict__ for tarea in self.tareas], f)

    def cargar_desde_archivo(self, archivo):
        if os.path.exists(archivo):
            with open(archivo, "r") as f:
                tareas = json.load(f)
                self.tareas = [Tarea(**tarea) for tarea in tareas]

    def crear_proyecto(self, nombre):
        if nombre not in self.proyectos:
            self.proyectos[nombre] = []
            print(f"Proyecto '{nombre}' creado.")
        else:
            print(f"El proyecto '{nombre}' ya existe.")

    def eliminar_proyecto(self, nombre):
        if nombre in self.proyectos:
            del self.proyectos[nombre]
            print(f"Proyecto '{nombre}' eliminado.")
        else:
            print(f"El proyecto '{nombre}' no existe.")

    def agregar_tarea_a_proyecto(self, nombre, tarea):
        if nombre in self.proyectos:
            self.proyectos[nombre].append(tarea)
            print(f"Tarea '{tarea.titulo}' agregada al proyecto '{nombre}'.")
        else:
            print(f"El proyecto '{nombre}' no existe.")

    def eliminar_tarea_de_proyecto(self, nombre, indice):
        if nombre in self.proyectos:
            if 0 <= indice < len(self.proyectos[nombre]):
                del self.proyectos[nombre][indice]
                print(f"Tarea eliminada del proyecto '{nombre}'.")
            else:
                print("Índice de tarea no válido.")
        else:
            print(f"El proyecto '{nombre}' no existe.")

    def ver_proyectos(self):
        if not self.proyectos:
            print("No hay proyectos disponibles.")
        for nombre, tareas in self.proyectos.items():
            print(f"Proyecto: {nombre}")
            for i, tarea in enumerate(tareas):
                estado = "Completada" if tarea.completada else "Pendiente"
                print(f"  {i + 1}. {tarea.titulo} ({tarea.prioridad}) - {estado}")

    def ver_historial(self):
        if not self.historial:
            print("No hay tareas completadas.")
        for i, tarea in enumerate(self.historial):
            print(f"{i + 1}. {tarea.titulo} ({tarea.prioridad})")

def mostrar_bienvenida():
    print("\n¡Hola y bienvenido a BelNotes!")
    print("Tu aplicación para gestionar y organizar tus tareas diarias de manera eficiente.")
    print("Aquí puedes agregar, eliminar, ver y editar tareas, así como gestionar proyectos y colaboraciones.")

def main():
    mostrar_bienvenida()
    lista_tareas = ListaTareas()

    while True:
        print("\nOpciones:")
        print("1. Agregar tarea")
        print("2. Eliminar tarea")
        print("3. Ver tareas")
        print("4. Marcar tarea como completada")
        print("5. Editar tarea")
        print("6. Crear proyecto")
        print("7. Eliminar proyecto")
        print("8. Agregar tarea a proyecto")
        print("9. Eliminar tarea de proyecto")
        print("10. Ver proyectos")
        print("11. Ver historial")
        print("12. Salir")

        opcion = input("Ingrese una opción: ")

        if opcion == "1":
            titulo = input("Ingrese el título de la tarea: ")
            descripcion = input("Ingrese la descripción de la tarea: ")
            prioridad = lista_tareas.solicitar_prioridad('')  # Solicitar prioridad con validación
            fecha_vencimiento = lista_tareas.solicitar_fecha()
            categoria = input("Ingrese la categoría de la tarea: ")
            etiquetas = input("Ingrese las etiquetas de la tarea (separadas por comas): ")
            tarea = Tarea(titulo, descripcion, prioridad, fecha_vencimiento, categoria, etiquetas)
            lista_tareas.agregar_tarea(tarea)

        elif opcion == "2":
            lista_tareas.ver_tareas()
            indice = int(input("Ingrese el índice de la tarea a eliminar: ")) - 1
            lista_tareas.eliminar_tarea(indice)

        elif opcion == "3":
            lista_tareas.ver_tareas()

        elif opcion == "4":
            lista_tareas.ver_tareas()
            indice = int(input("Ingrese el índice de la tarea a marcar como completada: ")) - 1
            if 0 <= indice < len(lista_tareas.tareas):
                lista_tareas.tareas[indice].marcar_completada()
            else:
                print("Índice de tarea no válido.")

        elif opcion == "5":
            lista_tareas.ver_tareas()
            indice = int(input("Ingrese el índice de la tarea a editar: ")) - 1
            lista_tareas.editar_tarea(indice)

        elif opcion == "6":
            nombre = input("Ingrese el nombre del proyecto: ")
            lista_tareas.crear_proyecto(nombre)

        elif opcion == "7":
            nombre = input("Ingrese el nombre del proyecto a eliminar: ")
            lista_tareas.eliminar_proyecto(nombre)

        elif opcion == "8":
            nombre = input("Ingrese el nombre del proyecto: ")
            if nombre in lista_tareas.proyectos:
                titulo = input("Ingrese el título de la tarea: ")
                descripcion = input("Ingrese la descripción de la tarea: ")
                prioridad = lista_tareas.solicitar_prioridad('')  # Solicitar prioridad con validación
                fecha_vencimiento = lista_tareas.solicitar_fecha()
                categoria = input("Ingrese la categoría de la tarea: ")
                etiquetas = input("Ingrese las etiquetas de la tarea (separadas por comas): ")
                tarea = Tarea(titulo, descripcion, prioridad, fecha_vencimiento, categoria, etiquetas)
                lista_tareas.agregar_tarea_a_proyecto(nombre, tarea)
            else:
                print(f"El proyecto '{nombre}' no existe.")

        elif opcion == "9":
            nombre = input("Ingrese el nombre del proyecto: ")
            if nombre in lista_tareas.proyectos:
                lista_tareas.ver_proyectos()
                indice = int(input("Ingrese el índice de la tarea a eliminar del proyecto: ")) - 1
                lista_tareas.eliminar_tarea_de_proyecto(nombre, indice)
            else:
                print(f"El proyecto '{nombre}' no existe.")

        elif opcion == "10":
            lista_tareas.ver_proyectos()

        elif opcion == "11":
            lista_tareas.ver_historial()

        elif opcion == "12":
            print("¡Gracias por usar BelNotes! Hasta luego.")
            break

        else:
            print("Opción no válida. Por favor, intente de nuevo.")

if __name__ == "__main__":
    main()
