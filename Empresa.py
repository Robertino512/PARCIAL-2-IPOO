from SituacionLaboral import SituacionLaboral
import json
from EmpleadoContratado import EmpleadoContratado
from EmpleadoPermanente import EmpleadoPermanente
from EmpleadoVendedor import EmpleadoVendedor
class Empresa:
    def __init__(self, nombre):
        self.__nombre = nombre
        self.__empleados = []

    @property
    def get_nombre(self):
        return self.__nombre

    @property
    def get_empleados(self):
        return self.__empleados
    
    @property
    def cantidad_empleados(self):
     return len(self.__empleados)

    def registrar_empleado(self, empleado):
        for i in self.__empleados:
            if i.get_legajo == empleado.get_legajo:
                print("Ya existe un empleado con ese legajo")
                return

        else:    
            self.__empleados.append(empleado)
            print("Empleado regisrtado correctamente")

    def calcular_total_sueldos(self):
        total = 0

        for empleado in self.__empleados:
            if empleado.get_situacion_laboral== SituacionLaboral.ACTIVO:
                total+=empleado.liquidar_sueldo()

        return total

    def serializar_todo(self):
        datos = []
        for empleado in self.__empleados:
            datos.append(empleado.serializar())

        return json.dumps(datos)
    

    def deserializar_todo(self, data1):
        datos = json.loads(data1)

        self.__empleados = [] #evito elementos duplicados

        for data in datos:
            empleado = Empresa.deserializar_empleado(data)
            self.__empleados.append(empleado)

    

    @staticmethod
    def deserializar_empleado(data):

        if data["tipo"] == "vendedor":
            return EmpleadoVendedor.deserializar(data)

        elif data["tipo"] == "permanente":
            return EmpleadoPermanente.deserializar(data)

        elif data["tipo"] == "contratado":
            return EmpleadoContratado.deserializar(data)
        else:
            raise ValueError("No se conoce el tipo de empelado")