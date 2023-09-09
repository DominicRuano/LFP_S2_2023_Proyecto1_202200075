from tkinter import *
from tkinter import ttk

# Constantes que definen el ancho y el alto de la ventana
WIDTH = 600  # Ancho
HEIGHT = 400 # Alto


root = Tk()
root.title("My GUI App")

# Centrar la ventana en la pantalla
ancho_pantalla = (root.winfo_screenwidth() - WIDTH) // 2
alto_pantalla = (root.winfo_screenheight() - HEIGHT) // 2 

root.geometry("{}x{}+{}+{}".format(WIDTH, HEIGHT,ancho_pantalla, alto_pantalla))

# Create a Label
my_label = ttk.Label(root, text="Hello World!")
my_label.pack()

# Create a Button
my_button = ttk.Button(root, text="Click Me!")
my_button.pack()

# Create an Entry Field
name = ttk.Entry(root)
name.pack()

# Run the main window loop
root.mainloop()