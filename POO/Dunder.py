"""
son "ganchos" que python llama automaticamente, para que tus clases se comporten
bien al imprimir,comparar,iterar,sumar,usar,etc.
"""
class Perro:
    #El perro (inicializa)
    def __init__(self,nombre, energia = 60):
        self.nombre = nombre
        self.energia = energia
    #Presentacion amigable (para Print)
    def __str__(self):
        return f'perro{self.nombre!r}, energia={self.energia}'
    
    #presentacion tecnica (para depurar)
    def __repr__(self):
        return f'Perro(nombre ={self.nombre!r}, energia={self.energia})'

luna = Perro("Luna", 70)
print(luna)
