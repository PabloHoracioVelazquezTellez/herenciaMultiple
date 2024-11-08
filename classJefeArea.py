from classArea import Area
from classEmpleado import Empleado
class Jefes(Area,Empleado):
    def __init__(self):
        Area.__init__(self)
        Empleado.__init__(self)
        self._area =""
        self._historicoResultados =""

    def getArea(self):
        if self._area == "":
            return "error"
        else:
            return self._area

    def setArea(self,area):
        self._area = area

    def getHistoricoResultados(self):
        if self._historicoResultados == "":
            return "error"
        else:
            return self._historicoResultados

    def setHistoricoResultados(self,historicoResultados):
        self._historicoResultados = historicoResultados


    def mostrarInformacionJefe(self):
        infoArea= Area.mostrarInformacionArea(self)
        infoEmpleado= Empleado.mostrarInformacionEmpleado(self)
        return f"{infoArea}\n{infoEmpleado}\n, Area Asignada: {self._area}, Historico de resultados: {self._historicoResultados}"
