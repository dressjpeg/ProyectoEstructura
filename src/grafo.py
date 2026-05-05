class Grafo:
    def __init__(self):
        self.adyacencia = {}

    def agregar_tarea(self, tarea):
        if tarea not in self.adyacencia:
            self.adyacencia[tarea] = []

    def agregar_dependencia(self, tarea1, tarea2):
        # tarea1 -> tarea2
        if tarea1 not in self.adyacencia:
            self.agregar_tarea(tarea1)
        if tarea2 not in self.adyacencia:
            self.agregar_tarea(tarea2)

        self.adyacencia[tarea1].append(tarea2)

    def mostrar(self):
        for tarea in self.adyacencia:
            print(f"{tarea} -> {self.adyacencia[tarea]}")