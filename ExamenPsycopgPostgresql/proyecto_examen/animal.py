from logger_base import log

class Animal:
    def __init__(self,id=None,raza=None,fechaIngreso=None,fechaSalida=None) -> None:
        self._id=id
        self._raza=raza
        self._fechaIngreso=fechaIngreso
        self._fechaSalida=fechaSalida
        
    def __str__(self) -> str:
        return f"""
        ID: {self._id},RAZA: {self._raza},FECHA DE INGRESO: {self._fechaIngreso}, FECHA DE SALIDA: {self._fechaSalida}"""
        
    @property
    def Id(self):
        return self._id
    @Id.setter
    def Id(self,num):
        self._id = num
        
    @property
    def Raza(self):
        return self._raza
    @Raza.setter
    def Raza(self,raza):
        self._nombre = raza
        
    @property
    def FechaIngreso(self):
        return self._fechaIngreso
    @FechaIngreso.setter
    def FechaIngreso(self,fechaIngreso):
        self._fechaIngreso = fechaIngreso
        
    @property
    def FechaSalida(self):
        return self._fechaSalida
    @FechaSalida.setter
    def FechaSalida(self,fechaSalida):
        self._fechaSalida = fechaSalida
        
if __name__ == "__main__":
    ejemplo1 = Vendedor(1,"Ele","Cab",24)
    log.debug(ejemplo1)