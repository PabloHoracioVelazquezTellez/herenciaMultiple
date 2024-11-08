from classDepartamento import Departamento
class Area(Departamento):
    def __init__(self):
        super().__init__()
        self._nombreArea=""
        self._equipoTrabajo=""

    def getNombreArea(self):
        if self._nombreArea == "":
            return "error"
        else:
            return self._nombreArea

    def setNombreArea(self, nombre):
        self._nombreArea=nombre

    def getEquipoTrabajo(self):
        if self._equipoTrabajo == "":
            return "error"
        else:
            return self._equipoTrabajo

    def setEquipoTrabajo(self, equipoTrabajo):
        self._equipoTrabajo=equipoTrabajo


    def mostrarInformacionArea(self):
        infoDepartamento=Departamento.mostrarInformacionD(self)
        return f"{infoDepartamento}, Area: {self._nombreArea}, EquipoTrabajo: {self._equipoTrabajo}"
