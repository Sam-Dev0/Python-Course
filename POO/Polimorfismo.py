"""
Polimorfismo:
Misma orden, comportamientos distintos según quién la recibe.
Si digo: trabajar(), un PerroPolicia patrulla, un PerroGuia acompaña, y un PerroRescatista busca personas. La “palabra mágica” es la misma, la acción cambia.
Te permite escribir menos if/elif y código más limpio.Facilita agregar nuevas clases sin tocar lo ya escrito.
"""
class Perro:
    def __init__(self,nombre):
        self.nombre = nombre
    
    def trabajar(self):
        print(f'hago cosas de perros normales')

class PerroPolicia(Perro):
    def trabajar(self):
        print(f'hago cosas de perro policia como patrullar')

class PerroGuia(Perro):
    def trabajar(self):
        print(f'soy {self.nombre} y acompaño a las personas')

class PerroRescatista(Perro):
    def trabajar(self):
        print(f'rescato personas')

def turno(perro: Perro):
    #no pregunta "¿que tipo eres?" ->Polimorfismo
    perro.trabajar()

manada = [Perro('Edgardo'),PerroPolicia('Rex'),PerroGuia('Bruno'),PerroRescatista('Nina')]

for p in manada:
    turno(p)
