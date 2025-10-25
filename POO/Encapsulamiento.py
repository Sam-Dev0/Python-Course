"""
Encapsulamiento: metodo para proteger datos y metodos se usa con un guion bajo solo para proteger _protegido(solo lectura), 
y con dos guiones bajos para un metodo privado __privado(no se puede acceder a el ni cambiarlo)
"""

class Perro:
    especie = 'Canino'

    def __init__(self,nombre,peso):
        self.nombre = nombre # Publico
        self._peso = peso # Protegido
        self._energia = 60 # Protegido
        self.__chip_id = "x9k-77" # Privado
    
    # --- Lectura controlada (get) --- #
    @property
    def energia(self):
        return self._energia # Energia solo lectura

    # --- Escritura controlada (set) --- #
    @property
    def peso(self):
        return self._peso

    @peso.setter # permite hacer cambios en la variable peso
    def peso(self,valor):
        if valor  <= 0:
            raise ValueError("El peso debe ser positivo")
        self._peso = valor
    
    # --- Acciones seguras que modifican estado --- #
    def jugar(self,minutos: int):
        if minutos <= 0:
            raise ValueError("los minutos deben ser positivos")
        #Regla simple: 1min = -3 energia
        self._energia = max(0, self._energia - minutos * 3)
        print(f'{self.nombre} jugo {minutos} min. Energia: {self._energia}')
    
    def comer(self,gramos: int):
        if gramos <= 0:
            raise ValueError('comida no valida, debe ser positiva')
        # Regla simple: cada 10g = +1 de energia
        self._energia = min(100, self._energia + gramos // 10)
        print(f'{self.nombre} comio {gramos}g. Energia: {self._energia}')

    # --- Acceso indirecto a lo "Privado" si hace falta ---#
    def identificar(self):
        #Lo usamos desde adentro; fuera no es facil
        return f"chip {self.__chip_id}"
