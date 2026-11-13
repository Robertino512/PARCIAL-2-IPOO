from abc import ABC, abstractmethod
from SituacionLaboral import SituacionLaboral
class Empleado(ABC):
    legajos=0
    def __init__(self,nombre:str,documento:int,situacion_laboral:SituacionLaboral,legajo=None):
        self.__nombre:str=nombre
        self.__legajo:str=legajo if legajo is not None else Empleado.generar_legajo() 
        self.__documento:int=documento
        self.__situacion_laboral:str=situacion_laboral

    #GETTERS
    @property
    def get_nombre(self):
        return self.__nombre
    @property
    def get_legajo(self):
            return self.__legajo
    @property
    def get_documento(self):
            return self.__documento
    @property
    def get_situacion_laboral(self):
            return self.__situacion_laboral

    #SETTERS

    @get_nombre.setter
    def set_nombre(self,nuevoNombre):
          self.__nombre=nuevoNombre

    @get_documento.setter
    def set_documento(self,nuevoDoc):
          if self.validar_documento(nuevoDoc):
            self.__documento = nuevoDoc
          else:
                print ('Para cambiar el documento, el mismo debe ser de entre 7 y 8 caracteres ')

    @get_situacion_laboral.setter
    def set_situacion_laboral(self,sit_lab):
          self.__situacion_laboral=sit_lab

    @classmethod
    def generar_legajo(cls):
          cls.legajos+=1
          return cls.legajos

    @staticmethod
    def validar_documento(documento):

        documento = str(documento) #convierto a str temporalmente para poder usar len por que int no lo permite
        if 7 <= len(documento) <= 8:
              return True
        return False

    @abstractmethod
    def calcular_remuneracion(self):
          pass

    def liquidar_sueldo(self):
        if self.situacion_laboral == SituacionLaboral.ACTIVO:
            return self.calcular_remuneracion()
        else:
            raise ValueError("El empleado no se encuentra activo")  

    def serializar(self):
        return {

        "nombre": self.get_nombre,
        "legajo": self.get_legajo,
        "documento": self.get_documento,
        "situacion_laboral": self.get_situacion_laboral.value,
        }
    
    @classmethod
    def deserializar(cls,data):
        data = data.copy() 
        data.pop("tipo")
        data['situacion_laboral']=SituacionLaboral(data['situacion_laboral'])
        return cls(**data)