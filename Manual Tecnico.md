# LABORATORIO LENGUAJES FORMALES Y DE PROGRAMACION Sección B- 🖥️
## Informe 1 📚
### SEGUNDO SEMESTRE 2023 📅

```js
Universidad San Carlos de Guatemala 🎓
Programador: Dominic Juan pablo Ruano Perez 🧑‍💻
Carne: 202200075 🆔
```
---
## Descripción del Proyecto📋
Para este proyecto, se requiere que el estudiante desarrolle un analizador sintáctico diseñado para procesar archivos con extensión **.json**. Estos archivos se someterán a un análisis, a partir del cual se generarán informes tanto de las operaciones realizadas como de los errores detectados.

El programa empleará la biblioteca tkinter para crear una interfaz gráfica intuitiva, lo que permitirá que los usuarios poco familiarizados con la línea de comandos se sientan cómodos y puedan utilizarlo con facilidad.

Entre las capacidades destacadas del programa se encuentran la capacidad de generar informes, abrir y editar el archivo seleccionado, y guardar los cambios de manera que se conserven las propiedades originales del archivo. Además, se ofrece la opción de guardar una copia del archivo original con un nombre diferente.

Por último, el programa también ofrece la funcionalidad de representar gráficamente las operaciones contenidas en el archivo, haciendo uso de la biblioteca Graphviz. Esto permite generar una imagen que muestra de manera visual las operaciones de manera clara y comprensible.

> **Creacion del objeto en uso para el proyecto.**
<img src="https://i.ibb.co/gDMHRZz/clase-objeto.png" alt="funcion main" style="width:500px;"/>
con la intencion de mantener una accesibilidad se instancia un TDA el cual contendra toda la informacion neccesario para poder trabajar.
- **path:** guarda la direccion del archivo que se abre.
- **pathSalida:** guarda la direccion del archivo de salida al momento de guardar como.
- **contenido:** guarda el contenido de todo el archivo que se abre.
- **contenidoErrores:** guarda todos los errores detectados en el archivo.
- **listaerrores:** una lista con los errores almacenados.
- **listaAnalizada:** guarda todos los objetos que fueron analizados con exito.
- **listaAnalizadaRechazada:** una lista operaciones que no son reconcidas.
- **configuracion:** lista con las configuraciones necesarias para graphviz.

>**variables**
<img src="https://i.ibb.co/R6hY5MC/operaciones-y-caracteres.png">
- se definene las listas con todos los caracteres permitidos para el sistema.
- se define una lista con todas las operaciones que el sistema podria realizar.

## Objetivos 🎯
* Objetivo General
    * El objetivo general de este proyecto es desarrollar un analizador sintáctico capaz de procesar archivos con extensión .json y generar informes de operaciones y errores. Además, se busca proporcionar una interfaz gráfica amigable utilizando la biblioteca tkinter, para hacer que el programa sea accesible incluso para usuarios no familiarizados con la línea de comandos. Se incluye la capacidad de graficar operaciones mediante la librería Graphviz.
* Objetivos Específicos
    * Crear un analizador sintáctico eficiente y preciso que pueda identificar y analizar correctamente las operaciones contenidas en archivos .json, registrando cualquier error sintáctico encontrado.
    * Desarrollar una interfaz gráfica intuitiva utilizando tkinter que permita a los usuarios abrir, editar y guardar archivos .json de manera sencilla y que preserve las propiedades originales del archivo. También, proporcionar la funcionalidad de guardar una copia del archivo con un nombre diferente.
---


## Herramientas Principales a Utilizar 🛠️
* Visual Studio Code 💻
* Python 🐍
* Bibliotecas de Python
    * tkinter 🖼️
    * json
    * Graphviz
* Git  📜
* Github
---

## Enlaces de Utilidad  🔗
*  [instalacion de Python y VSC](https://www.youtube.com/watch?v=bZjulmpBIGk) 📹
*  [sitio oficial de graphviz](https://graphviz.org/)
*  [Documentacion de tkinter](https://docs.python.org/3/library/tk.html)

___
## Funciones dentro del codigo

>*   Funcion getPath()
    Es la encargada de obtener el path del archivo que se desea abrir.
<img src="https://i.ibb.co/Qk0VmrR/get-path.png" alt="funcion main" style="width:700px;"/>

---

>*   Funcion getContenido()
    Obtiene todo el contenido dentro del archivo.
<img src="https://i.ibb.co/JrSgKJb/get-contenido.png" alt="funcion main" style="width:500px;"/>

---

>*   Funcion getErrores()
    lee el archivo linea por linea y columna por columna y obtiene los errores en el archivo, ademas de agregarlos a lista de errores.
<img src="https://i.ibb.co/G35PtJZ/get-errores.png" alt="funcion main" style="width:600px;"/>

---

>*   Funcion obtener()
    agregando todos los objetos a unas lista y retornandola.
<img src="https://i.ibb.co/YZzfyDt/obtener.png" alt="funcion main" style="width:500px;"/>

---

>*   Funcion obtenerConfiguracion()
    Obtiene todas las configuraciones del archivo.
<img src="https://i.ibb.co/tx7YWrF/obtener-configuraciones.png" alt="funcion main" style="width:500px;"/>

---

>*   Funcion imprimirErroes()
    genera un archivo con formato .json y el nombre proporcionado
<img src="https://i.ibb.co/ZNRgtGB/imprimir-errores.png" alt="funcion main" style="width:500px;"/>

------

>*   Funcion Analizar()
    Analiza todo el contenido y reconoce las operaciones de ser asi las agregar a la lista del objeto y con la funcion eliminar elimina espacios en blanco resultantes en el procesos de seleccion.
<img src="https://i.ibb.co/QrxNh4F/analizar.png" alt="funcion main" style="width:500px;"/>

---

>*   Funcion eliminar()
    Leyendo todos los objetos en listaAnalizada determina cuales son objetos correctos para este sistema de lo contrario los agrega a otra lista.
<img src="https://i.ibb.co/0VQBY5w/eliminar.png" alt="funcion main" style="width:500px;"/>

---
>*   Funcion eliminiarChikito()
    funcion recursiva que ayuda a la eliminacion de operaciones no detectadas.
<img src="https://i.ibb.co/qkjXWG6/eliminarchikito.png" alt="funcion main" style="width:500px;"/>

---
>*   Funcion guardar()
    guarda el archivo abierto.
<img src="https://i.ibb.co/N2jvsMJ/guardar.png" alt="funcion main" style="width:500px;"/>

---
>*   Funcion reporte()
    fraccion de la funcion que genera el reporte de las operaciones generando las operaciones que son aceptadas.
<img src="https://i.ibb.co/NTyBV0n/reporte.png" alt="funcion main" style="width:500px;"/>

---
>*   Funcion reportechikito()
    fraccion de la funcion de respalda a la funcion de reporte para realizar el reporte.
<img src="https://i.ibb.co/NTyBV0n/reporte.png" alt="funcion main" style="width:500px;"/>

---
>*   Funcion guardarComo()
    realiza la opcion de guardar como.
<img src="https://i.ibb.co/VDX4wx1/guardar-como.png" alt="funcion main" style="width:500px;"/>

---
>*   clase Math()
    clase encargada de todas las operaciones del sistema, contando con suma, resta, multiplicacion entre otras... 
<img src="https://i.ibb.co/Qj3075G/math.png" alt="funcion main" style="width:400px;"/>

---
>*   Clase Graph()
    Contanto con el constructor que recibe como parametro el color de fondo, color de fuenta y la forma de los nodos.
    Ademas de las funciones:
>* add3nodos que añade 3 nodos, esta es usada para las funciones que requieren de dos numeros.
>*  add2nodos añade 2 nosodos, esta se usasa para las funciones que requieren solo un numero como parametro.
>*  graficar que grafica todos los nodos añadidos.
<img src="https://i.ibb.co/ZgNZbLV/graph.png" alt="funcion main" style="width:500px;"/>

---

>*   Muchas gracias eso seria todo
    gracias por leer todo este documento tenga un buen dia aux.
<img src="https://i.ibb.co/nB08qk2/1ac04daf-e3d7-4dbd-8c43-8877808ec602.jpg" alt="funcion main" style="width:200px;"/>