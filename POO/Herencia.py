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

"""
Herencia multiple: una clase hereda de varios padres: abuelo -> padre -> hijo...
MRO(orden de metodo de resolucion): Si A no tiene el método, python lo busca en B; si no está, va a C, 
y así sigue por la cadena de ancestros ya calculada en el __mro__.
Super():nos permite acceder a los métodos de la clase padre desde una de sus hijas.
"""
#Clase herencia multiple
class PerrodeShow(Perro):
    def presentarse(self):
        print('Soy un perro que hace trucos')

class RastreadorMixin():#Mixin bloque reutilizable
    def rastrer(self):
        print('Estoy rastreando')

class PerroRastreadordeShow(PerrodeShow, RastreadorMixin): #Hereda de los que estan por encima de ella
    pass
tony = PerroRastreadordeShow('Tony', 10000)
tony
tony.presentarse()
tony.rastrer()

#Clase usando super()
class Perro(Animal):
    def __init__(self,especie,edad,dueño)
        #Alternativa 1
        self.especie = especie
        self.edad = edad
        self.dueño = dueño
        #Alternativa 2
        super().__init__(especie,edad)
        self.dueño = dueño
mi_perro = Perro('Mamifero', 7, 'Luis')
mi_Perro.especie
mi_Perro.edad
mi_Perro.dueño
