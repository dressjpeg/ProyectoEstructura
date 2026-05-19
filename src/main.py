from grafo import Grafo
from ciclo import tiene_ciclo
from topologico import OrdenTopologico

# Crear grafo
g = Grafo()

# Agregar dependencias
g.agregar_dependencia("A", "B")
g.agregar_dependencia("B", "C")
g.agregar_dependencia("A", "D")

# Mostrar grafo
print("Grafo de tareas:")
g.mostrar()

# Verificar ciclos
if tiene_ciclo(g):
    print("\n❌ El grafo tiene un ciclo")
else:
    print("\n✅ No hay ciclos")

    # Orden topológico
    orden = OrdenTopologico(g)
    resultado = orden.ordenar()

    print("📌 Orden de ejecución válido:")
    print(resultado)