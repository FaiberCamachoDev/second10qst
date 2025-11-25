#========================
#        Punto 1
#========================

def Punto1():
    Edad = ""
    Guardian = True
    print("Gracias por hacer parte de este proceso, te haremos uns preguntas para poder clasificarte")
    while (Guardian):
        Edad = input("Cual es tu edad (solo numero)?: ")
        if not Edad.isdigit():
            print("No es una edad valida, try again.")
            continue
        Edad = int(Edad)
        if Edad >= 120 or Edad <= 0:
            print("No es una edad valida, try again.")
            continue
        else:
            print ("La edad es valida")
            Guardian=False
        print (f"Respondiste lo siguiente: {Edad}")
    print("""
        1.estudias 
        2.trabajas
        3.ninguna
    """)
    actividad = True
    while (actividad):
        informacion_personal = input("seleccione 1, 2 o 3 dependiendo cual sea tu actividad: ")
        if not informacion_personal.isdigit():
            print("ingrese un numero valido(1, 2 o 3).")
            continue
        informacion_personal = int(informacion_personal)
        if informacion_personal <= 0 or informacion_personal >=4:
            print("ingrese un numero valido(1, 2 o 3).")
            continue
        else:
            print ("gracias por la informacion")
            actividad=False

    if Edad < 6:
        print("Clasificación: Infante")
    elif 6 <=  Edad <= 17 and informacion_personal == 1:
        print ("Clasificación: Estudiante escolar")
    elif 18 <= Edad <= 25 and informacion_personal == 1:
        print ("Clasificación: Universitario")
    elif 25 < Edad and informacion_personal == 2:
        print ("Clasificación: Adulto activo")
    elif Edad >= 60 and informacion_personal == 3:
        print ("Clasificación: Adulto mayor jubilado")
    else:
        print ("Clasificación: No determinado")
    

#======================================
#              Punto #2
#======================================

def punto2 ():
    #variables
    Edad = ""
    Guardian = True
    while (Guardian):
        Edad = input("Cual es tu edad (solo numero)?: ")
        if not Edad.isdigit():
            print("No es una edad valida, try again.")
            continue
        Edad = int(Edad)
        if Edad <= 18:
            print("No es una edad valida")
            continue
        else:
            print ("La edad es valida")
            Guardian=False
            print (f"Respondiste lo siguiente: {Edad}")
    licencia = True
    while (licencia):
        Licencia_de_conducir = input("""
        "Tienes licencia de conducir?"\n
        "1. SI"\n
        "2. NO"
        """)
        if not Licencia_de_conducir.isdigit():
            print("ingrese un numero valido (1 o 2)")
            continue
        elif Licencia_de_conducir == "1":
            licencia = False
            print ("perfecto, continuemos")
        elif Licencia_de_conducir == "2":
            print ("No eres valido, gracias por participar.") 
            licencia = False
            exit()

    vehiculo = True
    while (vehiculo):
        vehiculo_propio = input("""
        "Tienes Vehciuclo propio?"\n
        "1. SI"\n
        "2. NO"
        """)
        if not vehiculo_propio.isdigit():
            print("ingrese un numero valido (1 o 2)")
            continue
        elif vehiculo_propio == "1":
            vehiculo = False
            print ("Apto")
        elif vehiculo_propio == "2":
            vehiculo_autorizado = input("""
                    Tienes acceso a un vehiculo autorizado?\n
                    1.Si
                    2.No
                    """)
            if not vehiculo_autorizado.isdigit():
                print("ingrese un numero valido (1 o 2)")
                continue
            if vehiculo_autorizado == "1":
                print ("Apto")
                vehiculo = False 
            else:
                print("no apto")
                vehiculo = False
        
#===========================================
#              Punto # 3
#===========================================

def punto3():
    #Variables
    nombreusuario = ""
    Codigoingreso =""
    listarestringida = {"Andrea", "Carolina", "Paolo", "Oliver"}

    ingreso = True
    while (ingreso):
        nombreusuario = str(input("Digita un nombre de usuario"))
        if nombreusuario in listarestringida:
            print("Te encuentras en lista restringida")
            ingreso=False
            continue
        else:
            print("Continua con la siguiente pregunta")


        Codigoingreso = input("ingresa un codigo de ingreso")
        if not Codigoingreso.isdigit():
            print("ingrese un codigo valido, unicamente valores numericos")

        else:
            Codigoingreso = int(Codigoingreso)
            if Codigoingreso %2 == 0 or Codigoingreso %10 == 7:
                print("Bienvenido")
            else:
                print("Codigo no cumple con los parametros")
                ingreso=False

# punto3() -- asi se llama un def parra mostrar el codigo. Es decir, no se debe poner de nuevo el "def" y sin ":", esto solo aplica al momento de abrirlo.

#================================
#            punto 4
#================================

# P4. Registro de asistentes

# Crea un ciclo que solicite nombres hasta que se escriba “FIN”. Al finalizar, muestra:

#     El total de nombres ingresados.
#     Si hay nombres repetidos.

# El programa debe ignorar entradas vacías y evitar usar TRY/EXCEPTION pero buscar alternativas para validaciones.

def punto4():
    
    Lista_nombres_guaradada = []
    Lista = True
    while (Lista):
        Nombre_lista = str(input("ingresa el nombre: "))
        if Nombre_lista == "":
            print("No se ha ingresado ningun nombre")
        if Nombre_lista.lower() == "fin":
            print("lista finalizada")
            break

        Lista_nombres_guaradada.append (Nombre_lista)

    Repetidos = {n for n in Lista_nombres_guaradada if Lista_nombres_guaradada.count(n)>1}

    print("Total de nombres ingresado: ", len(Lista_nombres_guaradada))
    print("lista nombres ingresados:", Lista_nombres_guaradada)

    if Repetidos: 
        print("nombre repetidos: ", Repetidos)
    else:
        print("no hay nombres repetidos")
    

#===================
#      punto 5
#===================

# P5. Intentos limitados
# Simula un inicio de sesión con usuario y contraseña predefinidos. Permite hasta tres intentos. Si ambos campos están vacíos, el intento no cuenta. Finaliza al alcanzar el máximo o lograr acceso exitoso. Evalúa cada combinación con operadores lógicos y muestra el motivo del fallo.

def punto5():

    Usuario_real="Riwi"
    Contraseña_real="123456"

    intentos = 0
    maximo_de_intentos = 3

    while intentos < maximo_de_intentos:
        Usuario = input("Cual es tu nombre de usuario?")
        Contraseña = input("Cual es tu contraseña?")

        if Usuario == "" and Contraseña == "":
            print("Por favor ingrese informacion en la casilla")
            continue
        if Usuario == Usuario_real and Contraseña == Contraseña_real:
            print ("Bienvenido")
            break
        else:
            intentos += 1
            print (f"Contraseña incorrecta, intento {intentos}/{maximo_de_intentos}")

            if Usuario != Usuario_real and Contraseña != Contraseña_real:
                print ("Usuario y contraseña incorrectos")
            elif Usuario != Usuario_real:
                print ("Usuario incorrecto")
            elif Contraseña != Contraseña_real:
                print ("Contraseña incorrecta")

    if intentos == maximo_de_intentos:
        print ("superaste tu numero de intentos. Acceso bloqueado")

# ========================
#       punto 6 
# ========================

# Solicita tres números enteros y determina:

#     Si los tres son positivos.
#     Si al menos uno es negativo.
#     Si exactamente uno es cero.

# Debe analizar todas las combinaciones mediante condiciones encadenadas.


def punto6():
    Numero_1 = int(input("Digita el primer numero entero:"))
    Numero_2 = int(input("Digita el segundo numero entero:"))
    Numero_3 = int(input("Digita el tercer numero entero:"))

    if Numero_1 > 0 and Numero_2 > 0 and Numero_3 > 0:
        print ("Los 3 numeros son positivos")

    elif Numero_1 > 0 or Numero_2 > 0 or Numero_3 > 0:
        print ("al menos 1 numero es negativo")

    elif (Numero_1 == 0 and Numero_2 != 0 and Numero_3 != 0) or \
        (Numero_1 == 0 and Numero_2 != 0 and Numero_3 != 0) or \
        (Numero_1 == 0 and Numero_2 != 0 and Numero_3 != 0):
        print ("Exactamente 1 es 0")

    else:
        print ("No cumple ninguna condicion especifica.")

# =====================
#      punto 7
# =====================

# P7. Clasificación de cliente Pide el valor total de una compra y el tipo de membresía. Clasifica al cliente como: Premium → monto alto y membresía activa. Frecuente → monto medio o membresía temporal. Regular → cualquier otro caso. Si el monto es inválido, muestra un mensaje de error.

def punto7():
    #variables

    confirmacion_valor = True

    while (confirmacion_valor):
        try:
            valor_compra =float(input("ingresa el valor de la compra:"))
            confirmacion_valor = False 
        except ValueError:
            print ("Ingrese un valor correcto, solo numeros")
            continue

    #solicitar membresia

    
    valor = True
    while (valor):
        input("ingrese nuevamente un valor positivo")
        if valor_compra <= 0:
            print("inserte un valor correcto, este no puede ser negativo")
            continue
        else:
            valor =False
            
    Membresia_final = True
    
    while (Membresia_final):

        membresia = int(input("""Confirma, por favor tu tipo de membresia:
                      1. activa
                      2. temporal
                      3. ninguna
                    """))
        if valor_compra > 300 and membresia == 1:
            print ("eres un cliente premium")
            Membresia_final = False
        elif 100 <= valor_compra <= 300 and membresia == 2:
            print("eres un usuario frecuente")
            Membresia_final =False
        elif membresia == 3:
            print("eres un usuario regular")
            Membresia_final = False
        else:
            print("Ingresa unicamente opciones validas (1,2,3)")
            
#==========================
#         punto 8
#==========================

# Solicita edad y respuesta a la pregunta: “¿Te gusta programar?” (sí/no). El programa debe repetirse mientras la edad ingresada sea mayor a cero. Al finalizar, muestra cuántas respuestas fueron afirmativas y cuántas negativas. Controla respuestas vacías o incorrectas dentro del ciclo.

def punto8():
    afirmativo = 0
    Negativos = 0
    ask_edad = True
    while (ask_edad):
        edad = input("Cual es tu edad?: ")

        if not edad.isdigit():
            print ("no es una edad valida ingresela solo con numero")   
        edad = int(edad)
        if edad <= 0:  
            print("Encuesta finalizada")
            ask_edad = False
            break
        if edad >= 120:
            print("Ingrese una edad correcta")
            continue
                        
        ask_programar = True
        while (ask_programar):
            programar = input("""Te gustaria programar: 
            1. Si
            2. No    
            """)
            if not programar.isdigit():
                print("ingresa solo numeros 1 o 2")
                continue
            programar =int(programar)

            if programar == 1:
                print("Te contactaremos para mas informacion")
                afirmativo += 1 
                ask_programar = False
            elif programar == 2:
                print ("Gracias por tu respuesta")
                Negativos +=1        
                ask_programar = False        
            else:
                print("Opcion invalida. Selecciona 1 o 2")
                continue
    print("Resultados:")
    print(f"Cantidad de personas que quieren aprender:{afirmativo}")
    print(f"Cantidad de personas que no quieren aprender:{Negativos}")

#================================
#          punto 9
#================================

# Crea un archivo llamado investigacion_bucles.md donde respondas:

    # Diferencias entre un bucle controlado por contador y un bucle controlado por condición.
    # Ejemplos cotidianos que representen el uso de cada tipo de bucle.
    # Cuándo es más apropiado usar while en lugar de for.
    # Qué es un bucle infinito, cómo prevenirlo y cómo detectarlo durante la ejecución.
    # Qué función cumplen las sentencias break y continue dentro de un ciclo.
    # Explica el error lógico más común al usar while y cómo evitarlo.

# El archivo debe incluir títulos, subtítulos y ejemplos descriptivos en formato Markdown.

def punto9():
    try:
        with open("investigacion_bucles.md", "r", encoding="utf8") as file: #UTF-8 es un tipo de codificación de caracteres, es decir, un modo de traducir texto a números para que la computadora lo pueda guardar y leer correctamente.
            contenido = file.read()
            print("Contenido del archivo")
            print (contenido)
            print("Fin del contenido del archivo")

    except FileNotFoundError:
        print("EL archivo de investigacion_bucles.md no se encuentra")

# P10. Panel de control doméstico

# Desarrolla un sistema por consola que simule el control de una vivienda:

#     Menú con opciones para encender luces, activar calefacción, ver estado o salir.
#     Las luces solo pueden encenderse si es de noche.
#     La calefacción solo puede activarse si la temperatura es menor a 18 °C y las luces están encendidas.
#     El sistema debe conservar el estado entre acciones y validar combinaciones imposibles.

# Incluye un diagrama de flujo que muestre la lógica de las condiciones principales.

def punto10():
    horario = 0
    Menu=True
    while (Menu):

        print(""" 
              Menu 

        1. Encender luces
        2. activar calefaccion
        3. Ver estado
        4. Salir 
        """)

        Seleccion_menu = input("Selecciona una de las opciones del menu: ")
        # 1. encender luces
        if not Seleccion_menu.isdigit():
            print("Error: Opcion invalida, solo numeros")
            continue
        Seleccion_menu = int(Seleccion_menu)

        if Seleccion_menu == 1:
            print("1 = dia")
            print("2 = noche")
        
            horario = input("Es de dia o de noche?: ").lower()
        
            if horario ==  "1":
                print("Es dia, no se pueden encender las luces")
                luces_encendidas = False
                continue
            elif horario == "2":
                print("Luces encendidas")
                luces_encendidas = True
                continue
            else:
                ("Error: Opcion invalidad")
        elif Seleccion_menu == 2:
            temperatura = float(input("Cual es la temperatura actual en °C?: "))
            if temperatura < 18 and luces_encendidas:
                print("Calefaccion activada")
            elif temperatura >= 18:
                print("La temperatura es demasiado alta para activar la calefaccion")
            elif not luces_encendidas:
                print("Las luces deben estar encendidas para activar la calefaccion")
        elif Seleccion_menu == 3:
            estado_luces = "encendidas" if luces_encendidas else "apagadas"
            print(f"Estado de las luces: {estado_luces}")
            print(f"Temperatura actual: {temperatura} °C")
        elif Seleccion_menu == 4:
            print("Saliendo del sistema de control domestico.")
            Menu = False
        else:
            print("Error: Opcion invalida, selecciona una opcion del menu.")
punto10()