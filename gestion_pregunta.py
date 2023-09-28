import json

def cargar_preguntas():
    try:
        with open("archivo_pregunta.json", "r") as archivo:
            preguntas = json.load(archivo)
    except FileNotFoundError:
        preguntas = []
    return preguntas

def guardar_preguntas(preguntas):
    with open("archivo_pregunta.json", "w") as archivo:
        json.dump(preguntas, archivo, indent=4)

def mostrar_preguntas(preguntas):
    print("\nLista de Preguntas:")
    for i, pregunta in enumerate(preguntas, 1):
        print(f"{i}. {pregunta['texto']}")

def crear_pregunta(preguntas):
    texto_pregunta = input("Ingrese el texto de la pregunta: ")
    nueva_pregunta = {"texto": texto_pregunta}
    preguntas.append(nueva_pregunta)
    guardar_preguntas(preguntas)
    print("Pregunta creada con éxito.")

def editar_pregunta(preguntas):
    mostrar_preguntas(preguntas)
    try:
        indice = int(input("Ingrese el número de la pregunta que desea editar: ")) - 1
        if 0 <= indice < len(preguntas):
            nuevo_texto = input("Ingrese el nuevo texto de la pregunta: ")
            preguntas[indice]["texto"] = nuevo_texto
            guardar_preguntas(preguntas)
            print("Pregunta editada con éxito.")
        else:
            print("Número de pregunta no válido.")
    except ValueError:
        print("Entrada no válida. Ingrese un número válido.")

def eliminar_pregunta(preguntas):
    mostrar_preguntas(preguntas)
    try:
        indice = int(input("Ingrese el número de la pregunta que desea eliminar: ")) - 1
        if 0 <= indice < len(preguntas):
            pregunta_eliminada = preguntas.pop(indice)
            guardar_preguntas(preguntas)
            print(f"Pregunta '{pregunta_eliminada['texto']}' eliminada con éxito.")
        else:
            print("Número de pregunta no válido.")
    except ValueError:
        print("Entrada no válida. Ingrese un número válido.")

# Cargar preguntas desde el archivo JSON
preguntas = cargar_preguntas()

# Ciclo principal del programa
while True:
    print("\nMenú de Gestión de Preguntas:")
    print("1. Mostrar Preguntas")
    print("2. Crear Pregunta")
    print("3. Editar Pregunta")
    print("4. Eliminar Pregunta")
    print("5. Salir")

    opcion = input("Seleccione una opción (1/2/3/4/5): ")

    if opcion == "1":
        mostrar_preguntas(preguntas)
    elif opcion == "2":
        crear_pregunta(preguntas)
    elif opcion == "3":
        editar_pregunta(preguntas)
    elif opcion == "4":
        eliminar_pregunta(preguntas)
    elif opcion == "5":
        print("Saliendo del programa. ¡Hasta luego!")
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción válida (1/2/3/4/5).")
