import tkinter as tk

def cifrar_cesar(mensaje, desplazamiento):
    mensaje_cifrado = ""
    for letra in mensaje:
        if letra.isalpha():
            is_upper = letra.isupper()
            letra = letra.lower()
            indice = ord(letra) - ord('a')
            indice_cifrado = (indice + desplazamiento) % 26
            letra_cifrada = chr(ord('a') + indice_cifrado)
            if is_upper:
                letra_cifrada = letra_cifrada.upper()
            mensaje_cifrado += letra_cifrada
        else:
            mensaje_cifrado += letra
    return mensaje_cifrado

def descifrar_cesar(mensaje_cifrado, desplazamiento):
    return cifrar_cesar(mensaje_cifrado, -desplazamiento)

def cifrar_click():
    mensaje_original = mensaje_input.get()
    desplazamiento = int(desplazamiento_input.get())
    mensaje_cifrado = cifrar_cesar(mensaje_original, desplazamiento)
    mensaje_cifrado_output.config(text="Mensaje cifrado: " + mensaje_cifrado)

def descifrar_click():
    mensaje_cifrado = mensaje_cifrado_input.get()
    desplazamiento = int(desplazamiento_descifrado_input.get())
    mensaje_descifrado = descifrar_cesar(mensaje_cifrado, desplazamiento)
    mensaje_descifrado_output.config(text="Mensaje descifrado: " + mensaje_descifrado)

# Configuración de la ventana
root = tk.Tk()
root.title("Cifrador César")

# Etiquetas
mensaje_label = tk.Label(root, text="Mensaje:")
mensaje_label.grid(row=0, column=0)

desplazamiento_label = tk.Label(root, text="Desplazamiento:")
desplazamiento_label.grid(row=1, column=0)

mensaje_cifrado_label = tk.Label(root, text="Mensaje cifrado:")
mensaje_cifrado_label.grid(row=3, column=0)

desplazamiento_descifrado_label = tk.Label(root, text="Desplazamiento:")
desplazamiento_descifrado_label.grid(row=4, column=0)

# Campos de entrada
mensaje_input = tk.Entry(root)
mensaje_input.grid(row=0, column=1)

desplazamiento_input = tk.Entry(root)
desplazamiento_input.grid(row=1, column=1)

mensaje_cifrado_input = tk.Entry(root)
mensaje_cifrado_input.grid(row=3, column=1)

desplazamiento_descifrado_input = tk.Entry(root)
desplazamiento_descifrado_input.grid(row=4, column=1)

# Botones
cifrar_button = tk.Button(root, text="Cifrar", command=cifrar_click)
cifrar_button.grid(row=2, column=0, columnspan=2)

descifrar_button = tk.Button(root, text="Descifrar", command=descifrar_click)
descifrar_button.grid(row=5, column=0, columnspan=2)

# Etiquetas para mostrar el resultado
mensaje_cifrado_output = tk.Label(root, text="")
mensaje_cifrado_output.grid(row=6, column=0, columnspan=2)

mensaje_descifrado_output = tk.Label(root, text="")
mensaje_descifrado_output.grid(row=7, column=0, columnspan=2)

root.mainloop()
