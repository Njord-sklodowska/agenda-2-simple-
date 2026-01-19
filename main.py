from menu import agregar_persona , borrar_persona , mostrar_personas
while True:
    print("Menu: 1- agregar , 2- eliminar , 3- ver contactos , 4- salir")
    button_menu = input("elegi que opcion desea realizar \n")
    if button_menu == "1":
        agregar_persona()
    elif button_menu == "2":
        borrar_persona()
    elif button_menu =="3":
        mostrar_personas()
    elif button_menu == "4":
        print("saliendo de aplicacion adios!!")
        break