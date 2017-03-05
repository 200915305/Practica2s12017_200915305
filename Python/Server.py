from flask import Flask, request, Response
import subprocess
app = Flask("Practica2")

#**************************Nodo Lista Simple...
class Nodo:

    def __init__(self, info):
        self.Info = info
        self.sig = None



#**************************Lista Simple...
class ListaD:


    def __init__(self, *elem):
        self.primeroL = None
        self.ultimoL = None
        self.Actual = None
        self.contar=0



    def insertar(self, *elem):


        for i in elem:

            nodo = Nodo(i)
            if (self.ultimoL != None):
                self.ultimoL.sig = nodo
                self.Actual = self.ultimoL
                self.contar+=1
            else:
                self.primeroL = nodo
                self.contar += 1
            self.ultimoL = nodo

    def eliminar(self, elem):
        self.contare=0
        if elem==0:
            self.primeroL=self.primeroL.sig
        else:
            aux=self.primeroL
            anterior=aux
            while aux!=None:

                if elem==self.contare:
                    anterior.sig=aux.sig
                anterior=aux
                aux=aux.sig
                self.contare += 1

    def Buscar(self,elem):
        nodo=self.primeroL
        print "************Mostrar Lista*************"

        while nodo!=None:
            if nodo.Info ==elem:
                print "elemento>>>",nodo.Info
                return nodo.Info
            nodo=nodo.sig

    def mostrar(self):
        nodo = self.primeroL
        while (nodo != None):
            print nodo.Info,
            nodo = nodo.sig
        print

    def Gragficar(self):
        Archivo = open('C:\Users\Administrador\Desktop\Python\Lista_simple.dot', 'w')

        Grafo_dot = "digraph ListaSimple{\nlabel = \"Lista Simple\"\n\n"
        nodo = self.primeroL

        Indice = 0
        while (nodo != None):
            Grafo_dot += "\tNode" + str(Indice) + "[label = \"" + nodo.Info + "\"];\n"
            nodo = nodo.sig
            Indice = Indice + 1
        Grafo_dot += "\n"
        nodo = self.primeroL
        Indice = 0
        while (nodo.sig != None):
            Grafo_dot += "\tNode" + str(Indice) + " -> Node" + str(Indice + 1) + ";\n"
            nodo = nodo.sig
            Indice = Indice + 1
        Grafo_dot += "}"
        Archivo.write(Grafo_dot)
        Archivo.close()
        subprocess.call(
            ['dot', 'C:\Users\Administrador\Desktop\Python\Lista_simple.dot', '-o', 'C:\Users\Administrador\Desktop\Python\Lista_simple.png',
             '-Tpng', '-Gcharset=utf8'])

lista = ListaD()

"""""
lista.insertar("a")
lista.insertar("b")
lista.insertar("c")
lista.insertar("d")
lista.insertar("e")
lista.insertar("f")
lista.mostrar()
lista.eliminar(4)
lista.mostrar()
lista.Buscar("c")
lista.Gragficar()
"""""

#*******************************Nodo Cola...
class NodoCola():
    def __init__(self, dato):
        self.dato=dato
        self.sig=None


#*********************************Cola...
class Cola():
    def __init__(self):
        self.primero=None
        self.ultimo=None

    def vacia(self):
         return self.primero==None

    def AgregarCola(self,dato):
        if self.vacia()==True:
            self.primero=self.ultimo=NodoCola(dato)
        else:
            aux=NodoCola(dato)
            aux.sig=self.primero
            self.primero=aux

    def EliminarUltimo(self):
        aux =self.primero
        while aux.sig != self.ultimo:
            aux=aux.sig
        print "salio>>",aux.sig.dato
        aux2=aux.sig.dato
        aux.sig=None
        self.ultimo=aux
        return aux2

    def mostrarCola(self):
        aux=self.primero
        print "************Mostrar Cola*************"
        while aux!= None:
            print aux.dato
            aux=aux.sig


    def GragficarCola(self):
        Archivo = open('C:\Users\Administrador\Desktop\Python\Cola.dot', 'w')
        Grafo_dot = "digraph Cola{\nlabel = \"Cola\"\n\n"
        temp=self.primero

        Indice = 0
        while (temp != None):
            Grafo_dot += "\tNode" + str(Indice) + "[label = \"" + str(temp.dato) + "\"];\n"
            temp = temp.sig
            Indice = Indice + 1
        Grafo_dot += "\n"
        temp = self.primero
        Indice = 0
        while (temp.sig != None):
            Grafo_dot += "\tNode" + str(Indice) + " -> Node" + str(Indice + 1) + ";\n"
            temp = temp.sig
            Indice = Indice + 1
        Grafo_dot += "}"
        Archivo.write(Grafo_dot)
        Archivo.close()
        subprocess.call(
            ['dot', 'C:\Users\Administrador\Desktop\Python\Cola.dot', '-o', 'C:\Users\Administrador\Desktop\Python\Cola.png',
             '-Tpng', '-Gcharset=utf8'])



cola=Cola()
"""""
cola.AgregarCola(1)
cola.AgregarCola(2)
cola.AgregarCola(3)
cola.AgregarCola(4)
cola.AgregarCola(5)
cola.AgregarCola(6)

cola.mostrarCola()
cola.GragficarCola()
cola.EliminarUltimo()
cola.GragficarCola()
cola.mostrarCola()
cola.EliminarUltimo()
cola.mostrarCola()
cola.EliminarUltimo()
cola.mostrarCola()
cola.EliminarUltimo()
cola.mostrarCola()
"""
#************************************Nodo Pila....
class NodoPila():
    def __init__(self,dato):
        self.dato=dato
        self.sigP=None

#************************************Pila....
class Pila():
    def __init__(self):
        self.primeroP=None
        self.ultimoP=None

    def vaciaP(self):
        return self.primeroP==None

    def AgreparPila(self,dato):
        if self.vaciaP() == True:
            self.primeroP = self.ultimoP = NodoPila(dato)
        else:
            aux = NodoPila(dato)
            aux.sigP = self.primeroP
            self.primeroP = aux



    def MostrarPila(self):
        aux=self.primeroP
        print "************Mostrar Pila*************"
        while aux != None:
            print aux.dato
            aux=aux.sigP

    def EliminarPrimero(self):
        aux=self.primeroP
        self.primeroP=self.primeroP.sigP
        return aux.dato

    def GraficarPila(self):
        Archivo = open('C:\Users\Administrador\Desktop\Python\Pila.dot', 'w')
        Grafo_dot = "digraph Pila{\nlabel = \"Pila\"\n\n"
        temp = self.primeroP

        Indice = 0
        while (temp != None):
            Grafo_dot += "\tNode" + str(Indice) + "[label = \"" + str(temp.dato) + "\"];\n"
            temp = temp.sigP
            Indice = Indice + 1
        Grafo_dot += "\n"
        temp = self.primeroP
        Indice = 0
        while (temp.sigP != None):
            Grafo_dot += "\tNode" + str(Indice) + " -> Node" + str(Indice + 1) + ";\n"
            temp = temp.sigP
            Indice = Indice + 1
        Grafo_dot += "}"
        Archivo.write(Grafo_dot)
        Archivo.close()
        subprocess.call(
            ['dot', 'C:\Users\Administrador\Desktop\Python\Pila.dot', '-o', 'C:\Users\Administrador\Desktop\Python\Pila.png',
             '-Tpng', '-Gcharset=utf8'])


pila = Pila()
"""""
pila.AgreparPila(1)
pila.AgreparPila(2)
pila.AgreparPila(3)
pila.AgreparPila(4)
pila.AgreparPila(5)
pila.AgreparPila(6)
pila.AgreparPila(7)
pila.AgreparPila(8)
pila.GraficarPila()
pila.MostrarPila()
pila.EliminarPrimero()
pila.MostrarPila()
"""
#********************************************Matriz Dispersa...








#********************************************Consumir Servidor....


@app.route('/AgregarLista', methods=['POST'])
def AgregarLista():
    parametro = str(request.form['dato'])
    lista.insertar(str(parametro))
    lista.Gragficar()
    return "Se Agrego " + str(parametro) + "!"


@app.route('/EliminarLista', methods=['POST'])
def EliminarLista():
    parametro = str(request.form['indice'])
    lista.eliminar(int(parametro))
    lista.Gragficar()
    return "Se Elimino " + str(parametro) + "!"

@app.route('/BuscarLista', methods=['POST'])
def BuscarLista():
    parametro = str(request.form['buscar'])
    dato= lista.Buscar(str(parametro))
    if dato==None:
        return "El Dato no se Encontro en la Lista"
    else:
        return "El Dato q se Encontro en la Lista es>>>"+dato
    lista.Gragficar()

@app.route('/AgregarCola', methods=['POST'])
def AgregarCola():
    parametro = str(request.form['datoc'])
    cola.AgregarCola(str(parametro))
    cola.GragficarCola()
    return "Se Agrego a la Cola " + str(parametro) + "!"

@app.route('/QuitarCola', methods=['POST'])
def QuitarCola():
    parametro = str(request.form['cola'])
    cola2=cola.EliminarUltimo()
    cola.GragficarCola()
    return "El dato que salio de la Cola es>>>> " + cola2 + "!"

@app.route('/AgregarPila', methods=['POST'])
def AgregarPila():
    parametro = str(request.form['pila'])
    pila.AgreparPila(str(parametro))
    pila.GraficarPila()
    return "Se Agrego a la Pila " + str(parametro) + "!"

@app.route('/SacarPila', methods=['POST'])
def SacarPila():
    parametro = str(request.form['pila'])
    pila2=pila.EliminarPrimero()
    pila.GraficarPila()
    return "El dato que salio de la Pila es>>>> " + pila2 + "!"

@app.route("/")
def hellof():
    return "***Servidor Flask y Python***"


if __name__ == "__main__":
    app.run()
