import json

def cargar_preguntas():
    try:
        with open("archivo_pregunta.json", "r") as archivo:
            preguntas = json.load(archivo)
    except FileNotFoundError:
        preguntas = []
    return preguntas

def mostrar_preguntas_una_por_una(preguntas):
    if not preguntas:
        print("No hay preguntas disponibles.")
        return

    for i, pregunta in enumerate(preguntas, 1):
        print(f"Pregunta {i}: {pregunta['texto']}")
        respuesta = input("Responde 's' para Sí o 'n' para No (s/n): ").strip().lower()

        if respuesta == 's':
            print("Respuesta: Sí\n")
        elif respuesta == 'n':
            print("Respuesta: No\n")
        else:
            print("Respuesta no válida. Debes ingresar 's' para Sí o 'n' para No.")

        # Puedes agregar lógica adicional aquí, como almacenar las respuestas.

# Cargar preguntas desde el archivo JSON
preguntas = cargar_preguntas()

# Mostrar preguntas una por una
mostrar_preguntas_una_por_una(preguntas)
