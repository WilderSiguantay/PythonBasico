class Persona():
    def __init__(self, nombre, edad, lugarResidencia):
        self.nombre = nombre
        self.edad = edad
        self.residencia = lugarResidencia

    def descripcion(self):
        print('Nombre: ', self.nombre,
        '\nEdad: ', self.edad, '\nResidencia: ', self.residencia)

    

class Empleado(Persona):

    def __init__(self, salario, antiguedad, nombreEmpleado, edadEmpleado, residenciaEmpleado):
        super().__init__(nombreEmpleado, edadEmpleado,residenciaEmpleado)
        '''
        Super está llamando al metodo de la clase padre, al nada mas ejecutar
        el constructor, ejecuta inmediatamente el metodo init de la superclase,
        el cual se ejecuta antes del metodo init de la subclase
        '''
        self.salario = salario
        self.antiguedad = antiguedad

    #Reescribir metodo descripcion
    def descripcion(self):
        super().descripcion()
        print('Salario: ', self.salario, '\nAntiguedad: ', self.antiguedad, ' Años')


Julio = Empleado(2000,2, 'Julio Juarez', 25,'Guatemala')
Julio.descripcion()

#PRINCIPIO DE SUSTITUCION
'''
ES SIEMPRE UN/UNA
El objeto que es una subclase siempre será un objeto de la superclase.
--> Un empleado siempre es una persona
--> Una persona no siempre es un empleado
'''

#FUNCION IS INSTANCE

'''
Nos indica si un objeto de instancia de una clase determinada.
Isinstance, nos devuelve true, si pertenece a una clase en concreto
o False si no pertenece
'''
Josue = Persona('Josue', 18, 'Colombia')
print(isinstance(Julio,Persona))
Josue.descripcion()

print(isinstance(Josue, Empleado))