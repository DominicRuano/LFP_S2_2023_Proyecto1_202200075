from tkinter import filedialog
from tkinter import messagebox
import json

CARACTERES = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ''""\",[]{}.1234567890 :"



class objeto:
    def __init__(self):
        self.path = None
        self.contenido = None
        self.contenidoErrores = None
        self.listaErrores = None
        self.pathSalida = None
    
    def getPath(self):
        while True:
            try:
                path = filedialog.askopenfile(title="Seleccione el archivo",filetypes=(("JSON files", ".json"),("all files", ".*")))
                if messagebox.askquestion("Archivo", f"¿Está seguro que {path.name} es el archivo correcto?") == "yes":
                    self.path = path.name
                    break
                else:
                    continue
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