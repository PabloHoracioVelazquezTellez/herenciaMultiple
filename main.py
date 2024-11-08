from classDirector import Directores
from classGerente import Gerentes
from classJefeArea import Jefes

def main():
    director = Directores()
    director.setNombre("Mario")
    director.setApellido("N")
    director.setVida(True)
    director.setNombreDepartamento("Altos ejecutivos")
    director.setSeccionTrabajo("Seccion 8")
    director.setNombreArea("Contabilidad")
    director.setEquipoTrabajo("Tomas, Juan, Luis")
    director.setEstatusSeguro(7)
    director.setCargo("Director")
    director.setEdad(40)
    director.setSueldo(234567890)
    director.setNomina("K12345678")
    director.setRegion("Centro Norte")

    print(director.mostrarInfoCompleta())

    gerente = Gerentes()
    gerente.setNombre("Ana")
    gerente.setApellido("Ramirez")
    gerente.setVida(True)
    gerente.setNombreDepartamento("Mercadeo")
    gerente.setSeccionTrabajo("Seccion 4")
    gerente.setNombreArea("Marketing")
    gerente.setEquipoTrabajo("Individual")
    gerente.setEstatusSeguro(1)
    gerente.setCargo("Gerente de Mercadeo")
    gerente.setEdad(32)
    gerente.setSueldo(23456)
    gerente.setNomina("K1234567")
    gerente.setZona("Pachuca")

    print("\n",gerente.mostrarInfoCompleta())

    jefe = Jefes()
    jefe.setNombre("Javier")
    jefe.setApellido("Ramirez")
    jefe.setVida(True)
    jefe.setNombreDepartamento("Ventas")
    jefe.setSeccionTrabajo("Seccion 9")
    jefe.setNombreArea("Abarrote")
    jefe.setEquipoTrabajo("Cubre Contingencias No Asignado")
    jefe.setEstatusSeguro(6)
    jefe.setCargo("Jefe de Ventas")
    jefe.setEdad(25)
    jefe.setSueldo(567856)
    jefe.setNomina("K1834658")
    jefe.setArea("Abarrote")
    jefe.setHistoricoResultados("Baja merma, Alto farderismo")

    print("\n",jefe.mostrarInformacionJefe())


main()