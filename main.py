from Empresa import Empresa
from Empleado import Empleado
from EmpleadoVendedor import EmpleadoVendedor
from EmpleadoPermanente import EmpleadoPermanente
from EmpleadoContratado import EmpleadoContratado
from SituacionLaboral import SituacionLaboral
from Empresa import Empresa
from Empleado import Empleado
from EmpleadoVendedor import EmpleadoVendedor
from EmpleadoPermanente import EmpleadoPermanente
from EmpleadoContratado import EmpleadoContratado
from SituacionLaboral import SituacionLaboral
from Bonificable import Bonificable


def menu():
    print('''
    ===== MENÚ PRINCIPAL =====
    1. Registrar empleado
    2. Modificar situación laboral
    3. Liquidar remuneración
    4. Aplicar bonificación
    5. Consultar total de sueldos
    6. Consultar cantidad de empleados
    7. Guardar información
    8. Recuperar información
    0. Salir
    ''')


def main():
    empresa = Empresa("EMPRESA ROB")
    datos = None

    while True:
        menu()
        op = int(input("Seleccione una opción: "))

        if op == 1:
            tipo = input("Tipo de empleado (vendedor/permanente/contratado): ").lower()

            nombre = input("Nombre: ")
            documento = int(input("Documento: "))

            if not Empleado.validar_documento(documento):
                print("El documento debe tener entre 7 y 8 dígitos")
                continue

            situacion = SituacionLaboral.ACTIVO

            if tipo == "vendedor":
                sueldo_basico = float(input("Sueldo básico: "))
                ventas = float(input("Ventas mensuales: "))
                empleado = EmpleadoVendedor(nombre, documento, situacion, sueldo_basico, ventas)

            elif tipo == "permanente":
                sueldo_basico = float(input("Sueldo básico: "))
                antiguedad = int(input("Antigüedad en años: "))
                empleado = EmpleadoPermanente(nombre, documento, situacion, sueldo_basico, antiguedad)

            elif tipo == "contratado":
                horas = float(input("Cantidad de horas: "))
                valor_hora = float(input("Valor por hora: "))
                empleado = EmpleadoContratado(nombre, documento, situacion, horas, valor_hora)

            else:
                print("Tipo de empleado inválido")
                continue

            empresa.registrar_empleado(empleado)

        elif op == 2:
            modificar_situacion(empresa)

        elif op == 3:
            liquidar_remuneracion(empresa)

        elif op == 4:
            aplicar_bonificacion(empresa)

        elif op == 5:
            print("Total de sueldos:", empresa.calcular_total_sueldos())

        elif op == 6:
            print("Cantidad de empleados:", empresa.cantidad_empleados)

        elif op == 7:
            datos = empresa.serializar_todo()
            print("Datos guardados correctamente")
            print(datos)

        elif op == 8:
                empresa.deserializar_todo(datos)
                print("Información recuperada correctamente")

        elif op == "0":
            print("Saliendo del programa...ADIOS ")
            break

        else:
            print("Opción inválida")

def liquidar_remuneracion(empresa):
        legajo = int(input("Ingrese el legajo: "))
        empleado = empresa.buscar_empleado(legajo)

        if empleado is None:
            print("Empleado inexistente")
            return

        try:
            sueldo = empleado.liquidar_sueldo()
            print("Remuneración:", sueldo)
        except ValueError as error:
            print(error)

def aplicar_bonificacion(empresa):
        legajo = int(input("Ingrese el legajo: "))
        empleado = empresa.buscar_empleado(legajo)

        if empleado is None:
            print("Empleado inexistente")
            return

        if not isinstance(empleado, Bonificable):
            print("Este empleado no admite bonificaciones")
            return

        importe = float(input("Importe de la bonificación: "))

        print("Remuneración con bonificación:",
          empleado.aplicar_bonificacion(importe))

def modificar_situacion(empresa):
        legajo = int(input("Ingrese el legajo: "))
        empleado = empresa.buscar_empleado(legajo)

        if empleado is None:
            print("Empleado inexistente")
            return

        print("1. Activo")
        print("2. Suspendido")
        print("3. Desvinculado")

        opcion = input("Nueva situación: ")

        if opcion == "1":
            empleado.set_situacion_laboral(SituacionLaboral.ACTIVO)
        elif opcion == "2":
            empleado.set_situacion_laboral(SituacionLaboral.SUSPENDIDO)
        elif opcion == "3":
            empleado.set_situacion_laboral(SituacionLaboral.DESVINCULADO)
        else:
            print("Opción inválida")
            return

        print("Situación laboral modificada correctamente")


if __name__ == "__main__":
    main()

