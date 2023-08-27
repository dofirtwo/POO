class Perro():
    def __init__(self,nombre,raza):
        self.nombre=nombre
        self.raza=raza
        
    def ladrar(self):
        print("guao")
        
    def caminar(self,pasos):
        print(f"{self.nombre} ha realizado {pasos} pasos")
        
miPerro = Perro("Tango","Beagle")
print(miPerro.nombre)
miPerro.ladrar()
miPerro.caminar(5)
miPerro.nombre="apolo"

    