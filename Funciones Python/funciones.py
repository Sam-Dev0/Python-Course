#funcion 1
def f1():
    print("Hola")
f1();

#funcion 2
def f2(nombre, apellido):
    print(nombre + " " +apellido)
f2("juan", "Perez");

#funcion 3(Recibe una cantidad especifica)
def f3(fname):
    print(fname +" Refsnes ")
f3("Emil");
f3("Tobias");
f3("Linus");

#funcion 4 (* recibe cualquier cantidad)-(Tupla)
def f4(*kids):
    print("The youngest child is " +kids[2])
f4("Email", "Tobias", "Linus");

#funcion 5
def f5(child3, child2, child1):
    print("The oldest child is " +child1)
f5(child1 = "Emil", child2 = "Tobias", child3 = "Linus");

#funcion 6
def f6(**kid):
    print("His name is " +kid["nombre"])
f6(nombre = "Tobias", apellido = "Lopez")

#funcion 7
def f7(country = "Norway"):
    print("Yo nací en " + country)
country = input("Digite su pais: ")
f7(country);
