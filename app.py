import tkinter as tk
from tkinter import ttk

# Constantes que definen el ancho y el alto de la ventana
WIDTH = 900  # Ancho
HEIGHT = 600 # Alto

def ejecutar_funcion(event):
    seleccion = combobx.get()
    if seleccion == "Abrir":
        print("Abriendo venta para elegir archivo")
    elif seleccion == "Guardar":
        print("Aguardando archivo")
    elif seleccion == "Guardar como":
        print("guardando archivo como")
    elif seleccion == "Salir":
        print("Saliendo del programa")

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
combobx["values"] = ["ARCHIVO", "Abrir", "Guardar", "Guardar como", "Salir"] # Valores del combobox
combobx.current(0) # Valor por defecto del combobo
combobx.configure(foreground='#E0E0E0')
combobx.place(x=10, y=7, width=100, height=23)

combobx.bind("<<ComboboxSelected>>", ejecutar_funcion)



button = tk.Button(root, text="Analizador", bg="#333766", fg="white", borderwidth=0.5)
button.place(x=140, y=7, width=100, height=23)

button2 = tk.Button(root, text="Errores", bg= "#333766", fg="white", borderwidth=0.5)
button2.place(x=270, y=7, width=100, height=23, )

button3 = tk.Button(root, text="Reporte", bg="#333766", fg="white", borderwidth=0.5)
button3.place(x=400, y=7, width=100, height=23)

entry = tk.Text(root, bg="#343541", fg="white")
entry.place(x=15, y=60, width=869, height=524)

etiqueta = tk.Label(root, text="Esta ventana no se puede maximizar ni redimensionar.", bg="#444654", fg="white")
etiqueta.pack(padx=20, pady=37)

# Main
root.mainloop()