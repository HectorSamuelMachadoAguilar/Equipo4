from doctor import Doctor
from Conexion import Conexion
from Cursor import CursorDelPool
from logger_base import log

class DoctorDAO:
    
    _SELECCIONAR = "SELECT * FROM doctor ORDER by nombre"
    _INSERT = "INSERT INTO doctor (id,nombre,numero_de_telefono) VALUES (%s,%s,%s)"
    _ACTUALIZAR= "UPDATE doctor SET nombre = %s, numero_de_telefono = %s WHERE id = %s"
    _ELIMINAR = "DELETE FROM doctor WHERE id = %s"
    
    @classmethod
    def seleccionar(cls):
        with CursorDelPool() as cursor:
            cursor.execute(cls._SELECCIONAR)
            registros = cursor.fetchall()
            doctores=[]
        for r in registros:
            doctores.append(Doctor(r[0],r[1],r[2]))
        return doctores
        
    @classmethod
    def insertar(cls,doctor):
        with CursorDelPool() as cursor:
            valores = (doctor.Id,doctor.Nombre,doctor.NumeroTelefono)
            cursor.execute(cls._INSERT,valores)
            return cursor.rowcount
        
    @classmethod
    def actualizar(cls,doctor):
        with CursorDelPool() as cursor:
            valores = (doctor.Nombre,doctor.NumeroTelefono,doctor.Id)
            cursor.execute(cls._ACTUALIZAR,valores)
            return cursor.rowcount
        
    @classmethod
    def eliminar(cls,doctor):
        with CursorDelPool() as cursor:
            valores = (doctor.Id,)
            cursor.execute(cls._ELIMINAR,valores)
            return cursor.rowcount
        
if __name__ == "__main__":
    
    
    miDoctor = Doctor(nombre="Cabello",numeroTelefono=867123123)
    miDoctor.Id = 2
    insert = DoctorDAO.insertar(miDoctor)
    log.debug(insert)
    
    #miVendedor = Vendedor(nombre="Leonel",apellido="Reyes",edad=39)
    #miVendedor.Id = 3
    #update = VendedorDAO.actualizar(miVendedor)
    #log.debug(f"Fila ACTUALIZADA = {update}")
    
    #miVendedor = Vendedor(id=2)
    #delete = VendedorDAO.eliminar(miVendedor)
    #log.debug(f"Fila ELIMINADA = {delete}")
    
    consulta = DoctorDAO.seleccionar()
    for r in consulta:
        log.debug(r)
    