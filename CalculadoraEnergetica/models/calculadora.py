#models/calculadora.py

class CalculadoraEnergetica:
    '''
    Esta clase representa la logica para calcular indicadores energeticos
    Se le pasan datos de entrada y devuelve un diccionario con los indicadores
    '''

    def __init__(self, m3_gas, mwh, gal_diesel, kg_co2, hl):
        '''
        Inicializa la clase con los datos de entrada necesarios para los calculos.

        :param m3_gas: Volumen de gas natural en m3
        :param mwh: Energia electrica en mwh
        :param gal_diesel: Volumen de diesel en galones
        :param kg_co2: kg de co2 consumidos
        :param hl: hectolitros envasados
        '''

        self.m3_gas = m3_gas
        self.mwh = mwh
        self.gal_diesel = gal_diesel
        self.kg_co2 = kg_co2
        self.hl = hl

        #Constantes de conversion
        self.PCI_GAS_NATURAL = 34.51
        self.PCI_DIESEL = 132.0006
        self.MJ_MWH = 3600

    def calcular(self):
        '''
        Aqui ocurre la magia, hace el calculo
        '''
        if self.hl == 0:
            raise ValueError('Los hectolitros son cero no puede generar indicador especifico')
        
        #Calcular indicador
        mj_gn = self.m3_gas * self.PCI_GAS_NATURAL
        mj_diesel = self.gal_diesel * self.PCI_DIESEL
        mj_electricidad = self.mwh * self.MJ_MWH
        total_energia = mj_gn + mj_diesel + mj_electricidad

        #Retorne los indicadores
        return {
            'CO2 [kg/hL]' : round(self.kg_co2 / self.hl, 2),
            'Termica [MJ/hL]' : round(mj_gn/self.hl, 2),
            'Electrica [kWh/hL]' : round((self.mwh*1000)/self.hl, 2),
            'TPE [MJ/hL]' : round(total_energia/self.hl, 2)
        }
