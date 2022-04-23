#crear clase
class Automovil:
    #crear atributos
    def __init__(self,aa,pl,col,mar):
        self.año = aa
        self.placa = pl
        self.color = col
        self.marca = mar
        
    def encender(self):
        print('encender ' + self.marca)
        
    def avanzar(self):
        print('avanzar ' + self.marca)
        
    def acelerar(self):
        print('acelerar ' + self.marca)
        
    def frenar(self):
        print('frenar ' + self.marca)
        
#creación de objetos
vw = Automovil(1970,'CH-1234','Amarillo','Volkswagen')
print("se creo el objeto vw con los datos:")
print("año : " + str(vw.año))
print("color: " + vw.color)
print("placa: " + vw.placa)
print("marca: " + vw.marca)
#utilizar objectos
vw.encender()

tico = Automovil(1985,'EJ-2345','Rojo','TICO')
print("se creo el objeto tico con los datos:")
print("año : " + str(tico.año))
print("color: " + tico.color)
print("placa: " + tico.placa)
print("marca: " + tico.marca)
#utilizar objectos
tico.encender()
tico.frenar()

lamborghini = Automovil(2018,'E7P-367','Amaraillo','Lamborghini')
print("se creo el objeto lamborghini con los datos:")
print("año : " + str(lamborghini.año))
print("color: " + lamborghini.color)
print("placa: " + lamborghini.placa)
print("marca: " + lamborghini.marca)
lamborghini.acelerar()