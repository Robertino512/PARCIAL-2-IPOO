from Empleado import Empleado
from SituacionLaboral import SituacionLaboral
class EmpleadoContratado(Empleado):
     def __init__(self,nombre:str,documento:int,situacion_laboral:SituacionLaboral,cant_horas:int,valor_hora:float,legajo=None):
            super().__init__(nombre,situacion_laboral,documento,legajo)
            self.__cant_horas:int=cant_horas
            self.__valor_horas:float=valor_hora


     @property
     def get_cant_horas(self):
        return self.__cant_horas
     @property
     def get_valor_hora(self):
           return self.__valor_horas

     @get_cant_horas.setter
     def set_cant_horas(self, cant_horas):
           self.__cant_horas=cant_horas

     @get_valor_hora.setter
     def set_valor_hora(self,nuevoValor):
           self.__valor_horas=nuevoValor
     
     def calcular_remuneracion(self):
              remuneracion=self.__valor_horas*self.__cant_horas
              return remuneracion

     def serializar(self):
            return {
                "tipo": 'contratado',
            "nombre": self.get_nombre,
            "legajo": self.get_legajo,
            "documento": self.get_documento,
            "situacion_laboral": self.get_situacion_laboral.value,
            "cantidad_de_horas": self.get_cant_horas,
            "valor_por_hora": self.get_valor_hora
            }