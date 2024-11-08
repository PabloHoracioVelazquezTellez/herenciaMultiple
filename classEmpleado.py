from classPersona import Persona

class Empleado(Persona):
    def __init__(self):
        super().__init__()
        self._cargo = ""
        self._sueldo = 0
        self._nomina = ""
        self._estatusSeguro= 0


    # Getter y Setter
    def getCargo(self):
        if self._cargo == "":
            return "error"
        else:
            return self._cargo

    def setCargo(self, cargo):
        self._cargo = cargo

    def getSueldo(self):
        if self._sueldo == 0:
            return "error"
        else:
            return self._sueldo

    def setSueldo(self, sueldo):
        self._sueldo= sueldo

    def getNomina(self):
        if self._nomina == "":
            return "error"
        else:
            return self._nomina

    def setNomina(self, nomina):
        self._nomina = nomina

    def getEstatusSeguro(self):
        if self._estatusSeguro == 0:
            return "error"
        else:
            return self._estatusSeguro

    def setEstatusSeguro(self, estatusSeguro):
        self._estatusSeguro = estatusSeguro
        if self._estatusSeguro not in range (1,7):
            self._estatusSeguro= "error"
        if self._estatusSeguro == 1:
            self._estatusSeguro= "Incapacidad medica"
        elif self._estatusSeguro == 2:
            self._estatusSeguro= "Incapacidad por maternidad"
        elif self._estatusSeguro == 3:
            self._estatusSeguro= "Incapacidad por riesgo de trabajo"
        elif self._estatusSeguro == 4:
            self._estatusSeguro= "Vacaciones"
        elif self._estatusSeguro == 5:
            self._estatusSeguro= "Falta con goce de sueldo"
        elif self._estatusSeguro == 6:
            self._estatusSeguro= "Falta sin goce de sueldo"
        elif self._estatusSeguro == 7:
            self._estatusSeguro= "Activo en planta"


    def mostrarInformacionEmpleado(self):
        parentInfo = super().mostrarInformacionPersona()
        return f"{parentInfo} \nEstatus: {self._estatusSeguro}, Cargo: {self._cargo}, sueldo: {self._sueldo}, Nomina: {self._nomina}"
