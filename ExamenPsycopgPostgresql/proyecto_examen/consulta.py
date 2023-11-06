from logger_base import log

class Consulta:
    def __init__(self,idAnimal=None,idDoctor=None,servicio=None,costo=None) -> None:
        self._idAnimal=idAnimal
        self._idDoctor=idDoctor
        self._servicio=servicio
        self._costo=costo
        
    def __str__(self) -> str:
        return f"""
        ID ANIMAL: {self._idAnimal},ID DOCTOR: {self._idDoctor},SERVICIO: {self._servicio},COSTO: {self._costo}"""
        
    @property
    def IdAnimal(self):
        return self._idAnimal
    @IdAnimal.setter
    def IdAnimal(self,num):
        self._idAnimal = num
        
    @property
    def IdDoctor(self):
        return self._idDoctor
    @IdDoctor.setter
    def IdDoctor(self,num):
        self._idDoctor = num
        
    @property
    def Servicio(self):
        return self._servicio
    @Servicio.setter
    def Servicio(self,servicio):
        self._servicio = servicio

    @property
    def Costo(self):
        return self._costo
    @Costo.setter
    def Costo(self,costo):
        self._costo = costo
    
#if __name__ == "__main__":
#    ejemplo1 = Vendedor(1,"Ele","Cab",24)
#    log.debug(ejemplo1)