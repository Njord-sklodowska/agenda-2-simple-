# importamos time aqui porque desde aqui se va a utilizar
import time

# desde persona importamos la clase Persona ---
# de esta menra se refiere menu conoce a Persona pero Persona no conoce a menu
# de esta manera podemos reutilizar en otros proyectos a la clase Persona
from persona import Persona
personas = [] # creamos una lista donde se alojan los datos de cada objeto creado

# otra funcion para empezar a agregar cada objeto que creamos    
def agregar_persona():
        while True:
            try:
                nombre =input("ingresa el nombre \n")
                apellido =input("ingresa el apellido \n")
                telefono =input("ingresa el numero \n")
                persona = Persona(nombre, apellido, telefono)
                personas.append(persona)
                time.sleep(1)
                print("  ")
                print("persona agregada correctamente !!!")
                print("  ")
                break

            except ValueError as error:
                print("no se ingreso uno de los datos.. ingresa de nuevo")

# funcion para la opcion mostrar contactos 
# y como se va a mostrar en caso de que no exista alguno...
def mostrar_personas():
    if not personas:
        print("no hay personas")
        return
    print("======================================")
    print("Contactos: \n")
    for i, p in enumerate(personas, start=1):
        print(f"{i}. {p.nombre} {p.apellido} - tel: {p.tel}")
    print()

# funcion de eliminacion de contacto
def borrar_persona():
    if not personas:
        print("no hay personas a borrar")
        return
    mostrar_personas() #llama a la funcion mostrar persona para visualizar contactos....
    try:
        delete= int(input("elegi el numero de la persona que queres borrar"))
        delete = personas.pop(delete - 1)
        print("borrando contacto")
        time.sleep(1)
        print("contacto eliminado...")
    except (ValueError , IndexError) :
        print("opcion invalida!")