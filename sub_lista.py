MAGENTA = '\033[35m'
RESET = '\033[39m'
YELLOW = '\033[33m'
import os
class Lista:
    def __init__(self,dimension):
        self.lista=[]
        self.stop=0
        self.dimension=dimension
        
    def append(self,valor):
        if self.stop<self.dimension:
            self.lista+=[valor]
            self.stop+=1
            print(YELLOW+"Agregado con exito")
        else:
            print(MAGENTA+"La lista esta llena")
            
    def obtener(self,pos):
        if pos<0 or self.stop==0:
            print(MAGENTA+"La posicion es invalida o la lista esta vacia por lo cual no se puede obtener nigun valor")
            return None
        elif pos>=self.stop:
            print(MAGENTA+"la posicion no existe porque es mayor que la longitud")
            return None
        elif pos>=0 and pos<self.stop:
            valor=self.lista[pos]
            listanew=self.lista[0:pos]
            for dato in range(pos,self.stop-1):
                listanew=listanew+[self.lista[dato+1]]
            self.stop-=1
            self.lista=listanew
            print(YELLOW+"eliminado con exito")
            return valor
        
    def buscar(self,dato):
        if self.stop>0 and self.stop<=self.dimension:
            for pos,ele in enumerate(self.lista):
                if ele==dato:
                    return pos
            else:
                return None
        else:
            return None
    
    def insertar(self,elemento):
        res=self.buscar(elemento)
        if res!=None:
            print(MAGENTA+"El valor ya se encuentra en la lista, lo cual ya no lo puede volver agregar")
        else:
            self.append(elemento)
        
            
    def eliminar(self,valor):
        res=self.buscar(valor)
        if res==None:
            print("No podemos eliminar porque no se encuentra en la lista")
        else:
            self.obtener(res)
        
    def mostrar(self,alternativa):
        os.system("cls")
        if self.stop==0:
            print("No hay nada que mostrar porque la lista esta vacia")
        else:
            if alternativa.lower()=="a":
                print(MAGENTA+"Se va a presentar de forma ascendente")
                for ele in range(0,self.stop):
                    print(RESET+"[{}]".format(self.lista[ele]))
            else:
                print(MAGENTA+"Se va a presentar de forma descendente")
                for ele in range(self.stop-1,-1,-1):
                    print(RESET+"[{}]".format(self.lista[ele]))
     