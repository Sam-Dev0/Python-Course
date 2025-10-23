
# Encapsulamiento: hacer que los metodos o atributos no sean accesibles desde afuera

class Mi_clase:
    atributo_clase = 'Hola' # accesible desde afuera
    __atributo_clase = 'Hola' #al momento de imprimir da error como si fuera una variable externa
    
    def __metodo1(self):
        print('algo')

# los que tenga __ solo son accesibles dentro de la clase no desde afuera