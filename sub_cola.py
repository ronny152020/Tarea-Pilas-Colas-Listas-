MAGENTA = '\033[35m'
RESET = '\033[39m'
YELLOW = '\033[33m'
class cola:
    def __init__(self,cantidadter):
        self.cola=[]
        self.stop=0
        self.limit=cantidadter
        
    def push(self,valor):
        if self.stop<self.limit:
            self.cola+=[valor]
            self.stop+=1
            print(YELLOW+"Agregado con exito")
        else:
            print(MAGENTA+"La COLA ya esta llena")
    
    def pop(self):
        if self.stop==0:
            print(MAGENTA+"No podemos eliminar ningun dato, porque la cola esta vacia")
        else:
            self.cola=self.cola[1:]
            self.stop-=1
            print(YELLOW+"Eliminado con exito")
    
    def empty(self):
        print(MAGENTA+"Verificaremos si la COLA esta vacia")
        if self.stop==0:
            print(YELLOW+"La cola esta vacia")
        else:
            print(YELLOW+"la cola si tiene valores")
        
    def show(self):
        if self.stop>0:
            for datos in range(0,self.stop):
                print("[{}]".format(self.cola[datos]))
        else:
            print(MAGENTA+"No hay nada que presentar, porque la cola esta vacia")
    
    def longitud(self):
        print(YELLOW+"La longitud de la cola es {}".format(self.stop))