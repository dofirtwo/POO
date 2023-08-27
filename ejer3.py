class Curso():
    def __init__(self, nombre):
        self.__nombre=nombre
        self.__alumnos=[]
    
    def getNombre(self):
        return self.__nombre
    
    def getAlumnos(self):
        return self.__alumnos
    
    def matricularAlumno(self,alumno):
        self.__alumnos.append(alumno)
        
    def __str__(self):
        return self.__nombre
    
    def __del__(self):
        print("Eliminado")
class Alumno():
    def __init__(self,nombre,edad):
        self.__nombre=nombre
        self.__edad=edad
        
    def getNombre(self):
        return self.__nombre
    
    def setNombre(self,nombre):
        self.__nombre==nombre
    
    def getEdad(self):
        return self.__edad
    
    def setEdad(self,edad):
        self.__edad=edad
    
    def __str__(self):
        return self.__nombre
        
unCurso= Curso("Python AVANZADO")
alumno1= Alumno("Maria",23)
alumno2= Alumno("Juan",32)
alumno3= Alumno("Rosa",18)  

unCurso.matricularAlumno(alumno1)
unCurso.matricularAlumno(alumno3)

for a in unCurso.getAlumnos():
    print(a)
    
unCurso.__del__()
print(unCurso.getNombre())    