from consulta import Consulta
from Conexion import Conexion
from Cursor import CursorDelPool
from logger_base import log

class ConsultaDAO:
    
    _SELECCIONAR = "SELECT * FROM consulta ORDER by costo"
    _SELECCIONAR2 = "SELECT * FROM consulta WHERE id_animal = %s"
    _INSERT = "INSERT INTO consulta (id_animal,id_doctor,servicio,costo) VALUES (%s,%s,%s,%s)"
    _ACTUALIZAR= "UPDATE consulta SET servicio = %s, costo = %s WHERE id_animal = %s"
    _ELIMINAR = "DELETE FROM consulta WHERE id_animal = %s"
    
    @classmethod
    def seleccionar(cls):
        with CursorDelPool() as cursor:
            cursor.execute(cls._SELECCIONAR)
            registros = cursor.fetchall()
            consultas=[]
        for r in registros:
            consultas.append(Consulta(r[0],r[1],r[2],r[3]))
        return consultas
        
    @classmethod
    def insertar(cls,consulta):
        with CursorDelPool() as cursor:
            valores = (consulta.IdAnimal,consulta.IdDoctor,consulta.Servicio,consulta.Costo)
            cursor.execute(cls._INSERT,valores)
            return cursor.rowcount
        
    @classmethod
    def actualizar(cls,consulta):
        with CursorDelPool() as cursor:
            valores = (consulta.Servicio,consulta.Costo,consulta.IdAnimal)
            cursor.execute(cls._ACTUALIZAR,valores)
            return cursor.rowcount
        
    @classmethod
    def eliminar(cls,consulta):
        with CursorDelPool() as cursor:
            valores = (consulta.IdAnimal,)
            cursor.execute(cls._ELIMINAR,valores)
            return cursor.rowcount
    
    @classmethod
    def seleccionar2(cls,consulta):
        with CursorDelPool() as cursor:
            valores = (consulta.IdAnimal,)
            cursor.execute(cls._SELECCIONAR2,valores)
            registros = cursor.fetchall()
            consultas=[]
        for r in registros:
            consultas.append(Consulta(r[0],r[1],r[2],r[3]))
        return consultas
        
if __name__ == "__main__":
    
    
    #miVendedor = Vendedor(nombre="Leonel",apellido="Reyes",edad=28)
    #miVendedor.Id = 2
    #insert = VendedorDAO.insertar(miVendedor)
    #log.debug(insert)
    
    #miVendedor = Vendedor(nombre="Leonel",apellido="Reyes",edad=39)
    #miVendedor.Id = 3
    #update = VendedorDAO.actualizar(miVendedor)
    #log.debug(f"Fila ACTUALIZADA = {update}")
    
    #miVendedor = Vendedor(id=2)
    #delete = VendedorDAO.eliminar(miVendedor)
    #log.debug(f"Fila ELIMINADA = {delete}")
    
    miOb = Consulta(idAnimal=1,idDoctor=1)
    consulta = ConsultaDAO.seleccionar2(miOb)
    for r in consulta:
        log.debug(r)
    