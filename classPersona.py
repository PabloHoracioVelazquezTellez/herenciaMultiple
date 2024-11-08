class Persona:
    def __init__(self):
        self._nombre = ""
        self._apellido = ""
        self._edad = 0
        self._vida= None

    # Getters y Setters
    def getNombre(self):
        if self._nombre == "":
            return "error"
        else:
            return self._nombre

    def setNombre(self, nombre):
        self._nombre = nombre

    def getApellido(self):
        if self._apellido == "":
             return "error"
        else:
             return self._apellido

    def setApellido(self, apellido):
        self._apellido = apellido

    def getEdad(self):
        if self._edad == "":
            return "error"
        else:
            return self._edad

    def setEdad(self, edad):
        self._edad = edad

    def getVida(self):
        if self._vida == None:
            return "error"
        elif self._vida == False:
            return "NO"
        else:
            return "SI"
    def setVida(self, vida):
        self._vida = vida

    def mostrarInformacionPersona(self):
        return f"Nombre: {self._nombre} {self._apellido}, Edad: {self._edad}, Vive? {self._vida}"
