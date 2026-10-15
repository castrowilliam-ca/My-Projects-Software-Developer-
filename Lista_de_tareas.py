import tkinter as tk
from tkinter import messagebox

def agregar_tarea(event=None):
    texto = entrada.get().strip()
    if not texto:
        messagebox.showwarning("Aviso", "Escribe una tarea")
        return
    
    marco_tarea = tk.Frame(lista, bg="#f9f9f9", pady=5)
    marco_tarea.pack(fill="x", padx=5, pady=2)
    
    etiqueta = tk.Label(
        marco_tarea,
        text=texto,
        font=("Arial", 12),
        bg="#f9f9f9",
        anchor="w"
    )
    etiqueta.pack(side="left", fill="x", expand=True)
    etiqueta.bind("<Button-1>", lambda e: marcar_completada(etiqueta))
    
    btn_borrar = tk.Button(
        marco_tarea,
        text="Eliminar",
        bg="#e74c3c",
        fg="white",
        relief="flat",
        command=lambda: marco_tarea.destroy()
    )
    btn_borrar.pack(side="right", padx=5)
    
    entrada.delete(0, tk.END)

def marcar_completada(etiqueta):
    estado = etiqueta.cget("font")
    if "overstrike" in estado:
        etiqueta.config(font=("Arial", 12), fg="#333333")
    else:
        etiqueta.config(font=("Arial", 12, "overstrike"), fg="#888888")

root = tk.Tk()
root.title("Lista de Tareas")
root.geometry("500x600")
root.resizable(True, True)
root.config(bg="#f4f4f9")

titulo = tk.Label(
    root,
    text="✅ Mis Tareas",
    font=("Arial", 20, "bold"),
    bg="#f4f4f9",
    fg="#2c3e50"
)
titulo.pack(pady=20)

marco_entrada = tk.Frame(root, bg="#f4f4f9")
marco_entrada.pack(pady=10, padx=20, fill="x")

entrada = tk.Entry(
    marco_entrada,
    font=("Arial", 12),
    bd=2,
    relief="solid"
)
entrada.pack(side="left", fill="x", expand=True, padx=(0, 10))
entrada.bind("<Return>", agregar_tarea)  # Agregar con Enter

boton_agregar = tk.Button(
    marco_entrada,
    text="Agregar",
    bg="#27ae60",
    fg="white",
    font=("Arial", 11, "bold"),
    relief="flat",
    command=agregar_tarea
)
boton_agregar.pack(side="right")

marco_lista = tk.Frame(root, bg="white", bd=2, relief="solid")
marco_lista.pack(pady=10, padx=20, fill="both", expand=True)

scroll = tk.Scrollbar(marco_lista)
scroll.pack(side="right", fill="y")

lista = tk.Frame(marco_lista, bg="white")
lista.pack(fill="both", expand=True)

instruccion = tk.Label(
    lista,
    text="💡 Haz clic en una tarea para marcarla como completada",
    font=("Arial", 10, "italic"),
    fg="#888888",
    bg="white"
)
instruccion.pack(pady=10)

root.mainloop()