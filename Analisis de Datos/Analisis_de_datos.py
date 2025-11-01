import numpy as np #(pip install numpy) libreria
import pandas as pd #(pip install pandas) libreria

"""LIBRERIA NUMPY"""
arreglo = np.array([1,2,3,4,5])
arreglo

arreglo[2]

arreglo_booleano = np.array([True,False,True,True])
arreglo_booleano

matriz = np.array([[1,2,3],[4,5,6]]) #arreglo(s) de arreglo
matriz

#Opreaciones
arreglo1 = np.array([1,2,3,4,5])
arreglo2 = np.array([6,7,8,9,0])
np.add(arreglo1,arreglo2) #suma
np.subtract(arreglo1,arreglo2) #resta
np.multiply(arreglo1,arreglo2) #multiplicacione
np.divide(arreglo1,arreglo2) #divicion
np.power(arreglo1,arreglo2) #potencia
#hay muchas mas


#funciones de comparacion
np.greater(arreglo1,arreglo2) #si es mayor que
np.greater_equal(arreglo1,arreglo2) #si es mayor o igual que
np.less(arreglo1,arreglo2) #si es menor que
np.less_equal(arreglo1,arreglo2) #si es menor o igual que

 #Funciones estadisticas
arreglo1 = np.array([1,2,3,4,5,6,7,8,9,0])
arreglo2 = np.array([6,7,8,9,0])


print(f'el valor minimo del arreglo es: { np.amin(arreglo1)}') #devuelve el valor minimo
print(f'el valor maximo del arreglo es: { np.amax(arreglo1)}') #devuelve el valor maximo
print(f'percentil 25: { np.percentile(arreglo1,25)}') #devuelve el percentil 25
print(f'la mediana del arreglo es: { np.median(arreglo1)}') #devuelve la mediana(el dato de la mitad)
print(f'la media del arreglo es: { np.mean(arreglo1)}') #devuelve la media (suma de la cantidad de datos)
print(f'la desviacion estandar del arreglo es: { np.std(arreglo1)}') #medida de dispersion de los datos


#----------------------------------------------------------------o---------------------------------------------------#


"""LIBRERIA PANDAS"""
Datos = pd.DataFrame(
    
    {
        "Nombre":['Andrea','Felipe','Susana'],
        "Edad":[16,34,67],
        "Pais":['Colombia','Chile','Peru'],
        "Sueldo":[10000000,2000000,3000000]
    }
)

serie = pd.Series([1,2,3,4,5], index=['a','b','c','d','e']) #el index cambia los indices ya definidos por lo que uno quiera que se identifique cada valor
serie
serie2 = pd.Series({'a':1, 'b':2, 'c':3, 'd':4, 'e':5})
serie2

resultado = serie + serie2
resultado

edad = Datos['Edad']
print(f'la edad maxima del df es: {edad.max()}')
print(f'la edad minima del df es: {edad.min()}')

#Ordenar DataFrames
Datos.sort_values(by='Edad',ascending=False)

#Describe datos que se puedan operar
Datos.describe()

#Lee el archivo .csv
titanic = pd.read_csv("titanic.csv")

#Lee las primeras 5 filas
titanic.head()

#Lee las ultimas 5 filas
titanic.tail()

#Evalua el tipo de dato de cada columna
titanic.dtypes

#Trae las filas que uno le determine
titanic.iloc[2:10]


#Devueleve el numero de filas y de columnas
forma = titanic.shape
forma


#Cuenta la cantidad de celdas que no estan vacias
titanic.count()


#Eliminar columnas
titanic = titanic.drop(['Cabin'],axis=1)#axis especifica la columna que desea eliminar
titanic

#Renombrar columnas
titanic = titanic.rename(columns={'PassengerId':'ID Pasajero', 'Survived':'Sobrevivio','Name':'Nombre','Age':'Edad'})
titanic


#Saber si un valor es falso
titanic.isnull().sum()


#Cambiar los valores nulos o vacios
titanic['Edad'] = titanic['Edad'].fillna(0)
titanic

#----------------------------------------------------------------o---------------------------------------------------#




"""LIBRERIA MATPLOTLIB"""
#Usar .ipynb en ves de .py para ver las graficas


import matplotlib.pyplot as plt #(pip install matplotlib) libreria graficas
import numpy as np

#Grafica
valores = np.array([1,2,3,4])
plt.plot(valores)
plt.show()

#Grafica de ejes X y Y
valores_x = np.array([1,2,3,4])
valores_y = np.array([4,5,2,1])
plt.plot(valores_x,valores_y)
plt.show()


#Grafica de puntos (o)
plt.plot(valores_x,valores_y,'o')


#Grafica de lineas
plt.plot(valores_x,valores_y,'--')


#Grafico con curvatura
x = np.linspace(0,2*np.pi, 100)
y = np.sin(x)
plt.plot(x,y)
plt.show()


#Grafico histograma
valores = np.random.randn(1000)
plt.hist(valores) #(hist) Grafico histograma
plt.show()


#Distribucion por edades de el df
plt.hist(titanic['Edad'])#llama la columna edad para sacar el grafico de edades
plt.title('Distribucion por edades') #le pone titulo al grafico
plt.xlabel('Edades') #Nombre del eje X
plt.ylabel('Cantidad') #Nombre del eje Y
plt.show()


#Grafico de dispersion
plt.scatter(titanic['Edad'],titanic['Fare']) #(scatter) Grafico de dispersion
plt.xlabel('Edad')
plt.ylabel('Fare')
plt.show()

#Histograma se parado con nombre propio
Nombres = ["Apple","Samsung","Xiaomi"]
valores = [100,50,200]
plt.bar(Nombres,valores)
plt.show()


#Histograma de calor 2D
valores_x = np.random.randn(1000)
valores_y = np.random.randn(1000)
plt.hist2d(valores_x,valores_y) #(hist2d) Grafico 2D de calor
plt.show


#Grafico de barras
eje_x = ['Colombia','Brasil','Peru']
eje_y = [2,7,4]
plt.bar(eje_x,eje_y) #(bar) grafico de barras
plt.title('Grafico de barras')
plt.show()

#Grafico pastel
plt.pie(eje_y,labels=eje_x) #(pie) grafico pastel
plt.show()


#Grafico multiple
valores_x = np.random.randn(10)
valores_y = np.random.randn(10)
plt.figure(figsize=(10,4))
plt.subplot(131) #(1)Fila, (3)Columnas, (1)Posicion
plt.plot(valores_x,valores_y)
plt.title('Grafico Lineas')
plt.xlabel('Eje X')
plt.ylabel('Eje Y')
plt.subplot(132) #(1)Fila, (3)Columnas, (2)Posicion
plt.hist2d(valores_x,valores_y)
plt.title('Histograma 2D')
plt.subplot(133) #(1)Fila, (3)Columnas, (3)Posicion
plt.hist(valores_x,edgecolor = 'black')
plt.title('Histograma')
plt.show()