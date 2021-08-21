from sub_pila import pila
from presentacion_de_menus import menu_principales
from sub_cola import cola
from sub_lista import Lista
import os
MAGENTA = '\033[35m'
RESET = '\033[39m'
YELLOW = '\033[33m'
opcion=""
while opcion!=4:
    presentacion=menu_principales("MENU PRINCIPAL",["1.- Pilas","2.- Colas","3.- Listas","4.- Salir"])
    opcion=presentacion.menu_submenus()
    os.system("cls")
    if opcion==1:
        tamaño=int(input("Ingrese el tamaño con que quiere trabajar la PILA: "))
        pilauso=pila(tamaño)
        os.system("cls")
        oppila=""
        while oppila!=6:
            os.system("cls")
            presentacion=menu_principales("SubMenu PILA",["1.- Push (agregar valores)","2.- Pop (eliminar valor)","3.- Show (presentar actual pila)","4.- empty (verificar si existe pila vacia)","5.- Longitud (identidicar longitud de la PILA)","6.- Salir"])
            oppila=presentacion.menu_submenus()
            os.system("cls")
            if oppila==1:
                valor=str(input("Ingrese el valor que desea agregar a la PILA: "))
                pilauso.push(valor)
                input(RESET+"presione cualquier tecla para continuar...")
            elif oppila==2:
                pilauso.pop()
                input(RESET+"presione cualquier tecla para continuar...")
            elif oppila==3:
                pilauso.show()
                input(RESET+"presione cualquier tecla para continuar...")
            elif oppila==4:
                pilauso.empty()
                input(RESET+"presione cualquier tecla para continuar...")
            elif oppila==5:
                pilauso.longitud()
                input(RESET+"presione cualquier tecla para continuar...")
    elif opcion==2:
        tamaño=int(input("Ingrese el tamaño que desea que sea la cola: "))
        colauso=cola(tamaño)
        os.system("cls")
        opcola=""
        while opcola!=6:
            os.system("cls")
            presentacion=menu_principales("SUBMENU COLA",["1.- Push (agregar valor)","2.- Pop (eliminar valor)","3.- Show (presentar actual COLA)","4.- empty (verificar si existe COLA vacia)","5.- Longitud (identidicar longitud de la COLA)","6.- Salir"])
            opcola=presentacion.menu_submenus()
            os.system("cls")
            if opcola==1:
                valor=str(input("Ingrese el valor que desea agregar a la COLA: "))
                colauso.push(valor)
                input(RESET+"presione cualquier tecla para continuar...")
            elif opcola==2:
                colauso.pop()
                input(RESET+"presione cualquier tecla para continuar...")
            elif opcola==3:
                colauso.show()
                input(RESET+"presione cualquier tecla para continuar...")
            elif opcola==4:
                colauso.empty()
                input(RESET+"presione cualquier tecla para continuar...")
            elif opcola==5:
                colauso.longitud()
                input(RESET+"presione cualquier tecla para continuar...")
    elif opcion==3:
        tamaño=int(input("Ingrese el tamaño que desea que sea la LISTA: "))
        listauso=Lista(tamaño)
        os.system("cls")
        oplista=""
        while oplista!=7:
            os.system("cls")
            presentacion=menu_principales("SUBMENU LISTA",["1.- append (agregar valor)","2.- obtener (eliminar valor)","3.- buscar (buscar un valor y identificar su posicion)","4.- insertar (agregar un valor si no existe en la lista)","5.- eliminar (eliminar un valor si existe en la lista)","6.- mostrar (presentar lista actual de forma asc o des","7.- Salir"])
            oplista=presentacion.menu_submenus()
            os.system("cls")
            if oplista==1:
                valor=str(input("Ingrese el valor que desea agregar a la lista: "))
                listauso.append(valor)
                input(RESET+"presione cualquier tecla para continuar...")
            elif oplista==2:
                posicion=int(input("Ingrese la posicion que desea eliminar un valor" ))
                listauso.obtener(posicion)
                input(RESET+"presione cualquier tecla para continuar...")
            elif oplista==3:
                dato=str(input("Ingrese el valor que desea buscar en la lista: "))
                if listauso.buscar(dato)!=None:
                    print("El valor se encuentra en la posicion {}".format(listauso.buscar(dato)))
                else:
                    print("El valor no se encuentra")
                input(RESET+"presione cualquier tecla para continuar...")
            elif oplista==4:
                elemento=str(input("Ingrese el dato que desea agregar a la lista: "))
                listauso.insertar(elemento)
                input(RESET+"presione cualquier tecla para continuar...")
            elif oplista==5:
                valor=str(input("Ingrese el dato que desea eliminar de la lista: "))
                listauso.eliminar(valor)
                input(RESET+"presione cualquier tecla para continuar...")
            elif oplista==6:
                alt=str(input(YELLOW+"¿De que forma quiere que se muestre la lista\nDe forma ascendente(ingrese la letra (A/a) para este caso)\no de forma descendente(ingrese un caracter diferente para este caso)\n"))
                listauso.mostrar(alt)
                input(RESET+"presione cualquier tecla para continuar...")
print(YELLOW+"Muchas gracias, tenga un buen dia")