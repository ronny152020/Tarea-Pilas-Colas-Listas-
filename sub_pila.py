MAGENTA = '\033[35m'
RESET = '\033[39m'
YELLOW = '\033[33m'
class pila:
    def __init__(self,cantidadele):
        self.pila=[]
        self.limit=0
        self.limite=cantidadele
        
    def push(self,valor):
        if self.limit<self.limite:
            self.pila+=[valor]
            self.limit+=1
            print(YELLOW+"Se ha agregado el elemento con exito")
        else:
            print(MAGENTA+"La Pila ya se encuentra llena")
    
    def pop(self):
        if self.limit==0:
            print(MAGENTA+"No se puede eliminar ningun elemento, debido a que la Pila se encuentra esta vacia")
        else:
            self.pila=self.pila[:-1]
            self.limit-=1
            print(YELLOW+"Se ha eliminado con exito el último elemento de la Pila")
   
    def show(self):
        if self.limit>0:
            for datos in range(self.limit-1,-1,-1):
                print("[{}]".format(self.pila[datos]))
        else:
            print(MAGENTA+"No hay elementos que presentar, porque la Pila se encuentra vacía")
    
    def empty(self):
        print("Se comprobará si la Pila esta vacía")
        if self.limit==0:
            print(YELLOW+"La Pila se encuentra vacía")
        else:
            print(YELLOW+"La Pila si tiene elementos dentro")
     
    def longitud(self):
        print(YELLOW+"La longitud de la Pila es de {}".format(self.limit))
        