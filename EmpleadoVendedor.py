from Empleado import Empleado
from Bonificable import Bonificable
from SituacionLaboral import SituacionLaboral
class EmpleadoVendedor(Empleado,Bonificable):
    def __init__(self,nombre:str,documento:int,situacion_laboral:SituacionLaboral,sueldo_basico:float,ventas_mensuales:int,legajo=None):
        super().__init__(nombre,documento,situacion_laboral,legajo)
        self.__ventas:int=ventas_mensuales
        self.__sueldo_basico:float=sueldo_basico

    @property
    def get_sueldo_basico(self):
              return self.__sueldo_basico

    @property
    def get_ventas(self):
         return self.__ventas

    @get_sueldo_basico.setter
    def set_sueldo_basico(self,nuevoSueldo):
        self.__sueldo_basico=nuevoSueldo

    @get_ventas.setter
    def set_ventas(self,nuevasVentas):
         self.__ventas=nuevasVentas


    def calcular_remuneracion(self):
        remuneracion= self.__sueldo_basico+(self.__ventas*0.05)
        return remuneracion

    
    def aplicar_bonificacion(self, importe):
        return self.calcular_remuneracion() + importe

    def serializar(self):
              
            return {
                "tipo": "vendedor",
                "nombre": self.get_nombre,
                "legajo": self.get_legajo,
                "documento": self.get_documento,
                "situacion_laboral": self.get_situacion_laboral.value,
                "sueldo_basico": self.get_sueldo_basico,
                "ventas_mensuales": self.get_ventas
            
                    }