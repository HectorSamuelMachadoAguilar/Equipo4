from animal import Animal
from Conexion import Conexion
from Cursor import CursorDelPool
from logger_base import log
from datetime import date

class AnimalDAO:
    
    _SELECCIONAR = "SELECT * FROM animal ORDER by raza"
    _INSERT = "INSERT INTO animal (id,raza,fecha_de_ingreso,fecha_de_salida) VALUES (%s,%s,%s,%s)"
    _ACTUALIZAR= "UPDATE animal SET raza = %s, fecha_de_ingreso = %s, fecha_de_salida = %s WHERE id = %s"
    _ELIMINAR = "DELETE FROM animal WHERE id = %s"
    _SELECCIONAR2 = "SELECT * FROM animal WHERE fecha_de_ingreso = %s"
    
    @classmethod
    def seleccionar(cls):
        with CursorDelPool() as cursor:
            cursor.execute(cls._SELECCIONAR)
            registros = cursor.fetchall()
            animales=[]
        for r in registros:
            animales.append(Animal(r[0],r[1],r[2],r[3]))
        return animales
    
    @classmethod
    def seleccionar2(cls,fechaIngreso):
        with CursorDelPool() as cursor:
            cursor.execute(cls._SELECCIONAR2,fechaIngreso)
            registros = cursor.fetchall()
            animales=[]
        for r in registros:
            animales.append(Animal(r[0],r[1],r[2],r[3]))
        return animales
        
    @classmethod
    def insertar(cls,animal):
        with CursorDelPool() as cursor:
            valores = (animal.Id,animal.Raza,animal.FechaIngreso,animal.FechaSalida)
            cursor.execute(cls._INSERT,valores)
            return cursor.rowcount
        
    @classmethod
    def actualizar(cls,animal):
        with CursorDelPool() as cursor:
            valores = (animal.Raza,animal.FechaIngreso,animal.FechaSalida,animal.Id)
            cursor.execute(cls._ACTUALIZAR,valores)
            return cursor.rowcount
        
    @classmethod
    def eliminar(cls,animal):
        with CursorDelPool() as cursor:
            valores = (animal.Id,)
            cursor.execute(cls._ELIMINAR,valores)
            return cursor.rowcount
        
if __name__ == "__main__":
    
    
    miAnimal = Animal(raza="Perro",fechaIngreso=date(2023,11,6),fechaSalida=date(2023,11,7))
    miAnimal.Id = 1
    insert = AnimalDAO.insertar(miAnimal)
    log.debug(insert)
    
    #miVendedor = Vendedor(nombre="Leonel",apellido="Reyes",edad=39)
    #miVendedor.Id = 3
    #update = VendedorDAO.actualizar(miVendedor)
    #log.debug(f"Fila ACTUALIZADA = {update}")
    
    #miAnimal = Animal(id=2)
    #delete = AnimalDAO.eliminar(miAnimal)
    #log.debug(f"Fila ELIMINADA = {delete}")
    
    consulta = AnimalDAO.seleccionar()
    for r in consulta:
        log.debug(r)
    