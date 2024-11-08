from classEmpleado import Empleado
from classArea import Area

class Gerentes(Area, Empleado):
    def __init__(self):
        Empleado.__init__(self)
        Area.__init__(self)
        self._zona = ""

    def getZona(self):
        if self._zona == "":
            return "error"
        else:
            return self._zona

    def setZona(self, zona):
        self._zona = zona

    def mostrarInfoCompleta(self):
        infoArea=Area.mostrarInformacionArea(self)
        infoEmpleado=Empleado.mostrarInformacionEmpleado(self)
        return f"{infoArea}\n{infoEmpleado}\nZona: {self._zona}"
