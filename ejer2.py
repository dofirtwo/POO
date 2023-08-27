class Persona():
    def __init__(self,identificacion,nombre,correo):
        """_summary_
            constructor con pparametros de inicializacion

        Args:
            identificacion (str): # documento de identidad
            nombre (str): nombre completo de la persona
            correo (str): correo completo de la persona
        """
        self.__identificacion=identificacion
        self.__nombre=nombre
        self.__correo=correo
        
    def getIdentificacion(self):
        return self.__identificacion
    def getNombre(self):
        return self.__nombre
    def getCorreo(self):
        return self.__correo
    
    def setIdentificacion(self,identificacion):
        self.__identificacion=identificacion
    def setNombre(self,nombre):
        self.__nombre=nombre
    def setCorreo(self,correo):
        self.__correo=correo

class Aprendiz(Persona):
    
    def __init__(self, identificacion, nombre, correo,puntajeIcfes):
        super().__init__(identificacion, nombre, correo)
        self.__puntajeIcfes=puntajeIcfes
        
    def getPuntajeIcfes(self):
        return self.__puntajeIcfes
    
    def setPuntajeIcfes(self,puntajeIcfes):
        self.__puntajeIcfes=puntajeIcfes
        
class Instructor(Persona):
    
    def __init__(self, identificacion, nombre, correo,especialidad):
        super().__init__(identificacion, nombre, correo)
        self.__especialidad=especialidad
        
    def getEspecialidad(self):
        return self.__especialidad
    
    def setEspecialidad(self,especialidad):
        self.__especialidad=especialidad