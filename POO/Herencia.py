"""
Herencia: es cuando una clase (Padre) le hereda las caracteristicas y habilidades a una clase (Hija),
la (Hija) puede agregar y cambiar cosas
"""
#Clase herencia
class Padre:
    def __init__(self,nombre,energia):
        self.nombre = nombre
        self.energia = energia
    
    def ladrar(self):
        print(f'{self.nombre}: Woof!!!')
    
    def trabajar(self):
        print(f'{self.nombre}: hago cosas de perro!!!')
        
class perroPolicia(Padre):# hereda lo que esta en la clase Padre
    def olfatear(self):
        print(f'{self.nombre}: estoy olfateando!!!!')


class perroGuia(perroPolicia):# hereda lo que esta en la clase "perroPolicia" y en la clase "Padre"
    def ayudar(self):
        print(f'{self.nombre}: ayudo a las personas!!!')


k9 = perroPolicia('Chucho',100)

k9.ladrar()
k9.trabajar()
k9.olfatear()

k10 = perroGuia('Gustavo',100)

k10.ladrar()
k10.trabajar()
k10.ayudar()
