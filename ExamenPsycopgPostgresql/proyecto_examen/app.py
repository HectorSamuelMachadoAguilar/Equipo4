from consultaDAO import ConsultaDAO
from consulta import Consulta
from doctorDAO import DoctorDAO
from doctor import Doctor
from animalDAO import AnimalDAO
from animal import Animal
from logger_base import log
from datetime import datetime,timedelta



#Ingreso a consulta
def IngresarConsulta(idAnimal,idDoctor,servicio,costo):
    DoctorId = 1

    contadorCitas = 0
    consulta = ConsultaDAO.seleccionar()
    for r in consulta:
        if r.IdDoctor == DoctorId:
            contadorCitas += 1
        log.debug(r)

    if contadorCitas > 2:
        log.warning(f"El doctor ya cuenta ocn el maximo de citas por hoy.")
    else:
        miConsulta = Consulta(idAnimal=idAnimal,idDoctor=idDoctor,servicio=servicio,costo=costo)
        insert = ConsultaDAO.insertar(miConsulta)
        log.debug(f"Se ingreso una consulta al Doctor con ID: {insert}")


#Dar de alta una consulta
def DarAltaConsulta(id,fechaSalida):
    
    miAnimal = Animal(id=id,fechaSalida=fechaSalida)
    update = AnimalDAO.actualizar(miAnimal)
    log.debug(update)
    
    
def ConsultasDiaAteriorHoy():
    
    fecha_actual = datetime.now()
    fecha_actual_str = fecha_actual.strftime("%Y-%m-%d %H:%M:%S")
    seleccionar = AnimalDAO.seleccionar2(fecha_actual_str)
    for r in seleccionar:
        log.debug(r)
    



#IngresarConsulta(idAnimal=1,idDoctor=1,servicio="vacunas",costo=200.0)
#consulta = ConsultaDAO.seleccionar()

ConsultasDiaAteriorHoy()

