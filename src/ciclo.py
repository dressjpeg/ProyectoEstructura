def tiene_ciclo(grafo):

    visitados = set()
    en_recursion = set()

    def dfs(nodo):

        visitados.add(nodo)
        en_recursion.add(nodo)

        for vecino in grafo.adyacencia[nodo]:

            if vecino not in visitados:

                if dfs(vecino):
                    return True

            elif vecino in en_recursion:
                return True

        en_recursion.remove(nodo)

        return False

    for nodo in grafo.adyacencia:

        if nodo not in visitados:

            if dfs(nodo):
                return True

    return False