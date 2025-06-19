import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk

# Colores y estilo
COLOR_PRIMARIO = "#4F6BA0"
COLOR_SECUNDARIO = "#A9C4E3"
FONDO = "#F5F5F5"
TEXTO = "#333333"

# Función: Gestión de Médicos
def abrir_gestion_medicos():
    ventana = tk.Toplevel(root)
    ventana.title("Gestión de Médicos")
    ventana.configure(bg=FONDO)

    tk.Label(ventana, text="Nombre:", bg=FONDO).grid(row=0, column=0, padx=5, pady=5)
    tk.Entry(ventana).grid(row=0, column=1, padx=5, pady=5)

    tk.Label(ventana, text="Numero de identificación:", bg=FONDO).grid(row=1, column=0, padx=5, pady=5)
    tk.Entry(ventana).grid(row=1, column=1, padx=5, pady=5)

    tk.Label(ventana, text="Fecha de Nacimiento:", bg=FONDO).grid(row=2, column=0, padx=5, pady=5)
    tk.Entry(ventana).grid(row=2, column=1, padx=5, pady=5)

    ttk.Button(ventana, text="Confirmar", command=lambda: messagebox.showinfo("Confirmado", "Médico agregado")).grid(row=3, column=0, columnspan=2, pady=10)

# Función: Gestión de Condiciones
def abrir_gestion_condiciones():
    ventana = tk.Toplevel(root)
    ventana.title("Gestión de Condiciones")
    ventana.configure(bg=FONDO)

    tk.Label(ventana, text="Médico:", bg=FONDO).grid(row=0, column=0, padx=5, pady=5)
    ttk.Combobox(ventana, values=["Dr. David", "Dra. Sash"]).grid(row=0, column=1, padx=5, pady=5)

    tk.Label(ventana, text="Condición:", bg=FONDO).grid(row=1, column=0, padx=5, pady=5)
    ttk.Combobox(ventana, values=["Cumpleaños", "Descanso", "Incapacidad"]).grid(row=1, column=1, padx=5, pady=5)

    tk.Label(ventana, text="Fecha:", bg=FONDO).grid(row=2, column=0, padx=5, pady=5)
    tk.Entry(ventana).grid(row=2, column=1, padx=5, pady=5)

    ttk.Button(ventana, text="Confirmar", command=lambda: messagebox.showinfo("Condición", "Condición registrada")).grid(row=3, column=0, columnspan=2, pady=10)

# Función base para mostrar mensaje
def abrir_mensaje(titulo):
    messagebox.showinfo(titulo, f"Ventana de {titulo}")

# --- Ventana principal ---
root = tk.Tk()
root.title("Clínica Vida – Gestión de Turnos")
root.geometry("500x620")
root.configure(bg=FONDO)

# Logo (opcional, colocar tu logo.png en el mismo directorio)
try:
    logo = Image.open("logo.png")
    logo = logo.resize((200, 80))
    logo_img = ImageTk.PhotoImage(logo)
    tk.Label(root, image=logo_img, bg=FONDO).pack(pady=10)
except:
    tk.Label(root, text="Clínica Vida", font=("Helvetica", 18, "bold"), bg=FONDO, fg=COLOR_PRIMARIO).pack(pady=10)

# Estilo de botones
style = ttk.Style()
style.theme_use("clam")
style.configure("TButton", font=("Helvetica", 11), padding=10, background=COLOR_PRIMARIO, foreground="white")
style.map("TButton", background=[('active', COLOR_SECUNDARIO)])

# Título
tk.Label(root, text="Menú Principal", font=("Helvetica", 14, "bold"), bg=FONDO, fg=COLOR_PRIMARIO).pack(pady=5)

# Botones
ttk.Button(root, text="Gestión de Médicos", command=abrir_gestion_medicos).pack(pady=5, fill="x", padx=40)
ttk.Button(root, text="Gestión de Condiciones", command=abrir_gestion_condiciones).pack(pady=5, fill="x", padx=40)
ttk.Button(root, text="Gestión normativa legal", command=lambda: abrir_mensaje("Normativa Legal")).pack(pady=5, fill="x", padx=40)
ttk.Button(root, text="Gestión normativa interna", command=lambda: abrir_mensaje("Normativa Interna")).pack(pady=5, fill="x", padx=40)
ttk.Button(root, text="Instructivo", command=lambda: abrir_mensaje("Instructivo")).pack(pady=5, fill="x", padx=40)
ttk.Button(root, text="Generar cuadro de turnos", command=lambda: abrir_mensaje("Generar Cuadro")).pack(pady=5, fill="x", padx=40)
ttk.Button(root, text="Exportar a Excel", command=lambda: abrir_mensaje("Exportar a Excel")).pack(pady=5, fill="x", padx=40)

root.mainloop()