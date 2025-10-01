#ui/formulario.py

import tkinter as tk
from tkinter import messagebox
from models.calculadora import CalculadoraEnergetica

class FormularioCalculadora:
    def __init__(self, root):
        self.root = root
        self.root.title('Calculadora indicadores energeticos')
        self.root.geometry('400x450')
        self.root.resizable(False, False)

        #Diccionario que guarda las entradas al usuario
        self.entradas = {}

        #Campos a mostrar
        campos = [
            ('m3 de gas natural', 'm3_gas'),
            ('MWh electricos', 'mwh'),
            ('Galones de diesel', "gal_diesel"),
            ('kg de CO2', 'kg_co2'),
            ('Hectolitros envasados', 'hl') 
        ]

        #Crear etiquetas y entradas de texto
        #idx = index
        for idx, (label_text, key) in enumerate(campos):
            tk.Label(root, text=label_text).grid(row=idx, column=0, padx=10, pady=10, sticky='w')
            entrada = tk.Entry(root)
            entrada.grid(row=idx, column=0, columnspan=2, padx=10)
            self.entradas[key] = entrada

        calcular_btn = tk.Button(root, text='Calcular', command = self.calcular)
        calcular_btn.grid(row=len(campos), column = 0, columnspan = 2, pady=20)

        self.resultados_text = tk.Text(root, height=8, width=45, state='disabled', bg='#f5f5f5')
        self.resultados_text.grid(row=len(campos)+1, column=0, columnspan=2, padx=10)



    def calcular(self):
        try:
            #Obtener entradas
            m3_gas = float(self.entradas['m3_gas'].get())
            mwh = float(self.entradas['mwh'].get())
            gal_diesel = float(self.entradas['gal_diesel'].get())
            kg_co2 = float(self.entradas['kg_co2'].get())
            hl = float(self.entradas['hl'].get())

            calc = CalculadoraEnergetica(m3_gas, mwh, gal_diesel, kg_co2, hl)
            resultados = calc.calcular()

            #Resultados
            self.resultados_text.config(state='normal')
            self.resultados_text.delete('1.0', tk.END)
            for clave, valor in resultados.items():
                self.resultados_text.insert(tk.END, f'{clave}: {valor}\n')
            self.resultados_text.config(state = 'disabled')

        except ValueError:

            messagebox.showerror('Error', 'Todos los campos deben contener numeros validos')
