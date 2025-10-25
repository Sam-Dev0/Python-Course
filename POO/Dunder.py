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

class Manada:
    def __init__(self,perros=None):
        self._perros = list(perros) if perros else []
    
    #__len__ (manada)
    def __len__(self):
        return len(self._perros)
    
    #__iter__ recorre con for
    def __iter__(self):
        return iter(self._perros)
    
    #__getitem__ acceder por indice
    def __getitem__(self,i):
        return self._perros[i]
    
    #__contains__ perro in manada 
    def __contains__(self,perro):
        return any(p.nombre == perro.nombre for p in self._perros)
    
luna, rex = Perro('luna'), Perro('rex')
m = Manada([luna, rex])
print(len(m))
for p in m: print(p.nombre)
print(Perro('luna')in m)
