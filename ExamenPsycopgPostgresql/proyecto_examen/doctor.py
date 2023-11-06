from logger_base import log

class Doctor:
    def __init__(self,id=None,nombre=None,numeroTelefono=None) -> None:
        self._id=id
        self._nombre=nombre
        self._numeroTelefono=numeroTelefono
        
    def __str__(self) -> str:
        return f"""
        ID: {self._id},NOMBRE: {self._nombre},NUMERO DE TELEFONO: {self._numeroTelefono}"""
        
    @property
    def Id(self):
        return self._id
    @Id.setter
    def Id(self,num):
        self._id = num
        
    @property
    def Nombre(self):
        return self._nombre
    @Nombre.setter
    def Nombre(self,nombre):
        self._nombre = nombre
        
    @property
    def NumeroTelefono(self):
        return self._numeroTelefono
    @NumeroTelefono.setter
    def NumeroTelefono(self,numeroTelefono):
        self._numeroTelefono = numeroTelefono

#if __name__ == "__main__":
#    ejemplo1 = Vendedor(1,"Ele","Cab",24)
#    log.debug(ejemplo1)