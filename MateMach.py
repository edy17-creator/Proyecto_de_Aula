import webbrowser
import os 
import time
url= "https://youtube.com/playlist?list=PLZjTheZ5n5YEZls66Ix1x-bYPGxRnqhmP&si=oNRlX_4EqH1NahML" 
div="https://youtu.be/mQ4wKV9_pZs?si=zwlpXULYgvjWAImC"
por="https://youtu.be/RE3XoDORMys?si=KiTGi39yeH6s1tA5"
log="https://youtu.be/kcWwLcvb2-4?si=D5l_W1x5PJ8Bk-EB"


def limpiar_pantalla():
    if os.name=='nt':
       os.system('cls')
    else:
       os.system('clear')   

def menu():
    print("los temas disponibles son los siguientes:")
    print("1 - decimales")
    print("2 - division")
    print("3 - Minimo comun multiplo")
    print("4 - factorización")
    print("5 - porcentajes")
    print("6 - logaritmo")


while True:
    nombre=input("ingrese su nombre su nombre: ")
    Nidentidad=input("ingrese su numero de identidad: ")
    grado=input("diga su curso: ")
    edad=int(input("diga su edad (mayor a 12): "))

    if edad<=12:
        print("Usted no tiene la edad minima ")
        while edad<=12:
            edad=int(input("ingrese una edad valida: "))
    
    limpiar_pantalla()

    print("")
    print("-1 Estudiante")
    print("-2 Docente")
    print("-3 salir")

    opcionusuario=int(input("Elija un tipo de usuario: "))
    limpiar_pantalla()

    if opcionusuario == 1: #estudiante
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
            "c","c","b","c","b","b","b","c","a","c","a","a","b","a","a"
        ]
        puntos = 0
        puntos = 0
        for i in range(len(preguntas)):
            time.sleep(1)
            print(f"\nPregunta {i+1}: {preguntas[i]}")
            for opcion in opciones[i]:
                print(opcion)
                
            respuesta = input("Tu respuesta: ").lower()
            
            while respuesta not in ["a", "b", "c", "d"]:
                print("Escoja una opción válida (a, b, c o d).")
                respuesta = input("Tu respuesta: ").lower()
                
            if respuesta == respuestas_correctas[i]:
                puntos += 1
                print("\n¡CORRECTO!")
            else:
                print(f"Incorrecto. la respuesta correcta era: {respuestas_correctas[i]}")
            
        print(f"\nObtuviste {puntos} de {len(preguntas)} respuestas correctas.")

        print("Guardando resultados en el archivo...")
        with open("resultados_estudiantes.txt", "a") as archivo:
                archivo.write(f"Nombre: {nombre}\n")
                archivo.write(f"ID: {Nidentidad}\n")
                archivo.write(f"Curso: {grado}\n")
                archivo.write(f"Edad: {edad}\n")
                archivo.write(f"Puntaje: {puntos} de {len(preguntas)}\n")
                archivo.write("-" * 40 + "\n")  # Separador

        menu()
        ayuda=int(input("¿En que tema deseas que te ayude? "))
        limpiar_pantalla()
        if ayuda==1:
           print("Tema: los numeros decimales")
           print("""Los números decimales son una forma de escribir los números que están entre
     los números enteros. Se usan para contar partes más pequeñas que uno, como cuando
     dividimos algo. Llevan una coma (o punto, según el país) para separar la parte
     entera de la parte decimal.""")
           print("""ejemplos
          Ejemplo 1: Jugo
          Tienes 1,5 litros de jugo.

          Esto significa que tienes 1 litro entero y medio litro más.

          🍫 Ejemplo 2: Chocolate
          Un chocolate cuesta 2,75 euros.

          Eso significa que cuesta 2 euros y 75 céntimos.

          📏 Ejemplo 3: Regla
         Una regla mide 30,5 centímetros.

         Eso quiere decir 30 centímetros y medio centímetro más.

         🕓 Ejemplo 4: Tiempo
         Viste una película que duró 1,25 horas.

         Eso es 1 hora y un cuarto de hora (15 minutos).

         🧁 Ejemplo 5: Pastel
         Cortaste un pastel y te comiste 0,5 del pastel.

          Eso significa que te comiste la mitad del pastel.""")
           p=input("deseas ver algunos vicdeos para entender mejor (si o no) ").lower()
           if p =="si":
              print("aqui tienes una lista de videos que te pueden ayudar:") 
              webbrowser.open(url)
           else:
               print("espero que esta información haya sido de ayuda")
        elif ayuda==2:
            print("Tema: la división")
            print("a continuación te dejare un pequeño concepto")
            print("""La división es una operación matemática que consiste en repartir una cantidad
           en partes iguales o en averiguar cuántas veces un número (llamado divisor) cabe
           dentro de otro (llamado dividendo). El resultado de una división se llama cociente,
           y si al repartir sobran unidades, eso se llama residuo. """)
            print("")
            print("""aqui tinenes algunos ejemplos:

         1. **10 ÷ 2 = 5**
       (Si tienes 10 caramelos y los repartes entre 2 personas, a cada una le tocan 5).
 
         2. **12 ÷ 3 = 4**
       (Si hay 12 lápices y los divides en 3 grupos iguales, cada grupo tendrá 4 lápices).

         3. **8 ÷ 4 = 2**
       (Si tienes 8 galletas y haces 4 porciones iguales, cada porción tendrá 2 galletas).

         4. **6 ÷ 1 = 6**
       (Dividir entre 1 significa que el número se queda igual).

         5. **9 ÷ 3 = 3**
       (Repartir 9 cosas en 3 partes iguales da 3 en cada parte)""")
            p=input("¿deseas ver algunos videos para reforzar lo aprendido?(si o no) ").lower()
            if p=="si":
                 webbrowser.open(div)
            else:
                print("espero que la información haya sido util")

        input("\npresione enter para volver al menu principal...")
        limpiar_pantalla()


    elif opcionusuario == 2:  # Docente
        print("\n¿Que desea realizar? ")
        print(" > 1 ver resultados guardados ")
        print(" > 2 Buscar resultado especifico ")
        print(" > 3 Borrar los datos guardados ")
        print(" > 4 ver estadisticas generales ")

        opciondocente=int(input("diga su respuesta: "))
        
        if opciondocente==1:
            print("\n-- Resultados de los estudiantes --")
            try:
                with open("resultados_estudiantes.txt", "r") as archivo:
                    contenido = archivo.read()
                    if contenido.strip() == "":
                        print("No hay resultados guardados aún.")
                    else:
                        print(contenido)
            except FileNotFoundError:
                print("No se encontró el archivo de resultados.")
            
            input("\npresione enter para volver al menu principal...")

        elif opciondocente==2:
            nombre_buscar = input("Ingrese el nombre del estudiante a buscar: ")
            with open("resultados_estudiantes.txt", "r") as archivo:
                datos = archivo.read()
                if nombre_buscar.lower() in datos.lower():
                    print("Resultado encontrado:")
                    lineas = datos.split("\n")
                    for i in range(len(lineas)):
                        if nombre_buscar.lower() in lineas[i].lower():
                            print("\n".join(lineas[i:i+5]))  # Muestra nombre + ID + curso + edad + puntaje
                else:
                     print("No se encontró ese nombre.")

            input("\npresione enter para volver al menu principal...")
            limpiar_pantalla()
        
        elif opciondocente==3:
                confirmar = input("¿Está seguro que desea borrar todos los resultados? (si/no): ").lower()
                if confirmar == "si":
                    open("resultados_estudiantes.txt", "w").close()
                    print("Todos los resultados han sido eliminados.")
                else:
                    print("Cancelado.")
        
        elif opciondocente==4:
            print("\n-- Estadísticas generales --")
            try:
                with open("resultados_estudiantes.txt", "r") as archivo:
                    puntos_totales = 0
                    cantidad_estudiantes = 0
                    puntajes = []
                    
                    for linea in archivo:
                        if "Puntaje:" in linea:
                            partes = linea.split()
                            try:
                                correcto = int(partes[1])
                                puntajes.append(correcto)
                                puntos_totales += correcto
                                cantidad_estudiantes += 1
                            except:
                                continue  # Por si hay error de formato

                    if cantidad_estudiantes > 0:
                        promedio = puntos_totales / cantidad_estudiantes
                        print(f"\nEstudiantes registrados: {cantidad_estudiantes}")
                        print(f"Promedio de puntaje: {promedio:.2f}")
                        print(f"Puntaje máximo: {max(puntajes)}")
                        print(f"Puntaje mínimo: {min(puntajes)}")
                    else:
                        print("No hay puntajes registrados aún.")
            except FileNotFoundError:
                print("No se encontró el archivo de resultados.")


    else:
        print("Usted a salido de exitosamente ")