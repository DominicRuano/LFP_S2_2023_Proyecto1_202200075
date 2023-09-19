import tkinter as tk
from tkinter import ttk
from leerjson import objeto

# Constantes que definen el ancho y el alto de la ventana
WIDTH = 900  # Ancho
HEIGHT = 600 # Alto

obj = objeto()

# Funcion que se ejecuta al seleccionar una opcion del combobox
def ejecutar_funcion(event):
    seleccion = combobx.get()
    if seleccion == "Abrir":
        obj.getPath()
        obj.getContenido()
        entry.delete(1.0, tk.END)
        entry.insert(tk.END, obj.contenido)

    elif seleccion == "Guardar":
        obj.guardar(entry.get("1.0", "end-1c"))

    elif seleccion == "Guardar como":
        obj.guardarComo(entry.get("1.0", "end-1c"))
    elif seleccion == "Salir":
        root.destroy()

def analizar():
    print("Analizando")

def errores():
    if obj:
        obj.getErrores()
        obj.imprimirErrores()
        entry.delete(1.0, tk.END)
        entry.insert(tk.END, obj.contenidoErrores)
    else:
        print("Aun no se ha creado el objeto.")

def reporte():
    print("Mostrando reporte")

# Creacion de la ventana
root = tk.Tk()
root.title("Analizador lexico - Editor de texto")
root.resizable(False, False)
root.configure(bg="#444654")

# Centrar la ventana en la pantalla
ancho_pantalla = (root.winfo_screenwidth() - WIDTH) // 2 
alto_pantalla = (root.winfo_screenheight() - HEIGHT - 50) // 2 # 50 es la altura de la barra de tareas
root.geometry("{}x{}+{}+{}".format(WIDTH, HEIGHT,ancho_pantalla, alto_pantalla))

# Colorea el fondo de la ventana
label_fondo = tk.Label(root, background="#343541")
label_fondo.place(x=0, y=0, width=900, height=37)

# Crearcion de estilo para los combobox
style= ttk.Style()
style.theme_use('clam')
style.configure("TCombobox", fieldbackground= "#3E447D", background= "#3E447D", foreground= "white", bordercolor= "#343541", 
                arrowcolor= "white", borderwidth= 0.5, lightcolor= "white", darkcolor= "black")

# Creacion del combobox
combobx = ttk.Combobox(root)
combobx.place(x=100, y=100)
combobx["values"] = ["Abrir", "Guardar", "Guardar como", "Salir"] # Valores del combobox
combobx.current(0) # Valor por defecto del combobo
combobx.configure(foreground='#E0E0E0')
combobx.place(x=10, y=7, width=100, height=23)

# Evento que se ejecuta al seleccionar una opcion del combobox
combobx.bind("<<ComboboxSelected>>", ejecutar_funcion)

# Creacion de los botones
button = tk.Button(root, text="Analizador", bg="#333766", fg="white", borderwidth=0.5, command=analizar)
button2 = tk.Button(root, text="Errores", bg= "#333766", fg="white", borderwidth=0.5, command=errores)
button3 = tk.Button(root, text="Reporte", bg="#333766", fg="white", borderwidth=0.5, command=reporte)

# Posicion de los botones
button.place(x=140, y=7, width=100, height=23)
button2.place(x=270, y=7, width=100, height=23, )
button3.place(x=400, y=7, width=100, height=23)

# Creacion del tetxbox
entry = tk.Text(root, bg="#343541", fg="white")
entry.place(x=15, y=60, width=869, height=524)

# Creacion de una etiqueda de advertencia
etiqueta = tk.Label(root, text="Esta ventana no se puede maximizar ni redimensionar.", bg="#444654", fg="white")
etiqueta.pack(padx=20, pady=37)

# Main
root.mainloop()