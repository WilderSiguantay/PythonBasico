class MyClass:
    #atributos (propiedades) de MyClass
    name = 'My CLASE'
    x = 10
    y = ['My', 'Class']

    #operaciones (Metodos) de MyClass
    def print(name):
        print(name)

#Crear objeto
# MyClass mc = new MyClass() --JAVA

#Crear objeto en Python
myclass_ = MyClass()

print('El nombre de mi clase es: ' , myclass_.name)

myclass_.name = "PRUEBA DE CAMBIO DE NOMBRE"

print('El nombre de mi clase es: ' , myclass_.name)


#clase persona

class Person:
    #self es equivalente a this en otros lenguajes de programacion
    #la funcion Init es el equivalente al constructor. 

    def __init__(self, name, age, altura, ubicacion):
        self.name = name #atributo --propiedad--
        self.age = age #atributo --propiedad--
        self.altura = altura #atributo --propiedad--
        self.ubicacion = ubicacion #atributo --propiedad--

    #Operaciones - Metodos - 
    def presentacion(self):
        print('Hello, mi nombre es: ',self.name)

    #Operaciones - Metodos - 
    def getUbicacion(self):
        print('Soy de: ' , self.ubicacion)

p1 = Person('José', '21', '1.78', 'Guatemala')
persona2 = Person('Andrés', '25', '1.70', 'Guatemala')

print("Nombre: ", p1.name, ' - Edad: ',p1.age)
persona2.presentacion()

#Modificacion de propiedades de un objeto
p1.name = "José Barrientos"
p1.presentacion()

#Eliminar propiedad de un objeto

print(p1.age)
del p1.age

print(p1.age)
#eliminar objeto
del p1

p1.presentacion()
