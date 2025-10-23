class Perro:
    especie = 'Mamifero'
    _conteo = 0
    
    def __init__(self,nombre,edad,raza):
        self.nombre = nombre
        self.edad = edad
        self.raza = raza
        print(f'se esta creando el perro {nombre} con {edad} años y de raza {raza}')
        Perro._conteo += 1
        
    #Metodos de instancia
    def ladrar(self):
        print('guau')
    
    def caminar(self,pasos):
        print(f'caminando {pasos} pasos')
        
    #Metodos de clase
    @classmethod
    def cuantos_hay(cls):
        return cls._conteo
    
    #Metodos estaticos
    @staticmethod
    def calorias_por_minuto(peso_kg: float):
        if peso_kg <= 0:
            print('peso no valido')
        if peso_kg < 10:
            return 4
        else:
            return 7
toby = Perro('Toby',0.4,'chow chow')
print(Toby.calorias_por_minuto(2))