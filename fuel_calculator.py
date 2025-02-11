import sys, os
import tkinter as tk
from tkinter import ttk
import pandas as pd
import numpy as np
from PIL import Image, ImageTk
import ctypes

myappid = u'agregadosdiaz.fuelcalculator.app'
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)


def resource_path(relative_path):
    """ Retorna la ruta absoluta, compatible con PyInstaller """
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

data = {
  "Medida_pulgadas": [
    0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5, 6.0, 6.5, 7.0, 7.5,
    8.0, 8.5, 9.0, 9.5, 10.0, 10.5, 11.0, 11.5, 12.0, 12.5, 13.0, 13.5, 14.0,
    14.5, 15.0, 15.5, 16.0, 16.5, 17.0, 17.5, 18.0, 18.5, 19.0, 19.5, 20.0,
    20.5, 21.0, 21.5, 22.0, 22.5, 23.0, 23.5, 24.0, 24.5, 25.0, 25.5, 26.0,
    26.5, 27.0, 27.5, 28.0, 28.5, 29.0, 29.5, 30.0, 30.5, 31.0, 31.5, 32.0,
    32.5, 33.0, 33.5, 34.0, 34.5, 35.0, 35.5, 36.0, 36.5, 37.0, 37.5, 38.0,
    38.5, 39.0, 39.5, 40.0, 40.5, 41.0, 41.5, 42.0, 42.5, 43.0, 43.5, 44.0,
    44.5, 45.0, 45.5, 46.0, 46.5, 47.0, 47.5, 48.0, 48.5, 49.0, 49.5, 50.0,
    50.5, 51.0, 51.5, 52.0, 52.5, 53.0, 53.5, 54.0, 54.5, 55.0, 55.5, 56.0,
    56.5, 57.0, 57.5, 58.0, 58.5, 59.0, 59.5, 60.0, 60.5, 61.0, 61.5, 62.0,
    62.5, 63.0, 63.5, 64.0, 64.5, 65.0, 65.5, 66.0, 66.5, 67.0, 67.5, 68.0,
    68.5, 69.0, 69.5, 70.0, 70.5, 71.0, 71.5, 72.0, 72.5, 73.0, 73.5, 74.0,
    74.5, 75.0
  ],
  "Volumen_galones": [
    3, 9, 15, 25, 35, 46, 58, 71, 84, 99, 113, 129, 145, 182, 179, 197, 215,
    234, 253, 273, 293, 313, 334, 356, 377, 399, 421, 444, 467, 490, 514, 538,
    562, 586, 611, 635, 660, 686, 711, 737, 763, 769, 815, 742, 769, 896, 923,
    950, 977, 1005, 1032, 1060, 1088, 1115, 1144, 1172, 1200, 1229, 1257, 1286,
    1315, 1343, 1372, 1401, 1430, 1459, 1488, 1517, 1546, 1575, 1605, 1634,
    1663, 1692, 1721, 1751, 1780, 1809, 1838, 1887, 1897, 1926, 1955, 1984,
    2013, 2042, 2073, 2099, 2128, 2157, 2185, 2214, 2242, 2271, 2299, 2327,
    2355, 2383, 2435, 2454, 2474, 2493, 2520, 2547, 2674, 2661, 2520, 2654,
    2680, 2700, 2732, 2757, 2782, 2807, 2832, 2837, 2887, 2905, 2929, 2953,
    2976, 2999, 3021, 3044, 3066, 3087, 3109, 3129, 3150, 3170, 3190, 3209,
    3228, 3246, 3264, 3281, 3298, 3314, 3329, 3344, 3359, 3372, 3385, 3397,
    3408, 3418, 3426, 3434, 3440, 3453
  ]
}

# Convertir data en un DataFrame una sola vez para mejorar rendimiento
df_measure = pd.DataFrame({
    "Medida pulgadas": data["Medida_pulgadas"],
    "Volumen galones": data["Volumen_galones"]
}).sort_values(by="Medida pulgadas").reset_index(drop=True)


def calculating_available_gasoil(medida_pulgadas: float) -> float:
    """Calcula el volumen en galones mediante interpolación lineal."""
    return np.interp(medida_pulgadas, df_measure["Medida pulgadas"], df_measure["Volumen galones"])


def calculate_gasoil(*args) -> None:
    try:
        measure = measure_entry.get()
        if measure:  # Verificar si hay valor antes de calcular
            measure = float(measure)
            measure_estimate = calculating_available_gasoil(measure)
            result_text.set(f"Gasoil estimado: {round(measure_estimate)} galones")
        else:
            result_text.set("")
    except ValueError:
        result_text.set("Ingrese un valor válido")


# Crear ventana
window = tk.Tk()
window.title("Calculadora de Gasoil")
window.geometry("400x250")
window.resizable(False, False)
window.configure(bg="#F6F6F6")

# Contenedor principal centrado
frame = tk.Frame(window, bg="#F6F6F6")
frame.place(relx=0.5, rely=0.5, anchor="center")

# Imagen del taskbar
icon_path = resource_path("fuel_calculator_ico.ico")
icon = Image.open(icon_path)
icon = ImageTk.PhotoImage(icon)
window.iconphoto(True, icon)

# Título
title_label = ttk.Label(frame, text="Calculadora de Gasoil", font=("Helvetica", 16, "bold"), background="#F6F6F6")
title_label.pack(pady=5)

# Entrada de datos
label_input = ttk.Label(frame, text="Ingrese la medida (pulgadas):", font=("Helvetica", 10), background="#F6F6F6")
label_input.pack()

result_text = tk.StringVar()
measure_entry = tk.StringVar()
measure_entry.trace_add("write", calculate_gasoil)  # Detecta cambios en la entrada y actualiza resultado

measure_input = ttk.Entry(frame, textvariable=measure_entry, width=10, font=("Helvetica", 12))
measure_input.pack(pady=5)

# Mostrar resultado
label_result = ttk.Label(frame, textvariable=result_text, font=("Helvetica", 12), foreground="blue", background="#F6F6F6")
label_result.pack(pady=10)

# Ejecutar la aplicación
window.mainloop()