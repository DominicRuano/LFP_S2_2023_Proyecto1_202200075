from tkinter import filedialog
from tkinter import messagebox
import json

CARACTERES = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ''""\",[]{}.1234567890 :"

class objeto:
    def __init__(self):
        self.path = None
        self.pathSalida = None
        self.contenido = None
        self.contenidoErrores = None
        self.listaErrores = None
        self.listaAnalizada = [] # sintaxis [{"operacion": [valor1, valor2, valor n]}, {otro dic}] lista de diccionarios con listas
        self.configuracion = None

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
        operaciones = ["suma","resta","multiplicacion","divicion","potencia","raiz","inverso","seno","coseno","tangente","mod"]
        with open(self.path, "r") as archivo:
            datos = json.load(archivo)
        operaciones = datos["operaciones"]
        self.listaAnalizada = self.obtener(operaciones)
        cadena = "El archivo se ha analizado correctamente: "
        for a in self.listaAnalizada:
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
                        print("here")
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