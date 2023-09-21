from tkinter import filedialog
from tkinter import messagebox
import json
from ARITMETICA.mate import *
from graph import Graph

CARACTERES = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ''""\",[]{}.1234567890 :"
operacionesPermitidas = ["suma","resta","multiplicacion","division","potencia","raiz","inverso","seno","coseno","tangente","mod"]

class objeto():
    def __init__(self):
        self.path = None
        self.pathSalida = None
        self.contenido = None
        self.contenidoErrores = None
        self.listaErrores = None
        self.listaAnalizada = [] # sintaxis [{"operacion": [valor1, valor2, valor n]}, {otro dic}] lista de diccionarios con listas
        self.listaAnalizadaRechazada = []
        self.configuracion = []

    def getPath(self):
        try:
            path = filedialog.askopenfile(title="Seleccione el archivo",filetypes=(("JSON files", ".json"),("all files", ".*")))
            if messagebox.askquestion("Archivo", f"¿Está seguro que {path.name} es el archivo correcto?") == "yes":
                self.path = path.name
                self.getContenido()
        except:
            print("Error al abrir el archivo")
            messagebox.showerror("Error", "Error al abrir el archivo o se cerro la ventana, intentelo de nuevo")

    def getContenido(self):
        try:
            with open(self.path, 'r') as archivo_js:
                self.contenido = archivo_js.read()
        except FileNotFoundError:
            print("El archivo no se encontró.")
            messagebox.showerror("Error", "Error al abrir el archivo, archivo no encontrado.")
        except IOError as e:
            print(f"Error al abrir o leer el archivo: {str(e)}")
            messagebox.showerror("Error", "Error al abrir o leer el archivo")
        except Exception as e:
            print(f"Se produjo un error inesperado: {str(e)}")
            messagebox.showerror("Error", "Se produjo un error inesperado.")

    def getErrores(self):
        lista = []
        contador = 1
        try:
            lineas = self.contenido.splitlines()
            for numero, linea in enumerate(lineas, start=1):
                for caracter in linea:
                    if caracter not in CARACTERES:
                        #print(f"Error sintactico en la linea {numero} y columna {linea.index(caracter) + 1} el caracter es {caracter}")
                        lista.append({
                            "NO": contador,
                            "Descripcion": {
                                "Lexema": f"{caracter}",
                                "Tipo": "error lexico",
                                "Columna": linea.index(caracter) + 1,
                                "Fila": numero
                            }
                        })
                        contador += 1
            self.listaErrores = {"Errores": lista}
            self.imprimirErrores()
        except AttributeError as e:
            messagebox.showinfo("Sin traibutos", "El archivo aun no se ha cargado.")

    def imprimirErrores(self):
        nombre_archivo = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("Archivos JSON", "*.json")])
        if nombre_archivo:
            self.pathSalida = nombre_archivo
            with open(self.pathSalida, "w") as salida:
                json.dump(self.listaErrores, salida, indent=4)
        try:
            with open(self.pathSalida, 'r') as archivo_js:
                self.contenidoErrores = archivo_js.read()
        except:
            print("ocurrio un error al crear contenidoErrores en el objeto.")

    def guardar(self, texto):
        datos = json.loads(texto)
        try:
            with open(self.path, "w") as salida:
                    json.dump(datos, salida, indent=4)
            messagebox.showinfo("Guardado correcto", "El archivo se guardo correctamente")
        except:
            print("se produjo un error al guardar el archivo")

    def guardarComo(self, texto):
        datos = json.loads(texto)
        nombre_archivo = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("Archivos JSON", "*.json")])
        try:
            with open(nombre_archivo, "w") as salida:
                    json.dump(datos, salida, indent=4)
            messagebox.showinfo("Guardado correcto", f"El archivo llamado {nombre_archivo} se guardo correctamente")
        except:
            print("se produjo un error al guardar el archivo")

    def analizar(self):
        with open(self.path, "r") as archivo:
            datos = json.load(archivo)
        operaciones = datos["operaciones"]
        self.listaAnalizada = self.obtener(operaciones)
        self.eliminar()
        self.eliminar()
        self.configuracion = self.obtenerConfirg(datos["configuraciones"])
        cadena = "El archivo se ha analizado correctamente: "
        for a in self.listaAnalizada:
            cadena += f"\n      {a}"
        cadena += "\n\nLos objetos rechazados fueron:"
        for a in self.listaAnalizadaRechazada:
            cadena += f"\n      {a}"
        cadena += "\n\nLas configuraciones son las siguiente: "
        for a in self.configuracion:
            cadena += f"\n{a}"
        if self.listaAnalizada:
            messagebox.showinfo("Analizar", f"{cadena}")

    def obtener(self, operaciones):
        listaFinal = []
        llenar = False
        lista = {}
        llave = ""
        numeros = []
        for operacion in operaciones:
            for valor in operacion:
                if "operacion" == str(valor).lower():
                    llave = operacion[valor]
                    llenar = True
                elif llenar:
                    if isinstance(operacion[valor], list):
                        numeros.append(self.obtener(operacion[valor]))
                    else:
                        numeros.append(operacion[valor])
            if llave and numeros:
                lista[llave] = numeros
                listaFinal.append(lista)
            lista = {}
            llave = ""
            numeros = []
            llenar = False
        return listaFinal

    def eliminar(self, valor = False):
        if valor:
            for a in self.listaAnalizada:
                for b in a:
                    if b.lower() in operacionesPermitidas:
                        for c in a[b]:
                            if isinstance(c, list):
                                if self.eliminaChikito(c):
                                    pass
                                else:
                                    self.listaAnalizadaRechazada.append(a)
                                    self.listaAnalizada[self.listaAnalizada.index(a)] = []
                        break
                    else:
                        self.listaAnalizadaRechazada.append(a)
                        self.listaAnalizada[self.listaAnalizada.index(a)] = []
                        break
        else:
            self.eliminar(valor=True)
            for a in self.listaAnalizada:
                if a == []:
                    self.listaAnalizada.pop(self.listaAnalizada.index(a))
                else:
                    for objeto in a:
                        if objeto == []:
                            self.listaAnalizadaRechazada.append(a)
                            self.listaAnalizada.pop(self.listaAnalizada.index(a))

    def eliminaChikito(self, datos):
        for a in datos:
            for b in a:
                if isinstance(b, str):
                    if b.lower() in operacionesPermitidas:
                        for c in a[b]:
                            if isinstance(c, list):
                                return self.eliminaChikito(c)
                    else:
                        return False
                if isinstance(b, int) or isinstance(b, float):
                    return True
        return True

    def obtenerConfirg(self, datos):
        lista = []
        configuraciones = {}
        for configuracion in datos:
            for objeto in configuracion:
                configuraciones[objeto] = configuracion[objeto]
                lista.append(configuraciones)
                configuraciones = {}
        return lista

    def reporte(self):
        contador = 0
        lista = []
        for a in self.configuracion:
            lista.append(a)
        print()
        print()
        graphviz = Graph(fondo=lista[1]["fondo"], fuente=lista[2]["fuente"], forma=lista[3]["forma"])
        for operacion in self.listaAnalizada:
            for valor in operacion:
                if "suma" == str(valor).lower():
                    print("se dectecto una suma")
                    if isinstance(operacion[valor][0], list) or isinstance(operacion[valor][1], list):
                        if isinstance(operacion[valor][0], list):
                            lista = self.reporteChikito(operacion[valor][0], contador+2, graphviz)
                            nombre = f"{valor}\n{suma(lista[1], operacion[valor][1])}"
                            graphviz.add3Nodos([nombre, lista[0], operacion[valor][1]], id=contador)
                            contador += 100
                        else:
                            lista = self.reporteChikito(operacion[valor][1], contador+2, graphviz)
                            nombre = f"{valor}\n{suma(operacion[valor][0], lista[1])}"
                            graphviz.add3Nodos([nombre, operacion[valor][0], lista[0]], id=contador)
                            contador += 100
                    else:
                        nombre = f"{valor}\n{suma(operacion[valor][0], operacion[valor][1])}"
                        graphviz.add3Nodos([nombre, operacion[valor][0], operacion[valor][1]], id=contador)
                        contador += 100
                elif "resta" == str(valor).lower():
                    print("se dectecto una resta")
                    if isinstance(operacion[valor][0], list) or isinstance(operacion[valor][1], list):
                        if isinstance(operacion[valor][0], list):
                            lista = self.reporteChikito(operacion[valor][0], contador+2, graphviz)
                            nombre = f"{valor}\n{resta(lista[1], operacion[valor][1])}"
                            graphviz.add3Nodos([nombre, lista[0], operacion[valor][1]], id=contador)
                            contador += 100
                        else:
                            lista = self.reporteChikito(operacion[valor][1], contador+2, graphviz)
                            nombre = f"{valor}\n{resta(operacion[valor][0], lista[1])}"
                            graphviz.add3Nodos([nombre, operacion[valor][0], lista[0]], id=contador)
                            contador += 100
                    else:
                        nombre = f"{valor}\n{resta(operacion[valor][0], operacion[valor][1])}"
                        graphviz.add3Nodos([nombre, operacion[valor][0], operacion[valor][1]], id=contador)
                        contador += 100
                elif "multiplicacion" == str(valor).lower():
                    print("se dectecto una multiplicacion")
                    if isinstance(operacion[valor][0], list) or isinstance(operacion[valor][1], list):
                        if isinstance(operacion[valor][0], list):
                            lista = self.reporteChikito(operacion[valor][0], contador+2, graphviz)
                            nombre = f"{valor}\n{multiplicacion(lista[1], operacion[valor][1])}"
                            graphviz.add3Nodos([nombre, lista[0], operacion[valor][1]], id=contador)
                            contador += 100
                        else:
                            lista = self.reporteChikito(operacion[valor][1], contador+2, graphviz)
                            nombre = f"{valor}\n{multiplicacion(operacion[valor][0], lista[1])}"
                            graphviz.add3Nodos([nombre, operacion[valor][0], lista[0]], id=contador)
                            contador += 100
                    else:
                        nombre = f"{valor}\n{multiplicacion(operacion[valor][0], operacion[valor][1])}"
                        graphviz.add3Nodos([nombre, operacion[valor][0], operacion[valor][1]], id=contador)
                        contador += 100
                elif "division" == str(valor).lower():
                    print("se dectecto una division")
                    if isinstance(operacion[valor][0], list) or isinstance(operacion[valor][1], list):
                        if isinstance(operacion[valor][0], list):
                            lista = self.reporteChikito(operacion[valor][0], contador+2, graphviz)
                            nombre = f"{valor}\n{division(lista[1], operacion[valor][1])}"
                            graphviz.add3Nodos([nombre, lista[0], operacion[valor][1]], id=contador)
                            contador += 100
                        else:
                            lista = self.reporteChikito(operacion[valor][1], contador+2, graphviz)
                            nombre = f"{valor}\n{division(operacion[valor][0], lista[1])}"
                            graphviz.add3Nodos([nombre, operacion[valor][0], lista[0]], id=contador)
                            contador += 100
                    else:
                        nombre = f"{valor}\n{division(operacion[valor][0], operacion[valor][1])}"
                        graphviz.add3Nodos([nombre, operacion[valor][0], operacion[valor][1]], id=contador)
                        contador += 100
                elif "potencia" == str(valor).lower():
                    print("se dectecto una potencia")
                    if isinstance(operacion[valor][0], list) or isinstance(operacion[valor][1], list):
                        if isinstance(operacion[valor][0], list):
                            lista = self.reporteChikito(operacion[valor][0], contador+2, graphviz)
                            nombre = f"{valor}\n{potencia(lista[1], operacion[valor][1])}"
                            graphviz.add3Nodos([nombre, lista[0], operacion[valor][1]], id=contador)
                            contador += 100
                        else:
                            lista = self.reporteChikito(operacion[valor][1], contador+2, graphviz)
                            nombre = f"{valor}\n{potencia(operacion[valor][0], lista[1])}"
                            graphviz.add3Nodos([nombre, operacion[valor][0], lista[0]], id=contador)
                            contador += 100
                    else:
                        nombre = f"{valor}\n{potencia(operacion[valor][0], operacion[valor][1])}"
                        graphviz.add3Nodos([nombre, operacion[valor][0], operacion[valor][1]], id=contador)
                        contador += 100
                elif "raiz" == str(valor).lower():
                    print("se dectecto una raiz")
                    if isinstance(operacion[valor][0], list) or isinstance(operacion[valor][1], list):
                        if isinstance(operacion[valor][0], list):
                            lista = self.reporteChikito(operacion[valor][0], contador+2, graphviz)
                            nombre = f"{valor}\n{raiz(lista[1], operacion[valor][1])}"
                            graphviz.add3Nodos([nombre, lista[0], operacion[valor][1]], id=contador)
                            contador += 100
                        else:
                            lista = self.reporteChikito(operacion[valor][1], contador+2, graphviz)
                            nombre = f"{valor}\n{raiz(operacion[valor][0], lista[1])}"
                            graphviz.add3Nodos([nombre, operacion[valor][0], lista[0]], id=contador)
                            contador += 100
                    else:
                        nombre = f"{valor}\n{raiz(operacion[valor][0], operacion[valor][1])}"
                        graphviz.add3Nodos([nombre, operacion[valor][0], operacion[valor][1]], id=contador)
                        contador += 100
                elif "inverso" == str(valor).lower():
                    print("se dectecto una inverso")
                    if isinstance(operacion[valor][0], list):
                        lista = self.reporteChikito(operacion[valor][0], contador+1, graphviz)
                        nombre = f"{valor}\n{inverso(lista[1], operacion[valor][1])}"
                        graphviz.add2Nodos([nombre, lista[0]], id=contador)
                        contador += 100
                    else:
                        nombre = f"{valor}\n{inverso(operacion[valor][0])}"
                        graphviz.add2Nodos([nombre, operacion[valor][0]], id=contador)
                        contador += 100
                elif "seno" == str(valor).lower():
                    print("se dectecto una seno")
                    if isinstance(operacion[valor][0], list):
                        lista = self.reporteChikito(operacion[valor][0], contador+1, graphviz)
                        nombre = f"{valor}\n{seno(lista[1], operacion[valor][1])}"
                        graphviz.add2Nodos([nombre, lista[0]], id=contador)
                        contador += 100
                    else:
                        nombre = f"{valor}\n{seno(operacion[valor][0])}"
                        graphviz.add2Nodos([nombre, operacion[valor][0]], id=contador)
                        contador += 100
                elif "coseno" == str(valor).lower():
                    print("se dectecto una coseno")
                    if isinstance(operacion[valor][0], list):
                        lista = self.reporteChikito(operacion[valor][0], contador+1, graphviz)
                        nombre = f"{valor}\n{coseno(lista[1], operacion[valor][1])}"
                        graphviz.add2Nodos([nombre, lista[0]], id=contador)
                        contador += 100
                    else:
                        nombre = f"{valor}\n{coseno(operacion[valor][0])}"
                        graphviz.add2Nodos([nombre, operacion[valor][0]], id=contador)
                        contador += 100
                elif "tangente" == str(valor).lower():
                    print("se dectecto una tangente")
                    if isinstance(operacion[valor][0], list):
                        lista = self.reporteChikito(operacion[valor][0], contador+1, graphviz)
                        nombre = f"{valor}\n{tangente(lista[1], operacion[valor][1])}"
                        graphviz.add2Nodos([nombre, lista[0]], id=contador)
                        contador += 100
                    else:
                        nombre = f"{valor}\n{tangente(operacion[valor][0])}"
                        graphviz.add2Nodos([nombre, operacion[valor][0]], id=contador)
                        contador += 100
                elif "mod" == str(valor).lower():
                    print("se dectecto una mod")
                    if isinstance(operacion[valor][0], list) or isinstance(operacion[valor][1], list):
                        if isinstance(operacion[valor][0], list):
                            lista = self.reporteChikito(operacion[valor][0], contador+2, graphviz)
                            nombre = f"{valor}\n{modulo(lista[1], operacion[valor][1])}"
                            graphviz.add3Nodos([nombre, lista[0], operacion[valor][1]], id=contador)
                            contador += 100
                        else:
                            lista = self.reporteChikito(operacion[valor][1], contador+2, graphviz)
                            nombre = f"{valor}\n{modulo(operacion[valor][0], lista[1])}"
                            graphviz.add3Nodos([nombre, operacion[valor][0], lista[0]], id=contador)
                            contador += 100
                    else:
                        nombre = f"{valor}\n{modulo(operacion[valor][0], operacion[valor][1])}"
                        graphviz.add3Nodos([nombre, operacion[valor][0], operacion[valor][1]], id=contador)
                        contador += 100
        graphviz.graficar()

    def reporteChikito(self, datos, contador, graphviz):
        for operacion in datos:
            for valor in operacion:
                if "suma" == str(valor).lower():
                    print("se dectecto una suma")
                    if isinstance(operacion[valor][0], list) or isinstance(operacion[valor][1], list):
                        if isinstance(operacion[valor][0], list):
                            lista = self.reporteChikito(operacion[valor][0], contador+2, graphviz)
                            nombre = f"{valor}\n{suma(lista[1], operacion[valor][1])}"
                            graphviz.add3Nodos([nombre, lista[0], operacion[valor][1]], id=contador)
                            return [nombre, suma(operacion[valor][0], lista[1])]
                        else:
                            lista = self.reporteChikito(operacion[valor][1], contador+2, graphviz)
                            nombre = f"{valor}\n{suma(operacion[valor][0], lista[1])}"
                            graphviz.add3Nodos([nombre, operacion[valor][0], lista[0]], id=contador)
                            return [nombre, suma(operacion[valor][0], lista[1])]
                    else:
                        nombre = f"{valor}\n{suma(operacion[valor][0], operacion[valor][1])}"
                        graphviz.add3Nodos([nombre, operacion[valor][0], operacion[valor][1]], id=contador)
                        return [nombre, suma(operacion[valor][0], operacion[valor][1])]
                elif "resta" == str(valor).lower():
                    print("se dectecto una resta")
                    if isinstance(operacion[valor][0], list) or isinstance(operacion[valor][1], list):
                        if isinstance(operacion[valor][0], list):
                            lista = self.reporteChikito(operacion[valor][0], contador+2, graphviz)
                            nombre = f"{valor}\n{resta(lista[1], operacion[valor][1])}"
                            graphviz.add3Nodos([nombre, lista[0], operacion[valor][1]], id=contador)
                            return [nombre, resta(operacion[valor][0], lista[1])]
                        else:
                            lista = self.reporteChikito(operacion[valor][1], contador+2, graphviz)
                            nombre = f"{valor}\n{resta(operacion[valor][0], lista[1])}"
                            graphviz.add3Nodos([nombre, operacion[valor][0], lista[0]], id=contador)
                            return [nombre, resta(operacion[valor][0], lista[1])]
                    else:
                        nombre = f"{valor}\n{resta(operacion[valor][0], operacion[valor][1])}"
                        graphviz.add3Nodos([nombre, operacion[valor][0], operacion[valor][1]], id=contador)
                        return [nombre, resta(operacion[valor][0], operacion[valor][1])]
                elif "multiplicacion" == str(valor).lower():
                    print("se dectecto una multiplicacion")
                    if isinstance(operacion[valor][0], list) or isinstance(operacion[valor][1], list):
                        if isinstance(operacion[valor][0], list):
                            lista = self.reporteChikito(operacion[valor][0], contador+2, graphviz)
                            nombre = f"{valor}\n{multiplicacion(lista[1], operacion[valor][1])}"
                            graphviz.add3Nodos([nombre, lista[0], operacion[valor][1]], id=contador)
                            return [nombre, multiplicacion(operacion[valor][0], lista[1])]
                        else:
                            lista = self.reporteChikito(operacion[valor][1], contador+2, graphviz)
                            nombre = f"{valor}\n{multiplicacion(operacion[valor][0], lista[1])}"
                            graphviz.add3Nodos([nombre, operacion[valor][0], lista[0]], id=contador)
                            return [nombre, multiplicacion(operacion[valor][0], lista[1])]
                    else:
                        nombre = f"{valor}\n{multiplicacion(operacion[valor][0], operacion[valor][1])}"
                        graphviz.add3Nodos([nombre, operacion[valor][0], operacion[valor][1]], id=contador)
                        return [nombre, multiplicacion(operacion[valor][0], operacion[valor][1])]
                elif "division" == str(valor).lower():
                    print("se dectecto una division")
                    if isinstance(operacion[valor][0], list) or isinstance(operacion[valor][1], list):
                        if isinstance(operacion[valor][0], list):
                            lista = self.reporteChikito(operacion[valor][0], contador+2, graphviz)
                            nombre = f"{valor}\n{division(lista[1], operacion[valor][1])}"
                            graphviz.add3Nodos([nombre, lista[0], operacion[valor][1]], id=contador)
                            return [nombre, division(operacion[valor][0], lista[1])]
                        else:
                            lista = self.reporteChikito(operacion[valor][1], contador+2, graphviz)
                            nombre = f"{valor}\n{division(operacion[valor][0], lista[1])}"
                            graphviz.add3Nodos([nombre, operacion[valor][0], lista[0]], id=contador)
                            return [nombre, division(operacion[valor][0], lista[1])]
                    else:
                        nombre = f"{valor}\n{division(operacion[valor][0], operacion[valor][1])}"
                        graphviz.add3Nodos([nombre, operacion[valor][0], operacion[valor][1]], id=contador)
                        return [nombre, division(operacion[valor][0], operacion[valor][1])]
                elif "potencia" == str(valor).lower():
                    print("se dectecto una potencia")
                    if isinstance(operacion[valor][0], list) or isinstance(operacion[valor][1], list):
                        if isinstance(operacion[valor][0], list):
                            lista = self.reporteChikito(operacion[valor][0], contador+2, graphviz)
                            nombre = f"{valor}\n{potencia(lista[1], operacion[valor][1])}"
                            graphviz.add3Nodos([nombre, lista[0], operacion[valor][1]], id=contador)
                            return [nombre, potencia(operacion[valor][0], lista[1])]
                        else:
                            lista = self.reporteChikito(operacion[valor][1], contador+2, graphviz)
                            nombre = f"{valor}\n{potencia(operacion[valor][0], lista[1])}"
                            graphviz.add3Nodos([nombre, operacion[valor][0], lista[0]], id=contador)
                            return [nombre, potencia(operacion[valor][0], lista[1])]
                    else:
                        nombre = f"{valor}\n{potencia(operacion[valor][0], operacion[valor][1])}"
                        graphviz.add3Nodos([nombre, operacion[valor][0], operacion[valor][1]], id=contador)
                        return [nombre, potencia(operacion[valor][0], operacion[valor][1])]
                elif "raiz" == str(valor).lower():
                    print("se dectecto una raiz")
                    if isinstance(operacion[valor][0], list) or isinstance(operacion[valor][1], list):
                        if isinstance(operacion[valor][0], list):
                            lista = self.reporteChikito(operacion[valor][0], contador+2, graphviz)
                            nombre = f"{valor}\n{raiz(lista[1], operacion[valor][1])}"
                            graphviz.add3Nodos([nombre, lista[0], operacion[valor][1]], id=contador)
                            return [nombre, raiz(operacion[valor][0], lista[1])]
                        else:
                            lista = self.reporteChikito(operacion[valor][1], contador+2, graphviz)
                            nombre = f"{valor}\n{raiz(operacion[valor][0], lista[1])}"
                            graphviz.add3Nodos([nombre, operacion[valor][0], lista[0]], id=contador)
                            return [nombre, raiz(operacion[valor][0], lista[1])]
                    else:
                        nombre = f"{valor}\n{raiz(operacion[valor][0], operacion[valor][1])}"
                        graphviz.add3Nodos([nombre, operacion[valor][0], operacion[valor][1]], id=contador)
                        return [nombre, raiz(operacion[valor][0], operacion[valor][1])]
                elif "inverso" == str(valor).lower():
                    print("se dectecto una inverso")
                    if isinstance(operacion[valor][0], list):
                        lista = self.reporteChikito(operacion[valor][0], contador+1, graphviz)
                        nombre = f"{valor}\n{inverso(lista[1])}"
                        graphviz.add2Nodos([nombre, lista[0]], id=contador)
                        return [nombre, inverso(operacion[valor][0])]
                    else:
                        nombre = f"{valor}\n{inverso(operacion[valor][0], operacion[valor][1])}"
                        graphviz.add2Nodos([nombre, operacion[valor][0]], id=contador)
                        return [nombre, inverso(operacion[valor][0])]
                elif "seno" == str(valor).lower():
                    print("se dectecto una seno")
                    if isinstance(operacion[valor][0], list):
                        lista = self.reporteChikito(operacion[valor][0], contador+1, graphviz)
                        nombre = f"{valor}\n{seno(lista[1])}"
                        graphviz.add2Nodos([nombre, lista[0]], id=contador)
                        return [nombre, seno(operacion[valor][0])]
                    else:
                        nombre = f"{valor}\n{seno(operacion[valor][0], operacion[valor][1])}"
                        graphviz.add2Nodos([nombre, operacion[valor][0]], id=contador)
                        return [nombre, seno(operacion[valor][0])]
                elif "coseno" == str(valor).lower():
                    print("se dectecto una coseno")
                    if isinstance(operacion[valor][0], list):
                        lista = self.reporteChikito(operacion[valor][0], contador+1, graphviz)
                        nombre = f"{valor}\n{coseno(lista[1])}"
                        graphviz.add2Nodos([nombre, lista[0]], id=contador)
                        return [nombre, coseno(operacion[valor][0])]
                    else:
                        nombre = f"{valor}\n{coseno(operacion[valor][0], operacion[valor][1])}"
                        graphviz.add2Nodos([nombre, operacion[valor][0]], id=contador)
                        return [nombre, coseno(operacion[valor][0])]
                elif "tangente" == str(valor).lower():
                    print("se dectecto una tangente")
                    if isinstance(operacion[valor][0], list):
                        lista = self.reporteChikito(operacion[valor][0], contador+1, graphviz)
                        nombre = f"{valor}\n{tangente(lista[1])}"
                        graphviz.add2Nodos([nombre, lista[0]], id=contador)
                        return [nombre, tangente(operacion[valor][0])]
                    else:
                        nombre = f"{valor}\n{tangente(operacion[valor][0], operacion[valor][1])}"
                        graphviz.add2Nodos([nombre, operacion[valor][0]], id=contador)
                        return [nombre, tangente(operacion[valor][0])]
                elif "mod" == str(valor).lower():
                    print("se dectecto una mod")
                    if isinstance(operacion[valor][0], list) or isinstance(operacion[valor][1], list):
                        if isinstance(operacion[valor][0], list):
                            lista = self.reporteChikito(operacion[valor][0], contador+2, graphviz)
                            nombre = f"{valor}\n{modulo(lista[1], operacion[valor][1])}"
                            graphviz.add3Nodos([nombre, lista[0], operacion[valor][1]], id=contador)
                            return [nombre, modulo(operacion[valor][0], lista[1])]
                        else:
                            lista = self.reporteChikito(operacion[valor][1], contador+2, graphviz)
                            nombre = f"{valor}\n{modulo(operacion[valor][0], lista[1])}"
                            graphviz.add3Nodos([nombre, operacion[valor][0], lista[0]], id=contador)
                            return [nombre, modulo(operacion[valor][0], lista[1])]
                    else:
                        nombre = f"{valor}\n{modulo(operacion[valor][0], operacion[valor][1])}"
                        graphviz.add3Nodos([nombre, operacion[valor][0], operacion[valor][1]], id=contador)
                        return [nombre, modulo(operacion[valor][0], operacion[valor][1])]
        print("ocurrio un error en aliminarChikito y re devolvio un valor vacio y un 0")
        return ["", 0]
