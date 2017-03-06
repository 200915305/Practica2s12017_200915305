from flask import Flask, request, Response
import subprocess

app = Flask("Practica2")


# **************************Nodo Lista Simple...
class Nodo:
    def __init__(self, info):
        self.Info = info
        self.sig = None


# **************************Lista Simple...
class ListaD:
    def __init__(self, *elem):
        self.primeroL = None
        self.ultimoL = None
        self.Actual = None
        self.contar = 0

    def insertar(self, *elem):

        for i in elem:

            nodo = Nodo(i)
            if (self.ultimoL != None):
                self.ultimoL.sig = nodo
                self.Actual = self.ultimoL
                self.contar += 1
            else:
                self.primeroL = nodo
                self.contar += 1
            self.ultimoL = nodo

    def eliminar(self, elem):
        self.contare = 0
        if elem == 0:
            self.primeroL = self.primeroL.sig
        else:
            aux = self.primeroL
            anterior = aux
            while aux != None:

                if elem == self.contare:
                    anterior.sig = aux.sig
                anterior = aux
                aux = aux.sig
                self.contare += 1

    def Buscar(self, elem):
        nodo = self.primeroL
        print "************Mostrar Lista*************"

        while nodo != None:
            if nodo.Info == elem:
                print "elemento>>>", nodo.Info
                return nodo.Info
            nodo = nodo.sig

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
            ['dot', 'C:\Users\Administrador\Desktop\Python\Lista_simple.dot', '-o',
             'C:\Users\Administrador\Desktop\Python\Lista_simple.png',
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


# *******************************Nodo Cola...
class NodoCola():
    def __init__(self, dato):
        self.dato = dato
        self.sig = None


# *********************************Cola...
class Cola():
    def __init__(self):
        self.primero = None
        self.ultimo = None

    def vacia(self):
        return self.primero == None

    def AgregarCola(self, dato):
        if self.vacia() == True:
            self.primero = self.ultimo = NodoCola(dato)
        else:
            aux = NodoCola(dato)
            aux.sig = self.primero
            self.primero = aux

    def EliminarUltimo(self):
        aux = self.primero
        while aux.sig != self.ultimo:
            aux = aux.sig
        print "salio>>", aux.sig.dato
        aux2 = aux.sig.dato
        aux.sig = None
        self.ultimo = aux
        return aux2

    def mostrarCola(self):
        aux = self.primero
        print "************Mostrar Cola*************"
        while aux != None:
            print aux.dato
            aux = aux.sig

    def GragficarCola(self):
        Archivo = open('C:\Users\Administrador\Desktop\Python\Cola.dot', 'w')
        Grafo_dot = "digraph Cola{\nlabel = \"Cola\"\n\n"
        temp = self.primero

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
            ['dot', 'C:\Users\Administrador\Desktop\Python\Cola.dot', '-o',
             'C:\Users\Administrador\Desktop\Python\Cola.png',
             '-Tpng', '-Gcharset=utf8'])


cola = Cola()
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


# ************************************Nodo Pila....
class NodoPila():
    def __init__(self, dato):
        self.dato = dato
        self.sigP = None


# ************************************Pila....
class Pila():
    def __init__(self):
        self.primeroP = None
        self.ultimoP = None

    def vaciaP(self):
        return self.primeroP == None

    def AgreparPila(self, dato):
        if self.vaciaP() == True:
            self.primeroP = self.ultimoP = NodoPila(dato)
        else:
            aux = NodoPila(dato)
            aux.sigP = self.primeroP
            self.primeroP = aux

    def MostrarPila(self):
        aux = self.primeroP
        print "************Mostrar Pila*************"
        while aux != None:
            print aux.dato
            aux = aux.sigP

    def EliminarPrimero(self):
        aux = self.primeroP
        self.primeroP = self.primeroP.sigP
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
            ['dot', 'C:\Users\Administrador\Desktop\Python\Pila.dot', '-o',
             'C:\Users\Administrador\Desktop\Python\Pila.png',
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


# ********************************************Matriz Dispersa...

#*********************************************NodoMatriz...
class NodoMatriz(object):
    def __init__(self, valor=None, letra=None, dominio=None, sig=None, ant=None, arriba=None, abajo=None):
        self.sig = sig
        self.ant = ant
        self.arriba = arriba
        self.abajo = abajo
        self.valor = valor
        self.letra = letra
        self.dominio = dominio

    def getValor(self):
        return self.valor

    def setValor(self, dato):
        self.valor = dato

    def getSiguiente(self):
        return self.sig

    def setSiguiente(self, dato):
        self.sig = dato

    def getAnterior(self):
        return self.ant

    def setAnterior(self, dato):
        self.ant = dato

    def getArriba(self):
        return self.arriba

    def setArriba(self, dato):
        self.arriba = dato

    def getAbajo(self):
        return self.abajo

    def setAbajo(self, dato):
        self.abajo = dato

    def getLetra(self):
        return self.letra

    def setLetra(self, dato):
        self.letra = dato

    def getDominio(self):
        return self.dominio

    def setDominio(self, dato):
        self.dominio = dato


#*********************************************Nodo Dominio......
class NodoDominio(object):
    def __init__(self, valor=None, letra=None, dominio=None, siguiente=None, anterior=None, arriba=None, abajo=None):
        self.siguiente = siguiente
        self.anterior = anterior
        self.arriba = arriba
        self.abajo = abajo
        self.dato = valor
        self.letra = letra
        self.dominio = dominio

    def getSiguiente(self):
        return self.siguiente

    def setSiguiente(self, valorAux):
        self.siguiente = valorAux

    def getAnterior(self):
        return self.anterior

    def setAnterior(self, valorAux):
        self.anterior = valorAux

    def getArriba(self):
        return self.arriba

    def setArriba(self, valorAux):
        self.arriba = valorAux

    def getAbajo(self):
        return self.abajo

    def setAbajo(self, valorAux):
        self.abajo = valorAux

    def setValor(self, dato):
        self.dato = dato

    def getValor(self):
        return self.dato

    def getPrimero(self):
        return self.primero

    def setPrimero(self, primero):
        self.primero = primero

    def getUltimo(self):
        return self.ultimo

    def setUltmio(self, ultimo):
        return self.ultimo

    def getLetra(self):
        return self.letra

    def setLetra(self, valorAux):
        self.letra = valorAux

    def getDominio(self):
        return self.dominio

    def setDominio(self, valorAux):
        self.dominio = valorAux


#*********************************************NodoLetra.................
class NodoLetra(object):
    def __init__(self, valor=None, letra=None, dominio=None, siguiente=None, anterior=None, arriba=None, abajo=None):
        self.siguiente = siguiente
        self.anterior = anterior
        self.arriba = arriba
        self.abajo = abajo
        self.dato = valor
        self.letra = letra
        self.dominio = dominio

    def setSiguiente(self, valorAux):
        self.siguiente = valorAux

    def getSiguiente(self):
        return self.siguiente

    def getAnterior(self):
        return self.anterior

    def setAnterior(self, valorAux):
        self.anterior = valorAux

    def setValor(self, dato):
        self.dato = dato

    def setAbajo(self, abajo):
        self.abajo = abajo

    def setArriba(self, arriba):
        self.arriba = arriba

    def getAbajo(self):
        return self.abajo

    def getArriba(self):
        return self.arriba

    def getValor(self):
        return self.dato

    def getPrimero(self):
        return self.primero

    def setPrimero(self, primero):
        self.primero = primero

    def getUltimo(self):
        return self.ultimo

    def setUltmio(self, ultimo):
        return self.ultimo

    def getLetra(self):
        return self.letra

    def setLetra(self, valorAux):
        self.letra = valorAux

    def getDominio(self):
        return self.dominio

    def setDominio(self, valorAux):
        self.dominio = valorAux


#*********************************************Nombres....



class Nombres(object):
    def __init__(self):
        self.primero = None
        self.ultimo = None
        self.tamano = 0

    def vacio(self):
        if self.tamano == 0:
            return True
        else:
            return False

    def insertar(self, insertar):
        nuevo = NodoDominio(insertar)

        if self.vacio() == True:
            self.primero = nuevo
            self.ultimo = nuevo

        else:

            InsertarLetra = insertar[:1]
            InsertarLetra = ord(InsertarLetra)

            agregado = False
            Auxiliar = self.primero

            while Auxiliar != None:
                letracomparar = Auxiliar.getValor()[:1]
                letracomparar = ord(letracomparar)

                if InsertarLetra > letracomparar:
                    Auxiliar = Auxiliar.getSiguiente()
                else:
                    if Auxiliar == self.primero:
                        nuevo.setSiguiente(Auxiliar)
                        Auxiliar.setAnterior(nuevo)
                        self.primero = nuevo
                        agregado = True
                        break
                    else:

                        nuevo.setAnterior(Auxiliar.getAnterior())
                        Auxiliar.getAnterior().setSiguiente(nuevo)

                        nuevo.setSiguiente(Auxiliar)
                        Auxiliar.setAnterior(nuevo)
                        agregado = True
                        break
            if agregado == False:
                self.ultimo.setSiguiente(nuevo)
                nuevo.setAnterior(self.ultimo)
                self.ultimo = nuevo

        self.tamano = self.tamano + 1

    def getTamano(self):
        return self.tamano

    def buscar(self, valor):
        if self.vacio() == False:
            aux = self.primero
            while aux != None:
                if aux.getValor() == valor:
                    return aux
                aux = aux.getSiguiente()
        else:
            return None

    def getPrimero(self):
        return self.primero

    def setPrimero(self, primero):
        self.primero = primero

    def getUltimo(self):
        return self.ultimo

    def setUltmio(self, ultimo):
        return self.ultimo

    def eliminar(self, dato):
        if self.vacio() == False:
            nodoaux = self.primero

            while nodoaux != None:
                if nodoaux.getValor() == dato:
                    if nodoaux == self.primero:
                        if nodoaux.getSiguiente() != None:
                            self.primero = nodoaux.getSiguiente()
                            nodoaux = nodoaux.getSiguiente().setAnterior(None)
                            self.tamano = self.tamano - 1

                        else:
                            self.setUltmio(None)
                            self.setPrimero(None)
                            self.tamano = 0

                        break
                    elif nodoaux == self.getUltimo():
                        if nodoaux.getAnterior() != None:
                            self.ultimo = nodoaux.getAnterior()
                            nodoaux = nodoaux.getAnterior().setSiguiente(None)
                            self.tamano = self.tamano - 1
                        else:
                            self.setPrimero(None)
                            self.setUltmio(None)
                            self.tamano = 0

                        break
                    else:
                        nodoaux.getAnterior().setSiguiente(nodoaux.getSiguiente())
                        nodoaux.getSiguiente().setAnterior(nodoaux.getAnterior())
                        self.tamano = self.tamano - 1

                        break
                else:
                    nodoaux = nodoaux.getSiguiente()

#*********************************************Dominiosss..........



class Dominio(object):
    def __init__(self):
        self.primero = None
        self.ultimo = None
        self.tamano = 0

    def vacio(self):
        if self.tamano == 0:
            return True
        else:
            return False

    def insertar(self, insertar):
        nuevo = NodoDominio(insertar)

        if self.vacio() == True:
            self.primero = nuevo
            self.ultimo = nuevo

        else:

            InsertarLetra = insertar[:1]
            InsertarLetra = ord(InsertarLetra)

            agregado = False
            Auxiliar = self.primero

            while Auxiliar != None:
                letracomparar = Auxiliar.getValor()[:1]
                letracomparar = ord(letracomparar)

                if InsertarLetra > letracomparar:
                    Auxiliar = Auxiliar.getSiguiente()
                else:
                    if Auxiliar == self.primero:
                        nuevo.setSiguiente(Auxiliar)
                        Auxiliar.setAnterior(nuevo)
                        self.primero = nuevo
                        agregado = True
                        break
                    else:

                        nuevo.setAnterior(Auxiliar.getAnterior())
                        Auxiliar.getAnterior().setSiguiente(nuevo)

                        nuevo.setSiguiente(Auxiliar)
                        Auxiliar.setAnterior(nuevo)
                        agregado = True
                        break
            if agregado == False:
                self.ultimo.setSiguiente(nuevo)
                nuevo.setAnterior(self.ultimo)
                self.ultimo = nuevo

        self.tamano = self.tamano + 1

    def buscar(self, valor):
        if self.vacio() == False:
            aux = self.primero
            while aux != None:
                if aux.getValor() == valor:
                    return aux
                aux = aux.getSiguiente()
        else:
            return None

    def getPrimero(self):
        return self.primero

    def setPrimero(self, primero):
        self.primero = primero

    def getUltimo(self):
        return self.ultimo

    def setUltmio(self, ultimo):
        return self.ultimo

    def eliminar(self, dato):
        if self.vacio() == False:
            nodoaux = self.primero

            while nodoaux != None:

                if nodoaux.getValor() == dato:

                    if nodoaux == self.primero:

                        if nodoaux.getSiguiente() != None:
                            self.primero = nodoaux.getSiguiente()
                            nodoaux.getSiguiente().setAnterior(None)
                            self.tamano = self.tamano - 1

                        else:
                            self.ultimo = (None)
                            self.primero = (None)
                            self.tamano = 0

                        break
                    elif nodoaux == self.getUltimo():

                        if nodoaux.getAnterior() != None:
                            self.ultimo = nodoaux.getAnterior()
                            nodoaux.getAnterior().setSiguiente(None)
                            self.tamano = self.tamano - 1
                        else:
                            self.primero = (None)
                            self.ultimo = (None)
                            self.tamano = 0

                        break
                    else:
                        nodoaux.getAnterior().setSiguiente(nodoaux.getSiguiente())
                        nodoaux.getSiguiente().setAnterior(nodoaux.getAnterior())
                        self.tamano = self.tamano - 1

                        break
                else:
                    nodoaux = nodoaux.getSiguiente()



#**********************************************Letras..............




class Letras(object):
    def __init__(self):
        self.primero = None
        self.ultimo = None
        self.tamano = 0

    def vacio(self):
        if self.tamano == 0:
            return True
        else:
            return False

    def insertar(self, insertar):
        if self.vacio():
            self.insertarPrimero(insertar)
        else:
            self.insertarotro(insertar)

        self.tamano = self.tamano + 1

    def insertarPrimero(self, insertar):
        nuevo = NodoLetra(insertar)
        self.primero = nuevo
        self.ultimo = nuevo

    def insertarotro(self, insertar):
        nuevo = NodoLetra(insertar)

        if self.vacio() == True:
            self.primero = nuevo
            self.ultimo = nuevo

        else:

            InsertarLetra = insertar[:1]
            InsertarLetra = ord(InsertarLetra)

            agregado = False
            Auxiliar = self.primero

            while Auxiliar != None:
                letracomparar = Auxiliar.getValor()[:1]
                letracomparar = ord(letracomparar)

                if InsertarLetra > letracomparar:
                    Auxiliar = Auxiliar.getAbajo()
                else:
                    if Auxiliar == self.primero:
                        nuevo.setAbajo(Auxiliar)
                        Auxiliar.setArriba(nuevo)
                        self.primero = nuevo
                        agregado = True
                        break
                    else:

                        nuevo.setArriba(Auxiliar.getArriba())
                        Auxiliar.getArriba().setAbajo(nuevo)

                        nuevo.setAbajo(Auxiliar)
                        Auxiliar.setArriba(nuevo)
                        agregado = True
                        break
            if agregado == False:
                self.ultimo.setAbajo(nuevo)
                nuevo.setArriba(self.ultimo)
                self.ultimo = nuevo

        self.tamano = self.tamano + 1

    def buscar(self, valor):
        if self.vacio() == False:
            aux = self.primero
            while aux != self.ultimo.getAbajo():
                if aux.getValor() == valor:
                    return aux
                aux = aux.getAbajo()
        else:
            return None

    def getPrimero(self):
        return self.primero

    def setPrimero(self, primero):
        self.primero = primero

    def getUltimo(self):
        return self.ultimo

    def setUltmio(self, ultimo):
        return self.ultimo

    def eliminar(self, dato):
        if self.vacio() == False:
            nodoaux = self.primero

            while nodoaux != None:
                if nodoaux.getValor() == dato:
                    if nodoaux == self.primero:
                        if nodoaux.getAbajo() != None:
                            self.primero = nodoaux.getAbajo()
                            nodoaux.getAbajo().setArriba(None)
                            self.tamano = self.tamano - 1

                        else:
                            self.primero = (None)
                            self.ultimo = (None)
                            self.tamano = 0

                        break
                    elif nodoaux == self.getUltimo():
                        if nodoaux.getArriba() != None:
                            self.ultimo = nodoaux.getArriba()
                            nodoaux.getArriba().setAbajo(None)
                            self.tamano = self.tamano - 1
                        else:
                            self.setPrimero(None)
                            self.setUltmio(None)
                            self.tamano = 0

                        break
                    else:
                        nodoaux.getArriba().setAbajo(nodoaux.getAbajo())
                        nodoaux.getAbajo().setArriba(nodoaux.getArriba())
                        self.tamano = self.tamano - 1

                        break
                else:
                    nodoaux = nodoaux.getAbajo()

# ********************************************Matriz.....



class Matriz(object):
    def __init__(self):
        self.ListaL = None
        self.ListaD = None
        self.listanombres = None
        self.tamano = 0

#***********************************************Incertar en la Matriz....
    def insertar(self, letra, dominio, objeto):
        if self.tamano == 0:
            self.ListaL = Letras()
            self.ListaD = Dominio()

            ListaN = Nombres()

            ListaN.insertar(objeto)

            nodo = NodoMatriz(ListaN, letra, dominio)

            self.ListaD.insertar(dominio)
            self.ListaL.insertar(letra)

            auxLetra = self.ListaL.buscar(letra)
            auxDominio = self.ListaD.buscar(dominio)

            auxLetra.setSiguiente(nodo)
            auxDominio.setAbajo(nodo)

            nodo.setArriba(auxDominio)
            nodo.setAnterior(auxLetra)

            self.tamano = self.tamano + 1

        elif self.tamano > 0:

            if self.ListaL.buscar(letra) != None and self.ListaD.buscar(dominio) != None:

                if self.Comparar(letra, dominio) == True:

                    nodoauxD = self.ListaD.buscar(dominio)
                    nodoaux = nodoauxD

                    while nodoaux != None:

                        if nodoaux.getLetra() == letra:
                            nodoauxD = nodoaux
                            nodoaux = nodoaux.getAbajo()
                        else:
                            nodoaux = nodoaux.getAbajo()

                    listanombres = nodoauxD.getValor()
                    listanombres.insertar(objeto)


                else:
                    nodoauxD = self.ListaD.buscar(dominio)
                    nodoaux = nodoauxD.getAbajo()

                    ListaN = Nombres()

                    ListaN.insertar(objeto)

                    nodo = NodoMatriz(ListaN, letra, dominio)
                    letrainsertar = letra[:1]
                    letrainsertar = ord(letrainsertar)

                    agregado = False
                    while nodoaux != None:

                        letracomparar = nodoaux.getLetra()[:1]
                        letracomparar = ord(letracomparar)
                        if letrainsertar > letracomparar:
                            nodoaux = nodoaux.getAbajo()
                        else:
                            nodo.setAbajo(nodoaux)
                            nodo.setArriba(nodoaux.getArriba())
                            nodoaux.getArriba().setAbajo(nodo)
                            nodoaux.setArriba(nodo)
                            agregado = True
                            break
                    if agregado == False:
                        nodoaux = nodoauxD.getAbajo()
                        while nodoaux.getAbajo() != None:
                            nodoaux = nodoaux.getAbajo()

                        nodo.setArriba(nodoaux)
                        nodoaux.setAbajo(nodo)

                    nodoauxL = self.ListaL.buscar(letra)
                    nodoaux2 = nodoauxL.getSiguiente()

                    letrainsertar = dominio[:1]
                    letrainsertar = ord(letrainsertar)

                    agregado = False
                    while nodoaux2 != None:
                        letracomparar = nodoaux2.getDominio()[:1]
                        letracomparar = ord(letracomparar)

                        if letrainsertar > letracomparar:
                            nodoaux2 = nodoaux2.getSiguiente()
                        else:
                            nodo.setSiguiente(nodoaux2)
                            nodo.setAnterior(nodoaux2.getAnterior())
                            nodoaux2.getAnterior().setSiguiente(nodo)
                            nodoaux2.setAnterior(nodo)
                            agregado = True
                            break
                    if agregado == False:
                        nodoaux2 = nodoauxL.getSiguiente()
                        while nodoaux2.getSiguiente() != None:
                            nodoaux2 = nodoaux2.getSiguiente()

                        nodo.setAnterior(nodoaux2)
                        nodoaux2.setSiguiente(nodo)

                    self.tamano = self.tamano + 1


            elif self.ListaD.buscar(dominio) == None and self.ListaL.buscar(letra) != None:

                self.ListaD.insertar(dominio)

                nodoauxL = self.ListaL.buscar(letra)

                ListaN = Nombres()

                ListaN.insertar(objeto)

                nodo = NodoMatriz(ListaN, letra, dominio)
                nodoaux2 = nodoauxL.getSiguiente()

                letrainsertar = dominio[:1]
                letrainsertar = ord(letrainsertar)
                agregado = False

                while nodoaux2 != None:
                    letracomparar = nodoaux2.getDominio()[:1]
                    letracomparar = ord(letracomparar)

                    if letrainsertar > letracomparar:
                        nodoaux2 = nodoaux2.getSiguiente()
                    else:
                        nodo.setSiguiente(nodoaux2)
                        nodo.setAnterior(nodoaux2.getAnterior())
                        nodoaux2.getAnterior().setSiguiente(nodo)
                        nodoaux2.setAnterior(nodo)
                        agregado = True
                        break

                if agregado == False:
                    nodoaux2 = nodoauxL.getSiguiente()
                    while nodoaux2.getSiguiente() != None:
                        nodoaux2 = nodoaux2.getSiguiente()
                    nodo.setAnterior(nodoaux2)
                    nodoaux2.setSiguiente(nodo)

                auxDominio = self.ListaD.buscar(dominio)

                auxDominio.setAbajo(nodo)

                nodo.setArriba(auxDominio)

                self.tamano = self.tamano + 1



            elif self.ListaD.buscar(dominio) != None and self.ListaL.buscar(letra) == None:

                self.ListaL.insertar(letra)

                nodoauxD = self.ListaD.buscar(dominio)
                nodoaux = nodoauxD.getAbajo()

                ListaN = Nombres()

                ListaN.insertar(objeto)

                nodo = NodoMatriz(ListaN, letra, dominio)

                letrainsertar = letra[:1]
                letrainsertar = ord(letrainsertar)

                agregado = False
                while nodoaux != None:

                    letracomparar = nodoaux.getLetra()[:1]
                    letracomparar = ord(letracomparar)

                    if letrainsertar > letracomparar:
                        nodoaux = nodoaux.getAbajo()
                    else:
                        nodo.setAbajo(nodoaux)
                        nodo.setArriba(nodoaux.getArriba())
                        nodoaux.getArriba().setAbajo(nodo)
                        nodoaux.setArriba(nodo)
                        agregado = True
                        break
                if agregado == False:
                    nodoaux = nodoauxD.getAbajo()
                    while nodoaux.getAbajo() != None:
                        nodoaux = nodoaux.getAbajo()
                    nodo.setArriba(nodoaux)
                    nodoaux.setAbajo(nodo)

                auxLetra = self.ListaL.buscar(letra)
                auxLetra.setSiguiente(nodo)

                nodo.setAnterior(auxLetra)

                self.tamano = self.tamano + 1

            elif self.ListaD.buscar(dominio) == None and self.ListaL.buscar(letra) == None:

                self.ListaD.insertar(dominio)
                self.ListaL.insertar(letra)

                auxLista = self.ListaL.buscar(letra)
                auxDominio = self.ListaD.buscar(dominio)

                ListaN = Nombres()

                ListaN.insertar(objeto)

                nodo = NodoMatriz(ListaN, letra, dominio)

                auxLista.setSiguiente(nodo)
                auxDominio.setAbajo(nodo)

                nodo.setArriba(auxDominio)
                nodo.setAnterior(auxLista)
                self.tamano = self.tamano + 1

 #****************************************************Grafiar Matriz....
    def GraficarMatriz(self):
        f = open("C:\Users\Administrador\Desktop\Python\Matriz.txt", "w")
        f.write("digraph Matriz{ \n")
        f.write("node [fontcolor=\"blue\", height=0.5, color=\"gray\"]\n")
        f.write("[shape=box, style=filled]")
        f.write("rankdir=LR \n")
        f.write("edge  [color=\"black\", dir=fordware]\n")
        derecha = self.ListaD.getPrimero()
        Actual = derecha
        contador = 1
        f.write("i[style =\"filled\"; label=\"i\";pos= \"0,0!\"] \n")

        #Dominios
        while derecha != None:
            f.write(
                "\"" + Actual.getValor() + "\"" + "[style =\"filled\"; label=\"" + Actual.getValor() + "\";pos= \"" + str(contador) + ",0!\"]\n")
            contador = contador + 1
            derecha = derecha.getSiguiente()
            Actual = derecha

        contador = 1


        abajo = self.ListaL.getPrimero()
        Actual = abajo

        #Letras
        while abajo != None:
             f.write(Actual.getValor() + "[style =\"filled\"; label=" + Actual.getValor() + ";pos= \"0," +"-"+ str(contador) + "!\"]\n")
             contador = contador + 1

             abajo = abajo.getAbajo()
             Actual = abajo



        derecha = self.ListaD.getPrimero()
        actual = derecha
        while derecha != None:
            abajo = self.ListaL.getPrimero()
            while abajo != None:
                if actual.getAbajo() != None:
                    actual = actual.getAbajo()

                    f.write(
                        actual.getValor().getPrimero().getValor() + "[style =\"filled\"; label=" + actual.getValor().getPrimero().getValor() + ";pos= \"" + str(self.posX(actual.getDominio())) + "," +"-"+ str(self.posY(actual.getLetra())) + "!\"]\n")
                    self.imprimirPrimeros(actual.getValor(), f, actual.getLetra(), actual.getDominio())
                abajo = abajo.getAbajo()

            derecha = derecha.getSiguiente()
            actual = derecha

        derecha = self.ListaD.getPrimero()
        abajo = self.ListaL.getPrimero()
        f.write("\n i->" + "\"" + derecha.getValor() + "\"" + "->i->" + abajo.getValor() + "->i;\n")

        first = True
        Actual = derecha
        while derecha != None:

            if first == True:
                f.write(str("\"" + Actual.getValor()) + "\"")
                first = False
            else:
                f.write("->" + "\"" + Actual.getValor() + "\"")

            contador = contador + 1
            derecha = derecha.getSiguiente()
            Actual = derecha
        f.write(";")

        izquierda = self.ListaD.getUltimo()

        last = True
        Actual = izquierda

        while izquierda != None:

            if last == True:
                f.write(str("\"" + Actual.getValor()) + "\"")
                last = False

            else:
                f.write("->" + "\"" + Actual.getValor() + "\"")

            izquierda = izquierda.getAnterior()
            Actual = izquierda

        f.write(";\n")

        first = True
        Actual = abajo
        while abajo != None:
            if first == True:
                f.write(str(Actual.getValor()))
                first = False
            else:
                f.write("->" + Actual.getValor())
            abajo = abajo.getAbajo()
            Actual = abajo
        f.write(";\n")


        last = True
        arriba = self.ListaL.getUltimo()
        Actual = arriba
        while arriba != None:
            if last == True:
                f.write(str(Actual.getValor()))
                last = False
            else:
                f.write("->" + Actual.getValor())
            arriba = arriba.getArriba()
            Actual = arriba

        f.write(";\n")


        derecha = self.ListaD.getPrimero()
        actual = derecha
        while derecha != None:
            abajo = self.ListaL.getPrimero()
            f.write("\"" + derecha.getValor() + "\"")
            while abajo != None:
                if actual.getAbajo() != None:
                    actual = actual.getAbajo()
                    f.write("->" + actual.getValor().getPrimero().getValor())
                abajo = abajo.getAbajo()
            f.write(";\n")
            derecha = derecha.getSiguiente()
            actual = derecha

        f.write("\n\n\n")


        abajo = self.ListaL.getPrimero()
        actual = abajo
        while abajo != None:
            derecha = self.ListaD.getPrimero()
            f.write(abajo.getValor())
            while derecha != None:
                if actual.getSiguiente() != None:
                    actual = actual.getSiguiente()
                    f.write("->" + actual.getValor().getPrimero().getValor())
                derecha = derecha.getSiguiente()
            f.write(";\n")
            abajo = abajo.getAbajo()
            actual = abajo

        f.write("\n\n\n")

        derecha = self.ListaD.getPrimero()
        aux = derecha

        while derecha != None:

            while aux.getAbajo() != None:
                aux = aux.getAbajo()
            while aux.getArriba() != None:
                f.write(aux.getValor().getPrimero().getValor() + "->")
                aux = aux.getArriba()

            f.write("\"" + derecha.getValor() + "\"")
            f.write(";\n")
            derecha = derecha.getSiguiente()
            aux = derecha

        abajo = self.ListaL.getPrimero()
        aux = abajo

        while abajo != None:

            while aux.getSiguiente() != None:
                aux = aux.getSiguiente()
            while aux.getAnterior() != None:
                f.write(aux.getValor().getPrimero().getValor() + "->")
                aux = aux.getAnterior()

            f.write(abajo.getValor())
            f.write(";\n")
            abajo = abajo.getAbajo()
            aux = abajo

        f.write("}")
        subprocess.Popen("fdp -Tpng C:\Users\Administrador\Desktop\Python\Matriz.txt -o C:\Users\Administrador\Desktop\Python\Matriz.png")

    def posX(self, nodo):
        x = 1
        derecha = self.ListaD.getPrimero()

        while derecha != None:
            if derecha.getValor() == nodo:
                return x
            else:
                x = x + 1
                derecha = derecha.getSiguiente()

    def posY(self, nodo):

        y = 1
        abajo = self.ListaL.getPrimero()
        while abajo != None:
            if abajo.getValor() == nodo:
                return y
            else:
                y = y + 1
                abajo = abajo.getAbajo()

    def Comparar(self, letra, dominio):
        nodoAux = self.ListaD.buscar(dominio)
        while nodoAux != None:
            if nodoAux.getLetra() == letra:
                return True
            else:
                nodoAux = nodoAux.getAbajo()
        return False

    def imprimirPrimeros(self, lista, f, letra, dominio):
        f = f
        cont2 = self.posX(dominio)
        contador = self.posY(letra)
        if lista.getTamano() > 1:
            auxiliar = lista.getPrimero()
            while auxiliar.getSiguiente() != None:
                contador = contador + 0.05
                cont2 = cont2 + 0.05
                auxiliar = auxiliar.getSiguiente()
                aux = auxiliar
                f.write(
                    "\"" + auxiliar.getValor() + "\"" + "[fontcolor=\"black\",shape=box,style=filled; label=\"" + auxiliar.getValor() + "\";pos= \"" + str(cont2+cont2) + "," +"-"+ str(contador) + "!\"]\n")

            f.write(";\n")

            auxiliar = lista.getPrimero()
            f.write(auxiliar.getValor())
            while auxiliar.getSiguiente() != None:
                auxiliar = auxiliar.getSiguiente()
                aux = auxiliar

                f.write("->" + auxiliar.getValor())

            f.write(";\n")
            f.write(lista.getUltimo().getValor() + "")
            auxiliar = lista.getUltimo()

            while auxiliar.getAnterior() != None:
                auxiliar = auxiliar.getAnterior()
                f.write("->" + auxiliar.getValor())

            f.write(";\n")


    def insertarCorreo(self, email):
        objeto = email.split("@")
        nombre = objeto[0]

        dominio = objeto[1]
        letra = nombre[:1]
        self.insertar(letra, dominio, nombre)

    def eliminar(self, email):
        objeto = email.split("@")
        nombre = objeto[0]

        dominio = objeto[1]
        letra = nombre[:1]
        self.EliminarCorreo(letra, dominio, nombre)

    def EliminarCorreo(self, letra, dominio, dato):
        auxLetra = self.ListaL.buscar(letra)
        auxDominio = self.ListaD.buscar(dominio)

        if auxLetra != None and auxDominio != None:
            aux = auxDominio

            while aux != None:

                if aux.getLetra() == letra:
                    lista = aux.getValor()
                    lista.eliminar(dato)

                    if lista.getPrimero() == None:

                        if self.Dominios() > 2:
                            if aux.getAbajo() != None:
                                aux.getArriba().setAbajo(aux.getAbajo())
                                aux.getAbajo().setArriba(aux.getArriba())
                            elif aux.getAbajo() == None:
                                aux.getArriba().setAbajo(None)
                        elif self.Dominios() == 2:
                            self.ListaD.eliminar(dominio)

                        if self.Letras() > 2:
                            if aux.getSiguiente() != None:
                                aux.getAnterior().setSiguiente(aux.getSiguiente())
                                aux.getSiguiente().setAnterior(aux.getAnterior())
                            elif aux.getSiguiente() == None:
                                aux.getAnterior().setSiguiente(None)
                        elif self.Letras() == 2:
                            self.ListaL.eliminar(letra)
                    return True
                else:
                    aux = aux.getAbajo()
            return False


    def Dominios(self):
        contador = 0
        aux = self.ListaD.getPrimero()
        while aux != None:
            contador = contador + 1
            aux = aux.getAbajo()
        return contador

    def Letras(self):
        contador = 0
        aux = self.ListaL.getPrimero()
        while aux != None:
            contador = contador + 1
            aux = aux.getSiguiente()
        return contador

    def PorDominio(self, dominio):
        derecha = self.ListaD.getPrimero()
        while derecha.getSiguiente() != None:
            print derecha.getValor()
            derecha.getSiguiente()
#**************************************************Retornar Recorridos
    def MostrarDominios(self, nodo):
                aux = self.ListaD.getPrimero()
                dom=nodo
                actual = aux
                texto=""
                while aux != None:
                    if aux.getValor()==nodo:
                        print aux.getValor()
                        texto=texto+"<>"+str(aux.getValor())
                        abajo = self.ListaL.getPrimero()
                        while abajo != None:
                            if actual.getAbajo() != None:
                                actual = actual.getAbajo()

                                print actual.getValor().getPrimero().getValor()
                                texto=texto+"<>"+str(actual.getValor().getPrimero().getValor())+"@"+dom
                                lista=actual.getValor()
                                auxiliar = lista.getPrimero()
                                while auxiliar.getSiguiente() != None:

                                    auxiliar = auxiliar.getSiguiente()
                                    print auxiliar.getValor()
                                    texto=texto+"<>"+str(auxiliar.getValor())+"@"+dom
                            abajo = abajo.getAbajo()
                        print "____"

                        aux = aux.getSiguiente()
                        actual = aux
                    else:
                       print("no se encontro")
                       aux = aux.getSiguiente()
                       actual = aux
                print  texto
                return texto

    def MostrarLetra(self,nodo):
                aux = self.ListaL.getPrimero()
                actual = aux
                texto=""
                while aux != None:
                    if aux.getValor()==nodo:

                        print aux.getValor()
                        texto=texto+"<>"+str(aux.getValor())
                        abajo = self.ListaL.getPrimero()
                        while abajo != None:
                            if actual.getSiguiente() != None:
                                actual = actual.getSiguiente()

                                print actual.getValor().getPrimero().getValor()
                                texto=texto+"<>"+str(actual.getValor().getPrimero().getValor())
                                lista=actual.getValor()
                                auxiliar = lista.getPrimero()
                                while auxiliar.getSiguiente() != None:

                                    auxiliar = auxiliar.getSiguiente()
                                    print auxiliar.getValor()
                                    texto=texto+"<>"+str(auxiliar.getValor())
                            abajo = abajo.getSiguiente()
                        print "____"

                        aux = aux.getAbajo()
                        actual = aux
                    else:
                       print("no se encontro")
                       aux = aux.getAbajo()
                       actual = aux
                print texto
                return texto









matriz = Matriz()
matriz.insertarCorreo("ana@gmail.com")
matriz.insertarCorreo("maria@gmail.com")
matriz.insertarCorreo("sol@gmail.com")
matriz.insertarCorreo("carmen@hotmail.com")
matriz.insertarCorreo("carol@hotmail.com")
matriz.insertarCorreo("karina@hotmail.com")
matriz.insertarCorreo("karla@hotmail.com")
matriz.GraficarMatriz()
matriz.eliminar("sol@gmail.com")
matriz.insertarCorreo("maria2@gmail.com")
matriz.insertarCorreo("maria3@gmail.com")
matriz.MostrarDominios("gmail.com")
matriz.MostrarLetra("m")
matriz.GraficarMatriz()



# ********************************************Consumir Servidor....


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
    dato = lista.Buscar(str(parametro))
    if dato == None:
        return "El Dato no se Encontro en la Lista"
    else:
        return "El Dato q se Encontro en la Lista es>>>" + dato
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
    cola2 = cola.EliminarUltimo()
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
    pila2 = pila.EliminarPrimero()
    pila.GraficarPila()
    return "El dato que salio de la Pila es>>>> " + pila2 + "!"

@app.route('/AgregarMatriz', methods=['POST'])
def AgregarMatriz():
    parametro = str(request.form['correo'])
    matriz.insertarCorreo(str(parametro))
    matriz.GraficarMatriz()
    return "Se Agrego a l Matriz>>>> " + str(parametro) + "!"

@app.route('/EliminarMatriz', methods=['POST'])
def EliminarMatriz():
    parametro = str(request.form['correoE'])
    ret=matriz.eliminar(parametro)
    matriz.GraficarMatriz()
    return "Se Elimino de la Matriz>>>> " + str(parametro) + "!"


@app.route('/BuscarMatrizL', methods=['POST'])
def BuscarMatrizL():
    parametro = str(request.form['buscarL'])
    ret=matriz.MostrarLetra(parametro)
    if ret=="":
        return "La Busque Por Letra no se Completo>>>"
    else:
        return "Busqueda Por Letra>>>> " + str(ret) + "!"

@app.route('/BuscarMatrizD', methods=['POST'])
def BuscarMatrizD():
    parametro = str(request.form['buscarD'])
    ret=matriz.MostrarDominios(parametro)
    if ret=="":
        return "La Busque Por Dominio no se Completo>>>"
    else:
        return "Busqueda Por Dominio>>>> " + str(ret) + "!"

@app.route("/")
def hellof():
    return "***Servidor Flask y Python***"


if __name__ == "__main__":
    app.run()

