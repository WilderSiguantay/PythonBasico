'''
Clase padre o superclase
    - subClase

¿Para que nos sirve la herencia?
    - Reutilizar codigo.
    - Las caracteristicas en común que tienen los objetos (Propiedades)
    - Los comportamientos en común de estos objetos (Metodos/Funciones)
'''

#Vehiculos

class Vehiculos():#SUPERCLASE - CLASE_BASE - CLASE_PADRE

    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.enMarcha = False
        self.acelera = False
        self.frena = False

    def arrancar(self):
        self.enMarcha = True

    def acelerar(self):
        self.acelera = True
    
    def frenar(self):
        self.frena = True

    def estado(self):
        print('Marca: ', self.marca, "\nModelo: ", self.modelo,
        '\nEn Marcha: ', self.enMarcha, '\nAcelerando: ', self.acelera,
        '\nFrenando: ', self.frena)


class Moto(Vehiculos):
    hacerCaballito = 'No estoy haciendo caballito'

    def caballito(self):
        self.hacerCaballito = 'Estoy haciendo un caballito'

    def estado(self):
        print('Marca: ', self.marca, "\nModelo: ", self.modelo,
        '\nEn Marcha: ', self.enMarcha, '\nAcelerando: ', self.acelera,
        '\nFrenando: ', self.frena, '\n', self.hacerCaballito)


moto = Moto('Honda', 'CDF')
moto.acelerar()
moto.caballito()
#moto.estado()
    
#CLASE CAMION

class camion(Vehiculos):

    def carga(self, cargar):
        self.cargar = cargar
        if(self.cargar):
            return 'El camion está cargado.'
        else:
            return 'El camion no está cargado.'

micamion = camion('Hyundai', 'SKJ')
#print('-----CAMION----')
micamion.arrancar()
#micamion.estado()
#print( micamion.carga(True))
#print('-----FIN CAMION----')

#HERENCIA MULTIPLE
class VElectricos(Vehiculos):
    #Vehiculos  Electricos
    def __init__(self, marca, modelo):
        super().__init__(marca, modelo)
        self.autonomia = 100 #Autonomia de la bateria

    def cargarEnergia(self):
        self.cargando = True
    

class biciElectrica(VElectricos, Vehiculos):
    pass

mibiciElectrica = biciElectrica('BMX', 'SDD')
mibiciElectrica.arrancar()
mibiciElectrica.acelerar()
mibiciElectrica.cargarEnergia()
mibiciElectrica.estado()



    
