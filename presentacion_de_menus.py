import os
MAGENTA = '\033[35m'
RESET = '\033[39m'
YELLOW = '\033[33m'
class menu_principales:
    def __init__(self,titulo,opciones):
        self.menu=titulo
        self.opciones=opciones
        
    def menu_submenus(self):
        print(MAGENTA+self.menu)
        for opcion in self.opciones:
            print(RESET+opcion)
        op=int(input("Elija una opcion [1....{}]: ".format(len(self.opciones))))
        while op>len(self.opciones):
            os.system("cls")
            print(YELLOW+"Opcion invalida")
            for opcion in self.opciones:
                print(RESET+opcion)
            op=int(input("La opcion no existes o es invalida\nElija otra opcion [1....{}]: ".format(len(self.opciones))))
        return op