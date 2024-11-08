from classEmpleado import Empleado
from classArea import Area

class Directores(Area, Empleado):
    def __init__(self):
        Area.__init__(self)
        Empleado.__init__(self)
        self._region = ""

    # Getter y Setter
    def getRegion(self):
        if self._region == "":
            return "error"
        else:
            return self._region

    def setRegion(self, region):
        self._region = region


    #IMPRIMIR INFORMACION

    def mostrarInfoCompleta(self):
        infoDepartamento=Area.mostrarInformacionArea(self)
        infoEmpleado=Empleado.mostrarInformacionEmpleado(self)
        return f"{infoDepartamento}\n {infoEmpleado} \nRegion: {self._region}"

    def mostrarInformacionRegion(self):
        return f"La region del director es {self._region}"

    def mostrarSueldo(self):
        sueldoEmpleado= Empleado.getSueldo(self)
        return f"El sueldo del director es {sueldoEmpleado}"
