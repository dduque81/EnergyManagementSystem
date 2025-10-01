import tkinter as tk
from tkinter import messagebox
import csv
from datetime import datetime
from data.conexion import obtener_conexion


class RegistroManual:
    def __init__(self, root):
        self.root = root
        self.root.title('Registro manual')
        self.root.geometry('600x800')


        #Fecha
        tk.Label(root, text = 'Fecha (YYYY-MM-DD)').grid(row=0, column =0, padx = 10, pady = 5, sticky='w')
        self.fecha_entry = tk.Entry(root)
        self.fecha_entry.grid(row=0, column = 1)

        #Hectolitros
        #Can
        tk.Label(root, text = 'Hectolitros CAN').grid(row=1, column = 0, padx = 10, pady = 5, sticky = 'w')
        self.hectolitros_can_entry = tk.Entry(root)
        self.hectolitros_can_entry.grid(row=1, column = 1)
        #RGB
        tk.Label(root, text = 'Hectolitros RGB').grid(row=2, column=0, padx=10, pady=5, sticky='w')
        self.hectolitros_rgb_entry = tk.Entry(root)
        self.hectolitros_rgb_entry.grid(row=2, column = 1)

        #Filtrados
        tk.Label(root, text = 'Hectolitros filtrados').grid(row=3, column=0, padx=10, pady=5, sticky='w')
        self.hectolitros_filtrados_entry = tk.Entry(root)
        self.hectolitros_filtrados_entry.grid(row=3, column =1)

        #DAW
        tk.Label(root, text = 'Hectolitros DAW').grid(row=4, column=0, padx=10, pady=5, sticky='w')
        self.hectolitros_daw_entry = tk.Entry(root)
        self.hectolitros_daw_entry.grid(row=4, column = 1)

        #Cocimientos
        tk.Label(root, text = 'Cocimientos').grid(row=5, column=0, padx=10, pady=5, sticky= 'w')
        self.cocimientos_entry = tk.Entry(root)
        self.cocimientos_entry.grid(row=5, column=1)

        #Gas natural
        tk.Label(root, text = 'm3 de gas natural').grid(row=6, column=0, padx=10, pady=5, sticky= 'w')
        self.m3_gas_nat_entry = tk.Entry(root)
        self.m3_gas_nat_entry.grid(row=6, column=1)

        #MWH electrica
        #tk.Label(root, text = 'MWh cerv').grid(row=7, column=0, padx=10, pady=5, sticky= 'w')
        #self.mwh_entry = tk.Entry(root)
        #self.mwh_entry.grid(row=7, column=1)

        #ACPM
        tk.Label(root, text = 'Galones ACPM').grid(row=7, column=0, padx=10, pady=5, sticky= 'w')
        self.galones_acpm_entry = tk.Entry(root)
        self.galones_acpm_entry.grid(row=7, column=1)

        #CO2
        #tk.Label(root, text = 'CO2 consumido').grid(row=9, column=0, padx=10, pady=5, sticky= 'w')
        #self.co2_cons_entry = tk.Entry(root)
        #self.co2_cons_entry.grid(row=9, column=1)

        #Consumos de energia electrica
        #Calderas
        tk.Label(root, text = 'MWh Calderas').grid(row=8, column=0, padx=10, pady=5, sticky= 'w')
        self.mwh_cald_entry = tk.Entry(root)
        self.mwh_cald_entry.grid(row=8, column=1)
        #Refrig 05
        tk.Label(root, text = 'MWh Refrig 05').grid(row=9, column=0, padx=10, pady=5, sticky= 'w')
        self.refri_05_entry = tk.Entry(root)
        self.refri_05_entry.grid(row=9, column=1)
        #Refrig 06
        tk.Label(root, text = 'MWh Refrig 06').grid(row=10, column=0, padx=10, pady=5, sticky= 'w')
        self.refri_06_entry = tk.Entry(root)
        self.refri_06_entry.grid(row=10, column=1)
        #CO2-Air
        tk.Label(root, text = 'MWh CO2-Air').grid(row=11, column=0, padx=10, pady=5, sticky= 'w')
        self.mwh_co2_air_entry = tk.Entry(root)
        self.mwh_co2_air_entry.grid(row=11, column=1)
        #WTP-BTS
        tk.Label(root, text = 'MWh WTP-BTS').grid(row=12, column=0, padx=10, pady=5, sticky= 'w')
        self.mwh_wtp_bts_entry = tk.Entry(root)
        self.mwh_wtp_bts_entry.grid(row=12, column=1)
        #Filtro
        tk.Label(root, text = 'MWh filtro').grid(row=13, column=0, padx=10, pady=5, sticky= 'w')
        self.mwh_filtro_entry = tk.Entry(root)
        self.mwh_filtro_entry.grid(row=13, column=1)
        #Ferment
        tk.Label(root, text = 'MWh Brewhouse 01').grid(row=14, column=0, padx=10, pady=5, sticky= 'w')
        self.mwh_ferment_entry = tk.Entry(root)
        self.mwh_ferment_entry.grid(row=14, column=1)
        #CAN
        tk.Label(root, text = 'MWh Latas - L3').grid(row=15, column=0, padx=10, pady=5, sticky= 'w')
        self.mwh_l3_entry = tk.Entry(root)
        self.mwh_l3_entry.grid(row=15, column=1)
        #RGB
        tk.Label(root, text = 'MWh RGB - L5').grid(row=16, column=0, padx=10, pady=5, sticky= 'w')
        self.mwh_l5_entry = tk.Entry(root)
        self.mwh_l5_entry.grid(row=16, column=1)
        #Amenities
        tk.Label(root, text = 'MWh amenities').grid(row=17, column=0, padx=10, pady=5, sticky= 'w')
        self.mwh_amenities_entry = tk.Entry(root)
        self.mwh_amenities_entry.grid(row=17, column=1)
        #Warehouse
        tk.Label(root, text = 'MWh Warehouse').grid(row=18, column=0, padx=10, pady=5, sticky= 'w')
        self.mwh_warehouse_entry = tk.Entry(root)
        self.mwh_warehouse_entry.grid(row=18, column=1)
        #CO2 comprado
        tk.Label(root, text = 'CO2 comprado').grid(row=6, column=2, padx=10, pady=5, sticky= 'w')
        self.co2_comprado_entry = tk.Entry(root)
        self.co2_comprado_entry.grid(row=6, column=3)
        #CO2 recuperado
        tk.Label(root, text = 'CO2 recuperado').grid(row=7, column=2, padx=10, pady=5, sticky= 'w')
        self.co2_recuperado_entry = tk.Entry(root)
        self.co2_recuperado_entry.grid(row=7, column=3)
        #CO2 inventario
        tk.Label(root, text = 'CO2 inventario').grid(row=8, column=2, padx=10, pady=5, sticky= 'w')
        self.co2_inventario_entry = tk.Entry(root)
        self.co2_inventario_entry.grid(row=8, column=3)
        #CO2 8 Bar
        tk.Label(root, text = 'CO2 8 Bar').grid(row=9, column=2, padx=10, pady=5, sticky= 'w')
        self.co2_8bar_entry = tk.Entry(root)
        self.co2_8bar_entry.grid(row=9, column=3)
        #CO2 filtracion
        tk.Label(root, text = 'CO2 filtracion').grid(row=10, column=2, padx=10, pady=5, sticky= 'w')
        self.co2_filtracion_entry = tk.Entry(root)
        self.co2_filtracion_entry.grid(row=10, column=3)
        #CO2 ccts
        tk.Label(root, text = 'CO2 ccts').grid(row=11, column=2, padx=10, pady=5, sticky= 'w')
        self.co2_ccts_entry = tk.Entry(root)
        self.co2_ccts_entry.grid(row=11, column=3)
        #CO2 bbts
        tk.Label(root, text = 'CO2 bbts').grid(row=12, column=2, padx=10, pady=5, sticky= 'w')
        self.co2_bbts_entry = tk.Entry(root)
        self.co2_bbts_entry.grid(row=12, column=3)
        #CO2 12 Bar pack y otros
        tk.Label(root, text = 'CO2 linea 12 Bar pack').grid(row=13, column=2, padx=10, pady=5, sticky='w')
        self.co2_12bar_line_entry = tk.Entry(root)
        self.co2_12bar_line_entry.grid(row=13, column=3)
        #CO2 CAN
        tk.Label(root, text = 'CO2 CAN').grid(row=14, column=2, padx=10, pady=5, sticky='w')
        self.co2_can_entry = tk.Entry(root)
        self.co2_can_entry.grid(row=14, column=3)
        #CO2 RGB
        tk.Label(root, text = 'CO2 RGB').grid(row=15, column=2, padx=10, pady=5, sticky='w')
        self.co2_rgb_entry = tk.Entry(root)
        self.co2_rgb_entry.grid(row=15, column=3)
        #CO2 DAW
        tk.Label(root, text = 'CO2 DAW').grid(row=16, column=2, padx=10, pady=5, sticky='w')
        self.co2_daw_entry = tk.Entry(root)
        self.co2_daw_entry.grid(row=16, column=3)
        #CO2 Brewhouse
        tk.Label(root, text = 'CO2 Brewhouse').grid(row=17, column=2, padx=10, pady=5, sticky='w')
        self.co2_brewhouse_entry = tk.Entry(root)
        self.co2_brewhouse_entry.grid(row=17, column=3)

        #Boton ejecuta y guarda lo registrado
        tk.Button(root, text = 'Guardar datos', command = self.guardar_datos).grid(row=19, column = 0, columnspan=2, pady=20)


    def guardar_datos(self):
        try:
            #Leer los valores ingresados al formulario
            fecha = self.fecha_entry.get()
            #print(fecha)
            hl_can = float(self.hectolitros_can_entry.get())
            hl_rgb = float(self.hectolitros_rgb_entry.get())
            hl_filt = float(self.hectolitros_filtrados_entry.get())
            hl_daw = float(self.hectolitros_daw_entry.get())
            coc = float(self.cocimientos_entry.get())
            gas_nat = float(self.m3_gas_nat_entry.get())
            gal_acpm = float(self.galones_acpm_entry.get())
            mwh_cald = float(self.mwh_cald_entry.get())
            mwh_refrig05 = float(self.refri_05_entry.get())
            mwh_refrig06 = float(self.refri_06_entry.get())
            mwh_co2_air = float(self.mwh_co2_air_entry.get())
            mwh_wtp_bts = float(self.mwh_wtp_bts_entry.get())
            mwh_filtro = float(self.mwh_filtro_entry.get())
            mwh_ferment = float(self.mwh_ferment_entry.get())
            mwh_can = float(self.mwh_l3_entry.get())
            mwh_rgb = float(self.mwh_l5_entry.get())
            mwh_amenities = float(self.mwh_amenities_entry.get())
            mwh_warehouse = float(self.mwh_warehouse_entry.get())
            co2_comprado = float(self.co2_comprado_entry.get())
            co2_recuperado = float(self.co2_recuperado_entry.get())
            co2_inventario = float(self.co2_inventario_entry.get())
            co2_8bar = float(self.co2_8bar_entry.get())
            co2_filtracion = float(self.co2_12bar_line_entry.get())
            co2_ccts = float(self.co2_ccts_entry.get())
            co2_bbts = float(self.co2_bbts_entry.get())
            co2_12bar = float(self.co2_12bar_line_entry.get())
            co2_can = float(self.co2_can_entry.get())
            co2_rgb = float(self.co2_rgb_entry.get())
            co2_daw = float(self.co2_daw_entry.get())
            co2_brewhouse = float(self.co2_brewhouse_entry.get())


            #Validar fecha (Opcional - pero util para garantizar calidad del dato)
            fecha_obj = datetime.strptime(fecha, "%Y-%m-%d")

            conexion = obtener_conexion()
            cursor = conexion.cursor()
            cursor.execute("""
                INSERT INTO registros_1 (fecha, hl_can, hl_rgb, hl_filt, hl_daw, cocimientos, gas_nat, gal_acpm, mwh_cald, mwh_refrig05, mwh_refrig06, mwh_co2air, mwh_wtp, mwh_filtro, mwh_ferment, mwh_can, mwh_rgb, mwh_amenities, mwh_warehouse, co2_comp, co2_recup, co2_invent, co2_8bar, co2_filtr, co2_ccts, co2_bbts, co2_12bar, co2_can, co2_rgb, co2_daw, co2_brewh)
                           VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                           """, (fecha_obj, hl_can, hl_rgb, hl_filt, hl_daw, coc, gas_nat, gal_acpm, mwh_cald, mwh_refrig05, mwh_refrig06, mwh_co2_air, mwh_wtp_bts, mwh_filtro, mwh_ferment, mwh_can, mwh_rgb, mwh_amenities, mwh_warehouse, co2_comprado, co2_recuperado, co2_inventario, co2_8bar, co2_filtracion, co2_ccts, co2_bbts, co2_12bar, co2_can, co2_rgb, co2_daw, co2_brewhouse))
            conexion.commit()
            cursor.close()
            conexion.close()

            messagebox.showinfo('Exito', 'Registro procesado correctamente')

        except ValueError:
            messagebox.showerror('Error', 'Revisar los valores ingresados')


    