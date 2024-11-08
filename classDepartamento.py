class Departamento:
    def __init__(self):
        self._nombreDepartamento =""
        self._seccionTrabajo= ""

    def getNombreDepartamento(self):
        if self._nombreDepartamento == "":
            return "error"
        else:
            return self._nombreDepartamento

    def setNombreDepartamento(self, nombreDepartamento):
        self._nombreDepartamento = nombreDepartamento

    def getSeccionTrabajo(self):
        if self._seccionTrabajo == "":
            return "error"
        else:
            return self._seccionTrabajo

    def setSeccionTrabajo(self, seccionTrabajo):
        self._seccionTrabajo = seccionTrabajo

    def mostrarInformacionD(self):
        return f"Departamento: {self._nombreDepartamento}, Seccion de trabajo: {self._seccionTrabajo}"