import tkinter as tk
from tkinter import messagebox

def agregar_valor(valor):
    pantalla.insert(tk.END, valor)

def limpiar():
    pantalla.delete(0, tk.END)

def borrar_ultimo():
    texto = pantalla.get()
    pantalla.delete(0, tk.END)
    pantalla.insert(0, texto[:-1])

def calcular():
    try:
        resultado = eval(pantalla.get())
        pantalla.delete(0, tk.END)
        pantalla.insert(0, str(resultado))
    except Exception:
        pantalla.delete(0, tk.END)
        pantalla.insert(0, "Error")
        root.after(1500, lambda: pantalla.delete(0, tk.END))

root = tk.Tk()
root.title("Calculadora")
root.geometry("350x450")
root.resizable(False, False)
root.config(bg="#f0f0f5")

pantalla = tk.Entry(
    root,
    font=("Arial", 24),
    justify="right",
    bd=5,
    bg="#ffffff"
)
pantalla.pack(pady=15, padx=15, fill="x")

marco = tk.Frame(root, bg="#f0f0f5")
marco.pack(padx=10, pady=5, fill="both", expand=True)

botones = [
    ("C", 0, 0, limpiar, "#e74c3c"),
    ("/", 0, 1, lambda: agregar_valor("/"), "#3498db"),
    ("×", 0, 2, lambda: agregar_valor("*"), "#3498db"),
    ("←", 0, 3, borrar_ultimo, "#f39c12"),
    
    ("7", 1, 0, lambda: agregar_valor("7"), "#3498db"),
    ("8", 1, 1, lambda: agregar_valor("8"), "#3498db"),
    ("9", 1, 2, lambda: agregar_valor("9"), "#3498db"),
    ("-", 1, 3, lambda: agregar_valor("-"), "#3498db"),
    
    ("4", 2, 0, lambda: agregar_valor("4"), "#3498db"),
    ("5", 2, 1, lambda: agregar_valor("5"), "#3498db"),
    ("6", 2, 2, lambda: agregar_valor("6"), "#3498db"),
    ("+", 2, 3, lambda: agregar_valor("+"), "#3498db"),
    
    ("1", 3, 0, lambda: agregar_valor("1"), "#3498db"),
    ("2", 3, 1, lambda: agregar_valor("2"), "#3498db"),
    ("3", 3, 2, lambda: agregar_valor("3"), "#3498db"),
    ("=", 3, 3, calcular, "#e74c3c"),
    
    ("0", 4, 0, lambda: agregar_valor("0"), "#3498db"),
    (".", 4, 2, lambda: agregar_valor("."), "#3498db"),
]

for texto, fila, columna, comando, color in botones:
    ancho = 2 if texto == "0" else 1
    alto = 2 if texto == "=" else 1
    btn = tk.Button(
        marco,
        text=texto,
        font=("Arial", 16, "bold"),
        bg=color,
        fg="white",
        relief="flat",
        command=comando
    )
    btn.grid(
        row=fila,
        column=columna,
        columnspan=ancho,
        rowspan=alto,
        padx=5,
        pady=5,
        sticky="nsew"
    )

for i in range(4):
    marco.grid_columnconfigure(i, weight=1)
for i in range(5):
    marco.grid_rowconfigure(i, weight=1)

root.mainloop()