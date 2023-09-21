import graphviz

class Graph():
    def __init__(self, fondo="blue", fuente="white", forma="circle"):
        self.dot = graphviz.Digraph('structs', filename='Reporte.png', node_attr={'shape': forma, 'style': 'filled', 'fillcolor': fondo, 'fontcolor': fuente, 'fontname': 'Helvetica'})

    def add3Nodos(self, *args, id):
        self.dot.node(str(id + 1),str(args[0][0]))
        self.dot.node(str(id + 2),str(args[0][1]))
        self.dot.node(str(id + 3),str(args[0][2]))

        self.dot.edge(str(id + 1), str(id + 2))
        self.dot.edge(str(id + 1), str(id + 3))

    def graficar(self):
        self.dot.render(outfile="Reporte.png")
    
    def add2Nodos(self, *args, id):
        self.dot.node(str(id + 1),str(args[0][0]))
        self.dot.node(str(id + 2),str(args[0][1]))

        self.dot.edge(str(id + 1), str(id + 2))