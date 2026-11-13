from Empleado import Empleado
from Bonificable import Bonificable
from SituacionLaboral import SituacionLaboral
class EmpleadoPermanente(Empleado,Bonificable):
     def __init__(self,nombre:str,documento:int,situacion_laboral:SituacionLaboral, sueldo_basico:float, antiguedad:int,legajo=None):
            super().__init__(nombre,documento,situacion_laboral,legajo)
            self.__sueldo_basico:float=sueldo_basico
            self.__antiguedad:int=antiguedad

     @property
     def get_sueldo_basico(self):
          return self.__sueldo_basico

     @property
     def get_antiguedad(self):
          return self.__antiguedad

     @get_antiguedad.setter
     def set_antiguedad(self,antiguedadNueva):
          self.__antiguedad=antiguedadNueva

     @get_sueldo_basico.setter
     def set_sueldo_basico(self,nuevoSueldo):
          self.__sueldo_basico=nuevoSueldo

     
     

     def calcular_remuneracion(self):
          adicional=self.__antiguedad*0.02
          remuneracion_total=self.__sueldo_basico+adicional
          return remuneracion_total

     def aplicar_bonificacion(self, importe):
        return self.calcular_remuneracion() + importe

     def serializar(self):
          
        return {
            "tipo": "permanente",
            "nombre": self.get_nombre,
            "legajo": self.get_legajo,
            "documento": self.get_documento,
            "situacion_laboral": self.get_situacion_laboral.value,
            "sueldo_basico": self.get_sueldo_basico,
            "antiguedad": self.get_antiguedad
        
                }
     