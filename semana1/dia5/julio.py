class moneda:
    def __init__(self, tipo, cam):
        self.tipo = tipo
        self.cambio = cam
    def mostrar(self):
        print("el cambio es " + self.tipo + " y su cambio a soles es "+ str(self.cambioSoles))
    def convertirSolto (self, monto):
        resultado = monto / self.cambio
        return resultado
    def convertirOtrotoSol (self, monto):
        resultado = monto * self.cambio
        return resultado
dolarToSol = moneda("Dolares a Soles", 3.88)
euroToSol = moneda("Euro a Soles", 4.60)
solToDolar = moneda("Soles a Dolares", 3.73)
solToEuro = moneda("Soles a Euros", 4.10)
origen = input("Ingrese su tipo de cambio \n a) Soles a Dolares \n b) Dolares a soles : ")
monto = float(input("ingrese el monto : "))
if (origen == "a"):
    resultado = solToDolar.convertirSolto(monto)
elif(origen == "b"):
    resultado = dolarToSol.convertirOtrotoSol(monto)
else:
    resultado = "no tenemos ese cambio"
print(resultado)
