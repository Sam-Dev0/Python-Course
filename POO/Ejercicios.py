"""
Ejercicio  1.1
Crea una clase Perro con nombre y un metodo presentarse() que imprima "Soy {nombre}". Crea dos perros y llama el metodo, crea otro metodo para ladrar() y llamalo
"""
class Perro:
    especie = 'Mamifero'
    
    def __init__(self,nombre,edad,raza):
        self.nombre = nombre
        self.edad = edad
        self.raza = raza
        
    def presentarse(self):
        print(f'soy {self.nombre}')
        
    def ladrar(self):
        print('guau')
    
rocky = Perro('Rocky',8,'Criollo')
timo = Perro('Timo',6,'Labradudul')
rocky.presentarse()
rocky.ladrar()
timo.presentarse()
timo.ladrar()

"""
Ejercicio 2.1(instancia vs clase)
Define Perro como atributo de clase especie = "Canino" y de instancia nombre. Muestra especie desde dos perros
"""
class Perro:
    especie = 'Canino'
    
    def __init__(self,nombre):
        self.nombre = nombre
        
    @classmethod
    def perro(cls):
        print(f'soy un {Perro.especie}')
    
perro1 = Perro('buba')
perro1.especie

"""
Ejercicio 3.1 (estatico)
@staticmethod es_peso_saludable(peso) devuelve True si 5 <= peso <= 35
"""
class Perro:
    
    def __init__(self,nombre):
        self.nombre = nombre
    
    @staticmethod
    def es_peso_saludable(peso):
        if peso >= 5 and peso <= 35:
            return True
        else:
            return False
    
perro1 = Perro('buba')
print(perro1.es_peso_saludable(15))

"""
Ejercicio 4.1
Crea Gato con dormir(). Crea GatoCompañia(Gato) que sobrescriba dormir()
"""
class gato:
    def __init__(self,nombre,energia):
        self.nombre = nombre
        self.energia = energia
    
    def dormir(self):
        print(f'{self.nombre}: yo duermo mucho!!!')
        
class gatoCompañia(gato):
    
    def ronronear(self):
        print(f'{self.nombre}: ronroneo!!!')

gato1 = gatoCompañia('jesus',20)

gato1.dormir()
gato1.ronronear()

"""
Ejercicio 5.1
Crea clase Animal con hablar() y moverse(). Crea Perro, Vaca y Abeja que hereden Animal y sobrescriban hablar() con ladrar(), muar() y zumbar()
"""
class Animal:
    def __init__(self,especie,edad):
        self.especie = especie
        self.edad = edad
    
    def hablar(self):
        print(f'{self.especie}: yo hablo!!!')
    
    def moverse(self):
        print(f'{self.especie}: yo camino!!!')
    
class Perro(Animal):
    def ladrar(self):
        print(f'{self.especie}: Wooof!!!')

class Vaca(Animal):
    def muar(self):
         print(f'{self.especie}: Muuuu!!!')
         
class Abeja(Animal):
    def zumbar(self):
         print(f'{self.especie}: zzzzzzz!!!')
         

perro = Perro('Canino',4)

perro.hablar()
perro.moverse()
perro.ladrar()

vaca = Vaca('Vaca',10)

vaca.hablar()
vaca.moverse()
vaca.muar()

abeja = Abeja('Insecto',1)
    
abeja.hablar()
abeja.moverse()
abeja.zumbar()


#Ejercicio Herencia y Polimorfismo
class Persona:
    def __init__(self,nombre,apellido):
        self.nombre = nombre
        self.apellido = apellido
  
class Cliente(Persona):#Clase cliente que hereda Persona  
    def __init__(self,nombre,apellido,numerocuenta,balance):
        super().__init__(nombre,apellido)
        self.numerocuenta = numerocuenta
        self.balance = balance
    
    def __str__(self):
        return (f"Cliente: {self.nombre} {self.apellido}\n"
                f"Número de cuenta: {self.numero_cuenta}\n"
                f"Balance actual: ${self.balance:.2f}")

    def depositar(self,monto):
        if monto > 0:
            self.balance += monto
            print(f"Depósito exitoso. Nuevo balance: ${self.balance:.2f}")
        else:
            print("El monto debe ser mayor a cero.")
    
    def retirar(self,monto):
        if monto > self.balance:
            print("Fondos insuficientes. No se puede realizar el retiro.")
        elif monto <= 0:
            print("El monto debe ser mayor a cero.")
        else:
            self.balance -= monto
            print(f"Retiro exitoso. Nuevo balance: ${self.balance:.2f}")


def crear_cliente(self):#funcion crear cliente
    nombre = (input('indique su nombre: '))
    apellido = (input('indique su apellido: '))
    numerocuenta = (int(input('indique su numero de cuenta')))
    while True:
        try:
            balance_inicial = float(input("Ingrese el balance inicial: "))
            break
        except ValueError:
            print("Por favor, ingrese un número válido.")
    return Cliente(nombre, apellido, numerocuenta, balance_inicial)

def inicio(self): # Función principal que organiza el flujo del programa
    cliente = crear_cliente()
    print("Cliente creado exitosamente:")
    print(cliente)

    while True:
        print("¿Qué operación desea realizar?")
        print("1.Depositar")
        print("2.Retirar")
        print("3.Mostrar balance")
        print("4.Salir")
        opcion = input("Seleccione una opción (1-4): ")

        if opcion == "1":
            try:
                monto = float(input("Ingrese el monto a depositar: "))
                cliente.depositar(monto)
            except ValueError:
                print("Monto inválido.")
        elif opcion == "2":
            try:
                monto = float(input("Ingrese el monto a retirar: "))
                cliente.retirar(monto)
            except ValueError:
                print("Monto inválido.")
        elif opcion == "3":
            print(cliente)
        elif opcion == "4":
            print("Gracias por usar el sistema bancario. ¡Hasta pronto!")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__": #Ejecuta el programa
    inicio()
