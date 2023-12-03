# Ejercicio 7
import tkinter as tk

def mostrar_texto():
    texto_ingresado = entrada.get()
    etiqueta_resultado.config(text=f"Texto ingresado: {texto_ingresado}")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Ejercicio 7 - Tkinter")

# Crear un campo de entrada
entrada = tk.Entry(ventana, width=30)
entrada.pack(pady=10)

# Crear un botón que al presionarse llame a la función mostrar_texto
boton_mostrar = tk.Button(ventana, text="Mostrar Texto", command=mostrar_texto)
boton_mostrar.pack(pady=10)

# Crear una etiqueta para mostrar el resultado
etiqueta_resultado = tk.Label(ventana, text="")
etiqueta_resultado.pack(pady=10)

# Iniciar el bucle principal de la aplicación
ventana.mainloop()

# Ejercicio 8
import tkinter as tk

def realizar_operacion(operacion):
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())

        if operacion == "suma":
            resultado = num1 + num2
        elif operacion == "resta":
            resultado = num1 - num2
        elif operacion == "multiplicacion":
            resultado = num1 * num2
        elif operacion == "division":
            resultado = num1 / num2
        else:
            resultado = "Operación no válida"

        etiqueta_resultado.config(text=f"Resultado: {resultado}")

    except ValueError:
        etiqueta_resultado.config(text="Error: Ingrese números válidos")

# Crear la ventana principal
ventana_calculadora = tk.Tk()
ventana_calculadora.title("Calculadora Básica")

# Crear campos de entrada
entry_num1 = tk.Entry(ventana_calculadora, width=15)
entry_num1.grid(row=0, column=0, padx=5, pady=5)

entry_num2 = tk.Entry(ventana_calculadora, width=15)
entry_num2.grid(row=0, column=1, padx=5, pady=5)

# Crear botones de operaciones
boton_suma = tk.Button(ventana_calculadora, text="+", command=lambda: realizar_operacion("suma"))
boton_suma.grid(row=1, column=0, padx=5, pady=5)

boton_resta = tk.Button(ventana_calculadora, text="-", command=lambda: realizar_operacion("resta"))
boton_resta.grid(row=1, column=1, padx=5, pady=5)

boton_multiplicacion = tk.Button(ventana_calculadora, text="*", command=lambda: realizar_operacion("multiplicacion"))
boton_multiplicacion.grid(row=2, column=0, padx=5, pady=5)

boton_division = tk.Button(ventana_calculadora, text="/", command=lambda: realizar_operacion("division"))
boton_division.grid(row=2, column=1, padx=5, pady=5)

# Crear etiqueta para mostrar el resultado
etiqueta_resultado = tk.Label(ventana_calculadora, text="Resultado:")
etiqueta_resultado.grid(row=3, column=0, columnspan=2, pady=10)

# Iniciar el bucle principal de la aplicación
ventana_calculadora.mainloop()

# Ejercicio 9
import tkinter as tk

def cambiar_color(color):
    ventana.configure(bg=color)

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Cambiar Color de Fondo")

# Crear botones con diferentes colores
boton_rojo = tk.Button(ventana, text="Rojo", command=lambda: cambiar_color("red"))
boton_rojo.pack(side=tk.LEFT, padx=5)

boton_verde = tk.Button(ventana, text="Verde", command=lambda: cambiar_color("green"))
boton_verde.pack(side=tk.LEFT, padx=5)

boton_azul = tk.Button(ventana, text="Azul", command=lambda: cambiar_color("blue"))
boton_azul.pack(side=tk.LEFT, padx=5)

# Iniciar el bucle principal de la aplicación
ventana.mainloop()

#Ejercicio 10
import tkinter as tk
from tkinter import ttk

def mostrar_mensaje():
    opcion_seleccionada = lista_desplegable.get()
    etiqueta_resultado.config(text=f"Seleccionaste: {opcion_seleccionada}")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Interfaz con Lista Desplegable")

# Crear una lista de opciones
opciones = ["Opción 1", "Opción 2", "Opción 3", "Opción 4"]

# Crear una lista desplegable
lista_desplegable = ttk.Combobox(ventana, values=opciones)
lista_desplegable.pack(pady=10)

# Seleccionar la primera opción por defecto
lista_desplegable.set(opciones[0])

# Crear un botón para mostrar el mensaje
boton_mostrar = tk.Button(ventana, text="Mostrar Mensaje", command=mostrar_mensaje)
boton_mostrar.pack(pady=10)

# Crear una etiqueta para mostrar el resultado
etiqueta_resultado = tk.Label(ventana, text="")
etiqueta_resultado.pack(pady=10)

# Iniciar el bucle principal de la aplicación
ventana.mainloop()

