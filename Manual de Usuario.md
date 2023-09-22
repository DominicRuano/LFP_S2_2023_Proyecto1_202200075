# LABORATORIO LENGUAJES FORMALES Y DE PROGRAMACION Sección B- 🖥️
## Manual de usuario 📚
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

___
## Funciones dentro del codigo

>   **Menu.**
    se puede observar el menu inicial del sistema donde se observa el campo de texto vacio.
>*   *1.* El combo donde se puede acceder a distintas opciones que se explicaran mas adelante.
>* *2.* Boton analizar donde se analizara unicamente si se detecta un archivo abierto y que el campo de texto no haya sigo borrado.
>* *3.* Boton de errores donde generara un archivo con el nombre que se ingrese y pondra en el campo de texto el mismo con todos los errores detectados.
>*  *4.* Boton reporte donde se generara el reporte en **.PNG**
<img src="https://i.ibb.co/S0hzZm1/menu.png" alt="funcion main" style="width:500px;"/>

---
>*   **Combo.**
    Este combobox contiene algunas de ls funciones del programa, se acede dando click para desplegar las opciones y seleccionando una de ellas.
>*   *1.1* Abrir, abre una ventana para seleccionar que archivo deseamos abrir en el programa.
>* *1.2* Guardar, guarda los cambios en le mismo archivo que se abrio.
>* *1.3* Abre un menu donde debemos elegir el nombre y la ubicacion del archivo.
>*  *1.4* Salir, cierra el programa.
<img src="https://i.ibb.co/XXTL2SQ/combo.png" alt="funcion main" style="width:500px;"/>

---
>*   **Menu para Abrir un archivo.**
    esta ventana se muestra al seleccionar abrir, esta misma requiere que se seleccione un archivo para abrirlo, esta ventana cuenta con un filtro para visualizar unicamente los archivos con extencions **.json**
<img src="https://i.ibb.co/JQgfyBc/abrir.png" alt="funcion main" style="width:500px;"/>

---
>*   **Error en caso de errores.**
    En casi de detectarse un error ya sea porque no se seleccciono un archivo o cualquier otro error se mostrara este mensaje de error, seguido se podri volver a intentar abrir un archivo.
<img src="https://i.ibb.co/VVpp9tN/error-abrir.png" alt="funcion main" style="width:400px;"/>

---
>*   **Confirmacion de archivo.**
    Si se abrio al archivo sin errores mostrar este mensaje para asegurarse que esa sea la ruta correcta.
<img src="https://i.ibb.co/k06MfyP/conifirmacion-abrir.png" alt="funcion main" style="width:400px;"/>

---
>*   **Vista del menu para editar el archivo abierto.**
    si se abre correctamente el archivo este mismo se mostrara en el campo de texto en el programa.
<img src="https://i.ibb.co/XzhXSPt/menu-con-archivo-abierto.png" alt="funcion main" style="width:500px;"/>

---
>*   **Ventana de confirmacion de guardado.**
    En casi se guarde el archivo se mostrar este mensaje que confirmara que se guardo correctamente el archivo.
<img src="https://i.ibb.co/gvfHxJ5/guardar.png" alt="funcion main" style="width:400px;"/>

---
>*   **Ventana de Guardar como.**
    Para guardar como es necesario que se determine un nombre para el archivo y una ubicacion.
<img src="https://i.ibb.co/jRrR0xJ/guardar-como.png" alt="funcion main" style="width:500px;"/>

---
>*   **Mensaje de aviso de analizador.**
    Al seleccionar analizar se generar un reporte con las configuraciones, los objetos analizados aceptados y los objetos que fueron rechazados.
<img src="https://i.ibb.co/wLwT3Cq/mensaje-analizar.png" alt="funcion main" style="width:400px;"/>

---
>*   **Ventana para guardar los errores.**
    El boton de Errores mostrara una ventana donde se debe ingresar el nombre y seleccionar la ubicacion del archivo.
<img src="https://i.ibb.co/ggnFqzP/ventana-errores.png" alt="funcion main" style="width:500px;"/>

---
>*   **Vista del menu para visualizar los errores.**
    al generar los errores se abrira automaticamente el archivo de errores en el campo de texto.
<img src="https://i.ibb.co/RSm0pTK/menu-con-errores.png" alt="funcion main" style="width:500px;"/>

---
>*   Muchas gracias eso seria todo
    gracias por leer todo este documento tenga un buen dia aux.
<img src="https://i.ibb.co/nB08qk2/1ac04daf-e3d7-4dbd-8c43-8877808ec602.jpg" alt="funcion main" style="width:200px;"/>