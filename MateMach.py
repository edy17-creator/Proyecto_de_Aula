import webbrowser
import os 
import time
url= "https://youtube.com/playlist?list=PLZjTheZ5n5YEZls66Ix1x-bYPGxRnqhmP&si=oNRlX_4EqH1NahML" 
div="https://youtu.be/mQ4wKV9_pZs?si=zwlpXULYgvjWAImC"
por="https://youtu.be/RE3XoDORMys?si=KiTGi39yeH6s1tA5"
ecu="https://www.youtube.com/watch?v=IHblqjW8RY8&t=2s"
mcm="https://youtu.be/txLlA_fyL5g?si=Y-G0Pd6bDN-v6cs6"
fac="https://youtu.be/a8CUEopWCN0?si=hLSiUw2kgwhVjXS-"

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
        elif ayuda==3:
            print("tema:minimo comun multiplo")
            print("""El mínimo común múltiplo (MCM)** es el número entero positivo más pequeño que es
                  múltiplo de dos o más números a la vez. Es decir, es el menor número que puede ser dividido
                   exactamente por cada uno de esos números sin dejar residuo. El MCM se utiliza para encontrar
                   un punto común en situaciones donde se requiere que varios elementos coincidan en ciclos o
                   repeticiones, y es una herramienta fundamental en la resolución de problemas matemáticos
                   relacionados con fracciones, tiempos y sincronización de eventos.""")
            print("""ejemplos:
                  Claro, aquí tienes **3 ejemplos de mínimo común múltiplo (MCM)**:

                   1. MCM de 3 y 5:
                   Los múltiplos comunes son 15, 30, 45...
                   El MCM es 15.

                   2. MCM de 6 y 8:
                   Los múltiplos comunes son 24, 48, 72...
                   El MCM es 24.

                   3. MCM de 4, 6 y 12:
                   Los múltiplos comunes son 12, 24, 36...
                   El MCM es 12.""")
            p=input("¿deseas ver algunos videos para reforzar lo aprendido?(si o no) ").lower()
            if p=="si":
                 webbrowser.open(mcm)
            else:
                print("espero que la información haya sido util")
        elif ayuda==4:
            print("tema:factorización")
            print("""La factorización es el proceso de descomponer una expresión matemática en factores,
                   similar a descomponer un número en sus factores primos. Es la operación inversa de la
                   multiplicación, donde en lugar de multiplicar, se busca encontrar los componentes que,
                   al multiplicarse, dan la expresión original. """)
            print("""ejemplos: 

                  1. Factor común

                  Concepto:
                  Consiste en sacar el mayor factor que sea común a todos los términos de la expresión.

                  Ejemplo:
                  6x + 9
                  Factorización:
                  3(2x + 3)
                  El número 3 es común a ambos términos.

                   2. Diferencia de cuadrados

                   Concepto:

                  Se aplica cuando tienes dos términos al cuadrado separados por un signo menos.

                  La forma general es:

                  a^2 - b^2 = (a - b)(a + b)

                  Ejemplo:
                  x^2 - 16
                  Factorización:
                  (x - 4)(x + 4)
                  x^2 y 16 son cuadrados perfectos.

                   3. Trinomio cuadrado perfecto

                  Concepto:
                  Es un trinomio que resulta del cuadrado de un binomio.

                  Forma general:
                  a^2 + 2ab + b^2 = (a + b)^2

                   Ejemplo:
                  x^2 + 6x + 9
                  Factorización:
                  (x + 3)^2
                  x^2 es el cuadrado de x, 9 es el cuadrado de 3, y 6x = 2 * x * 3

                   4. Trinomio de la forma x^2 + bx + c

                  Concepto:

                  Se busca dos números que sumen b y se multipliquen para dar c.

                  Forma general:
                  x^2 + bx + c = (x + m)(x + n) con m+n = b y m \cdot n = c

                  Ejemplo:
                  x^2 + 5x + 6 

                  Factorización:
                  (x + 2)(x + 3)
                  2 + 3 = 5y 2 \cdot 3 = 6
 
                  5. Suma o diferencia de cubos

                  Concepto:
                   Se usa cuando los términos son cubos perfectos.
                   Formas:

                   a^3 - b^3 = (a - b)(a^2 + ab + b^2)
                   a^3 + b^3 = (a + b)(a^2 - ab + b^2)

                  Ejemplo (diferencia):
                  x^3 - 8
                  Factorización:
                  (x - 2)(x^2 + 2x + 4)

                   Ejemplo (suma):
                   x^3 + 27
                  Factorización:
                  (x + 3)(x^2 - 3x + 9)""")
            p=input("¿deseas ver algunos videos para reforzar lo aprendido?(si o no) ").lower()
            if p=="si":
                 webbrowser.open(fac)
            else:
                print("espero que la información haya sido util")
        elif ayuda==5:
            print("tema:porcentajes")
            print("""El porcentaje es una forma de expresar una proporción o parte de un total 
                  como una fracción de 100. Se representa con el símbolo %. Por ejemplo, decir
                   que un producto tiene un 20% de descuento significa que el precio se reduce
                   en 20 partes de cada 100.""")
            print("""
               🧮 ¿Cómo se calcula un porcentaje?

               1. **Sacar un porcentaje de un número

               👉 Multiplica el número por el porcentaje y divide entre 100.

                Ejemplo: ¿Cuál es el 25% de 200?


                   200/(25/100)=50

                  2. Saber qué porcentaje representa una cantidad de otra

                  👉 Divide la parte entre el total y multiplica por 100.

                  Ejemplo: Si 30 personas de 50 aprobaron:

                  30/50(100)=60%

                   3.Subir o bajar un número con un porcentaje

                  Subir (aumentar):
  
                  Suma el porcentaje al 100% y multiplica.

                     Ejemplo: Subir 100 en un 20%
  
                  100 * 1.20 = 120

                  Bajar (descuento):
                  Resta el porcentaje al 100% y multiplica.

                  Ejemplo: Bajar 100 en un 20%

                  100 * 0.80 = 80""")
            p=input("¿deseas ver algunos videos para reforzar lo aprendido?(si o no) ").lower()
            if p=="si":
                 webbrowser.open(por)
            else:
                print("espero que la información haya sido util")
        elif ayuda==6:
            print("tema:ecuaciones")
            print("""Una ecuación es una igualdad matemática que contiene una o más incógnitas
                   y cuya solución consiste en encontrar los valores que hacen que ambos lados
                   de la igualdad sean equivalentes.""")
            print("""ejemplos: 
                  1. x + 5 = 12

                  Explicación: Queremos encontrar el valor de x que hace verdadera esta igualdad.

                  Restamos 5 en ambos lados:

                  x = 12 - 5

                  x = 7

                  Por lo tanto, x = 7 es la solución.""")
            print("---------------------------------------------------------------------")
            print("""2. 3y - 4 = 11

                  Explicación: Primero sumamos 4 a ambos lados para eliminar el -4:

                  3y = 11 + 4 → 3y = 15

                  Luego dividimos entre 3:

                  y = 15 / 3 → y = 5

                  Así que la solución es y = 5.""")
            print("""3. 2a + 3 = a + 9

                  Explicación: Primero restamos a de ambos lados:

                  2a - a + 3 = 9 → a + 3 = 9

                  Luego restamos 3:

                  a = 9 - 3 → a = 6

                  Por lo tanto, a = 6 es la solución.""")
            p=input("¿deseas ver algunos videos para reforzar lo aprendido?(si o no) ").lower()
            if p=="si":
                 webbrowser.open(ecu)
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
        limpiar_pantalla()
        time.sleep(1)
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
            limpiar_pantalla()

        elif opciondocente==2:
            nombre_buscar = input("Ingrese el nombre del estudiante a buscar: ")
            time.sleep(1)
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
                limpiar_pantalla()
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