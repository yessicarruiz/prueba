from typing import Self


class Paciente:
    def __init__(self):
      self.__nombre = ""
      self.__cedula = 0
      self.__genero = ""
      self.__servicio = ""
      
    def verNombre(self):
        return self.__nombre
    def verServicio(self):
        return self.__servicio
    def verGenero(self):
        return self.__genero
    def verCedula(self):
        return self.__cedula
    
    def asignarNombre(self,n):
        self.__nombre = n
    def asignarServicio(self,s):
        self.__servicio = s
    def asignarGenero(self,g):
        self.__genero = g
    def asignarCedula(self,c):
        self.__cedula = c

class Sistema:
    def __init__(self):
      self.__lista_pacientes = []
    #   self.__lista_pacientes = {}
      self.__numero_pacientes = len(self.__lista_pacientes)
def main():

    while True:
        opcion = int(input("1. Nuevo paciente\n - 2. Numero de paciente\n - 3. Datos paciente\n - 4. ver datos del paciente 5.:  \n"))
        if opcion == 1:
            print ("datos del paciente: ")
            nombre= input ("ingrese el nombre: ")
            cedula= input ("ingrese la cedula del paciente ")
            genero= input ("ingrese M para masculino y F para femenino")
            servicio= input ("ingrese el servicio: ")

        if opcion == 2:
            p= Paciente()
            p.asignarNombre(nombre)
            p.asignarCedula(cedula)
            p.asignarGenero(genero)
            p.asignarServicio(servicio)
            Self.__lista_pacientes.append(p)
            print("Ahora hay: " + str(mi_sistema.verNumeroPacientes()))

        if opcion== 3:
            cedula = int(input("Ingrese la cedula a buscar: "))
        
        for paciente in self.__lista_pacientes:
            if cedula == paciente.verCedula():
                print("Nombre: " + paciente.verNombre())
                print("Cedula: " + str(paciente.verCedula()))
                print("Genero: " + paciente.verGenero())
                print("Servicio: " + paciente.verServicio())
                verDatosPaciente()
        
        if opcion == 4:
            break
        else:
            print("Opcion invalida")    

if __name__== "__main__":
    main()
