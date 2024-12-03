import tkinter as tk
from tkinter import messagebox

def registrar():
    nombre = entrada_nombre.get()
    correo = entrada_correo.get()
    fecha_nacimiento = entrada_fecha.get()
    contrasena = entrada_contrasena.get()
    repetir_contrasena = entrada_repetir_contrasena.get()

    # Valida contraseñas
    if contrasena != repetir_contrasena:
        messagebox.showerror("Error", "Las contraseñas no coinciden.")
        return

    # Crea ventana emergente para mostrar los datos
    ventana_datos = tk.Toplevel(ventana_principal)
    ventana_datos.title("Datos registrados")
    ventana_datos.geometry("300x200")

    tk.Label(ventana_datos, text=f"Nombre completo: {nombre}", anchor="w").pack(fill="x")
    tk.Label(ventana_datos, text=f"Correo electronico: {correo}", anchor="w").pack(fill="x")
    tk.Label(ventana_datos, text=f"Fecha de nacimiento: {fecha_nacimiento}", anchor="w").pack(fill="x")

# Crear ventana principal
ventana_principal = tk.Tk()
ventana_principal.title("Formulario de registro")
ventana_principal.geometry("400x300")

# Etiquetas y campos de entrada
etiqueta_nombre = tk.Label(ventana_principal, text="Nombre completo:")
etiqueta_nombre.pack(anchor="w", padx=10, pady=2)
entrada_nombre = tk.Entry(ventana_principal)
entrada_nombre.pack(fill="x", padx=10, pady=2)

etiqueta_correo = tk.Label(ventana_principal, text="Correo electronico:")
etiqueta_correo.pack(anchor="w", padx=10, pady=2)
entrada_correo = tk.Entry(ventana_principal)
entrada_correo.pack(fill="x", padx=10, pady=2)

etiqueta_fecha = tk.Label(ventana_principal, text="Fecha de nacimiento:")
etiqueta_fecha.pack(anchor="w", padx=10, pady=2)
entrada_fecha = tk.Entry(ventana_principal)
entrada_fecha.pack(fill="x", padx=10, pady=2)

etiqueta_contrasena = tk.Label(ventana_principal, text="Contraseña:")
etiqueta_contrasena.pack(anchor="w", padx=10, pady=2)
entrada_contrasena = tk.Entry(ventana_principal, show="*")
entrada_contrasena.pack(fill="x", padx=10, pady=2)

etiqueta_repetir_contrasena = tk.Label(ventana_principal, text="Repetir contraseña:")
etiqueta_repetir_contrasena.pack(anchor="w", padx=10, pady=2)
entrada_repetir_contrasena = tk.Entry(ventana_principal, show="*")
entrada_repetir_contrasena.pack(fill="x", padx=10, pady=2)

# Boton de envio
boton_registrar = tk.Button(ventana_principal, text="Registrar", command=registrar)
boton_registrar.pack(pady=20)
#para la ejecucion
ventana_principal.mainloop()
