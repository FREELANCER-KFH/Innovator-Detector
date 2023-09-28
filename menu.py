def gestionar_preguntas():
    print("Has seleccionado la opción de Gestión de Preguntas.")
    # Aquí puedes agregar la lógica para gestionar preguntas, como agregar, editar o eliminar preguntas.

def evaluar_preguntas():
    print("Has seleccionado la opción de Evaluación de Preguntas.")
    # Aquí puedes agregar la lógica para evaluar preguntas.

while True:
    print("\nMenú:")
    print("1. Gestión de Preguntas")
    print("2. Evaluación de Preguntas")
    print("3. Salir")

    opcion = input("Seleccione una opción (1/2/3): ")

    if opcion == "1":
        gestionar_preguntas()
    elif opcion == "2":
        evaluar_preguntas()
    elif opcion == "3":
        print("Saliendo del programa. ¡Hasta luego!")
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción válida (1/2/3).")
