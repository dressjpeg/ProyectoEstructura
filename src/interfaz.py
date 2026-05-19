import tkinter as tk
from tkinter import messagebox

from grafo import Grafo
from ciclo import tiene_ciclo
from topologico import OrdenTopologico

# Crear grafo
g = Grafo()


def agregar_dependencia():
    tarea1 = entrada_tarea1.get()
    tarea2 = entrada_tarea2.get()

    if tarea1 == "" or tarea2 == "":
        messagebox.showwarning(
            "Error",
            "Debes llenar ambas tareas"
        )
        return

    g.agregar_dependencia(tarea1, tarea2)

    lista_dependencias.insert(
        tk.END,
        f"{tarea1} -> {tarea2}"
    )

    entrada_tarea1.delete(0, tk.END)
    entrada_tarea2.delete(0, tk.END)


def verificar_proyecto():

    resultado_texto.delete("1.0", tk.END)

    resultado_texto.insert(
        tk.END,
        "Grafo de tareas:\n"
    )

    for tarea in g.adyacencia:

        resultado_texto.insert(
            tk.END,
            f"{tarea} -> {g.adyacencia[tarea]}\n"
        )

    if tiene_ciclo(g):

        resultado_texto.insert(
            tk.END,
            "\n❌ El grafo tiene un ciclo\n"
        )

    else:

        resultado_texto.insert(
            tk.END,
            "\n✅ No hay ciclos\n"
        )

        orden = OrdenTopologico(g)
        resultado = orden.ordenar()

        resultado_texto.insert(
            tk.END,
            f"\n📌 Orden válido:\n{resultado}"
        )


# Ventana principal
ventana = tk.Tk()

ventana.title(
    "Proyecto Estructura de Datos"
)

ventana.geometry("600x500")

# Título
titulo = tk.Label(
    ventana,
    text="Verificación de Ciclos y Orden Topológico",
    font=("Arial", 16, "bold")
)

titulo.pack(pady=10)

# Frame entradas
frame_entradas = tk.Frame(ventana)
frame_entradas.pack(pady=10)

# Tarea origen
label1 = tk.Label(
    frame_entradas,
    text="Tarea origen"
)

label1.grid(
    row=0,
    column=0,
    padx=5
)

entrada_tarea1 = tk.Entry(frame_entradas)

entrada_tarea1.grid(
    row=0,
    column=1,
    padx=5
)

# Tarea destino
label2 = tk.Label(
    frame_entradas,
    text="Tarea destino"
)

label2.grid(
    row=1,
    column=0,
    padx=5
)

entrada_tarea2 = tk.Entry(frame_entradas)

entrada_tarea2.grid(
    row=1,
    column=1,
    padx=5
)

# Botón agregar
boton_agregar = tk.Button(
    ventana,
    text="Agregar dependencia",
    command=agregar_dependencia
)

boton_agregar.pack(pady=10)

# Lista dependencias
lista_dependencias = tk.Listbox(
    ventana,
    width=50
)

lista_dependencias.pack(pady=10)

# Botón verificar
boton_verificar = tk.Button(
    ventana,
    text="Verificar proyecto",
    command=verificar_proyecto
)

boton_verificar.pack(pady=10)

# Área resultados
resultado_texto = tk.Text(
    ventana,
    height=12,
    width=70
)

resultado_texto.pack(pady=10)

# Ejecutar interfaz
ventana.mainloop()