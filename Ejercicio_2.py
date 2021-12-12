class Nodo:
    def __init__(self,nombre,telefono):
        self.nombre = nombre
        self.telefono = telefono
        self.siguiente = None

class Lista:
    def __init__(self):
        self.head = None
        self.Size = 0

    def listar(self, nombre, telefono):
        nodo = Nodo(nombre, telefono)
        if self.Size == 0:
            self.head = nodo
        else:
            Current = self.head
            while Current.siguiente != None:
                Current = Current.siguiente
            Current.siguiente = nodo        
        self.Size += 1
        return nodo


    def mostrar(self):
        if self.head is None:
            print("La agenda esta vacía")
            return
        else:
            n = self.head
            while n is not None:
                print(n.nombre," ",n.telefono," ")
                n = n.siguiente

Contactos = Lista()

Salir = False
opcion = 0

while not Salir:
    print("------------ Agenda Telefonica--------")
    print("1. Ingreso de Datos")
    print("2. Mostar Dtos")
    print("3. Salir")
    print("--------------------------------------")

    menu = (input("Opcion: "))
    if menu.isdigit():
        menu = int(menu)
        if menu == 1:
            nombre = input("Ingrese el nombre: ")
            telefono = input("Ingrese el numero: ")
            Contactos.listar(nombre, telefono)
        elif menu == 2:
            Contactos.mostrar()
        elif menu == 3:
            exit()
    else:
            print("Debe ingresar una opcion valida ")

