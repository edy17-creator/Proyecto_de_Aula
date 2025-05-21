
import webbrowser
url= "https://youtube.com/playlist?list=PLZjTheZ5n5YEZls66Ix1x-bYPGxRnqhmP&si=oNRlX_4EqH1NahML" 
import os 
def limpiar_pantalla():
    if os.name=='nt':
       os.system('cls')
    else:
       os.system('clear')




print("bienvenido a nuestro programa")
print("esta es una pagina dirigida a la educación matemática en los jovenes")
nombre=input("ingrese su nombre: ")
Nidentidad=input("ingrese su numero de identidad: ")
grado=input("ingrese el grado que está cursando: ")
edad=int(input("ingrese su edad(se admite entre el rango de 12 a 19 años): "))
limpiar_pantalla()

if edad<=12:
    print("Usted no tiene la edad minima (de 12 a 19 años) ")
    while edad<=12:
        edad=int(input("ingrese una edad valida: "))


print("")
print("-1 Estudiante")
print("-2 Docente")
print("-3 recepcionista")

opcion=int(input("Elija un tipo de usuario: "))
limpiar_pantalla()

if opcion==1:
    preguntas = [
    "¿que numero sigue en la secuencia?"
     " 3,6,12,24,__ ",
    "si 5 lapices cuestan 1500 pesos, ¿cuanto cuestan 8 lapices al mismo precio por unidad?",
    "¿cual es el numero que falta en la serie?"
    " 7,14,__,56,112",
    "¿Que numero la operacion correctamente?"
    " (6 + 3) * 2 = __ ",
    " Si un rectángulo tiene un largo de 8 cm y un ancho de 5 cm, ¿cuál es su área?",
    "¿Cuál es el número que falta en la secuencia lógica?"
    " 81, 27, 9, 3, __",
    "Si un número multiplicado por 4 da 36, ¿cuál es ese número?",
    "¿Qué número falta en esta operación? 15 + __ = 3 * 10",
    "El doble de un número es 64. ¿Cuál es la mitad de ese número?",
    "Un tren recorre 60 km en una hora. ¿Cuánto recorrerá en 4 horas a la misma velocidad?"

]

opciones = [
    ["a) 30", "b) 36", "c) 48", "d) 50"],
    ["a) 2000", "b) 2200", "c) 2400", "d) 1800"],
    ["a) 21", "b) 28", "c) 35", "d) 42"],
    ["a) 12", "b) 16", "c) 18", "d) 20"],
    ["a) 13 cm²", "b) 40 cm²", "c) 26 cm²z", "d) 80 cm²"],
    ["a) 0", "b) 1", "c) 2","d) 0.5"],
    ["a) 8", "b) 9", "c) 10", "d) 12"],
    ["a) 10", "b) 15", "c) 20","d) 25"],
    ["a) 16", "b) 32", "c) 8","d) 4"],
    ["a) 180 km", "b) 200 km", "c) 240 km", "d) 300 km"]
]

respuestas_correctas = ["c", "c", "b", "c","b","b","b","b","a","c"]

puntos = 0

for i in range(len(preguntas)):
    print(f"\nPregunta {i+1}: {preguntas[i]}")
    for opcion in opciones[i]:
        print(opcion)
    respuesta = input("Tu respuesta: ").lower()
    puntos += respuesta == respuestas_correctas[i]

    while respuesta not in ["a","b","c","d"]:
        print("Escoja una opción valida (a,b,c,d)")
        respuesta=input("tu respueta: ").lower()
    
    if respuesta==respuestas_correctas[i]:
        puntos+=1

# Resultado
print(f"\nObtuviste {puntos} de {len(preguntas)} respuestas correctas.")
print("los temas disponibles son los siguientes:")
print("1 - decimales")
print("2 - division")
print("3 - Minimo comun multiplo")
print("4 - factorización")
print("5 - porcentajes")
print("6 - logaritmo")
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
      p=input("deseas ver algunos vicdeos para entender mejor (si o no)").lower()
      if p=="si":
          print("aqui tienes una lista de videos que te podran ayudar con tu problematica:")
          webbrowser.open(url)
      else:
          print("espero que esta información hay sido de ayuda")
          
if ayuda==2:
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
       p=input("¿deseas ver algunos videos para reforzar lo aprendido?(si o no)")
       if p=="si":
           webbrowser.open()
    


