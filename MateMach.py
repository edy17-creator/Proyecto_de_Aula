nombre=input("diga su nombre: ")
Nidentidad=input("diga su numero de identidad: ")
grado=input("diga su curso: ")
edad=int(input("diga su edad (mayor a 12): "))

if edad<=12:
    print("Usted no tiene la edad minima ")
    while edad<=12:
        edad=int(input("ingrese una edad valida: "))


print("")
print("-1 Estudiante")
print("-2 Docente")
print("-3 padre de familia")
print("-4 recepcionista")

opcion=int(input("Elija un tipo de usuario: "))

if opcion == 1:
    preguntas = [
        "¿Qué número sigue en la secuencia? 3, 6, 12, 24, __",
        "Si 5 lápices cuestan 1500 pesos, ¿cuánto cuestan 8 lápices al mismo precio por unidad?",
        "¿Cuál es el número que falta en la serie? 7, 14, __, 56, 112",
        "¿Qué número completa correctamente la operación? (6 + 3) * 2 = __",
        "Si un rectángulo tiene un largo de 8 cm y un ancho de 5 cm, ¿cuál es su área?",
        "¿Cuál es el número que falta en la secuencia lógica? 81, 27, 9, 3, __",
        "Si un número multiplicado por 4 da 36, ¿cuál es ese número?",
        "¿Qué número falta en esta operación? 15 + __ = 3 * 10",
        "El doble de un número es 64. ¿Cuál es la mitad de ese número?",
        "Un tren recorre 60 km en una hora. ¿Cuánto recorrerá en 4 horas a la misma velocidad?",
        
        # Nivel Intermedio
        "Resuelve la ecuación: 2x - 4 = 10",
        "¿Cuál es el valor de x en la inecuación: 5x + 3 < 18?",
        "Resuelve: (x / 2) + 5 = 11",
        
        # Nivel Avanzado
        "Factoriza: x² - 9",
        "Resuelve la ecuación: (x - 2)(x + 4) = 0"
    ]

    opciones = [
        ["a) 30", "b) 36", "c) 48", "d) 50"],
        ["a) 2000", "b) 2200", "c) 2400", "d) 1800"],
        ["a) 21", "b) 28", "c) 35", "d) 42"],
        ["a) 12", "b) 16", "c) 18", "d) 20"],
        ["a) 13 cm²", "b) 40 cm²", "c) 26 cm²", "d) 80 cm²"],
        ["a) 0", "b) 1", "c) 2", "d) 0.5"],
        ["a) 8", "b) 9", "c) 10", "d) 12"],
        ["a) 10", "b) 15", "c) 20", "d) 25"],
        ["a) 16", "b) 32", "c) 8", "d) 4"],
        ["a) 180 km", "b) 200 km", "c) 240 km", "d) 300 km"],
        
        # Opciones intermedio
        ["a) 7", "b) 6", "c) 8", "d) 10"],
        ["a) x < 3", "b) x < 4", "c) x > 3", "d) x > 4"],
        ["a) 10", "b) 8", "c) 12", "d) 9"],
        
        # Opciones avanzado
        ["a) (x + 3)(x - 3)", "b) (x + 9)(x - 1)", "c) (x - 9)(x - 1)", "d) No se puede factorizar"],
        ["a) x = 2 y x = -4", "b) x = -2 y x = 4", "c) x = 2", "d) x = -4"]
    ]

    respuestas_correctas = [
        "c",  # 48
        "c",  # 2400
        "b",  # 28
        "c",  # 18
        "b",  # 40 cm²
        "b",  # 1
        "b",  # 9
        "c",  # 15
        "a",  # 16
        "c",  # 240 km
        "a",  # x = 7
        "a",  # x < 3
        "b",  # x = 12
        "a",  # (x + 3)(x - 3)
        "a"   # x = 2 y x = -4
    ]

puntos = 0

puntos = 0

for i in range(len(preguntas)):
    print(f"\nPregunta {i+1}: {preguntas[i]}")
    for opcion in opciones[i]:
        print(opcion)
    
    respuesta = input("Tu respuesta: ").lower()
    
    while respuesta not in ["a", "b", "c", "d"]:
        print("Escoja una opción válida (a, b, c o d).")
        respuesta = input("Tu respuesta: ").lower()
    
    if respuesta == respuestas_correctas[i]:
        puntos += 1

print(f"\nTu puntuación final es: {puntos} de {len(preguntas)}")


# Resultado
print(f"\nObtuviste {puntos} de {len(preguntas)} respuestas correctas.")


#if opcion==2:
