from collections import deque

class OrdenTopologico:

    def __init__(self, grafo):
        self.grafo = grafo

    def ordenar(self):

        grados_entrada = {}

        for tarea in self.grafo.adyacencia:
            grados_entrada[tarea] = 0

        for tarea in self.grafo.adyacencia:

            for vecino in self.grafo.adyacencia[tarea]:
                grados_entrada[vecino] += 1

        cola = deque()

        for tarea in grados_entrada:

            if grados_entrada[tarea] == 0:
                cola.append(tarea)

        orden = []

        while cola:

            actual = cola.popleft()
            orden.append(actual)

            for vecino in self.grafo.adyacencia[actual]:

                grados_entrada[vecino] -= 1

                if grados_entrada[vecino] == 0:
                    cola.append(vecino)

        return orden