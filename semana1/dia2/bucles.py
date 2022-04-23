#entrada
tabla = int(input("Ingresa la tabla de multiplicar que desea mostrar : "))
#proceso
valor1 = tabla * 1;
valor2 = tabla * 2;
valor3 = tabla * 3;
valor4 = tabla * 4;
valor5 = tabla * 5;
#salida
print(str(tabla) + ' X 1 = ' + str(valor1))
print(str(tabla) + ' X 2 = ' + str(valor2))
print(str(tabla) + ' X 3 = ' + str(valor3))
print(str(tabla) + ' X 4 = ' + str(valor4))
print(str(tabla) + ' X 5 = ' + str(valor5))



#TABLA DE MULTIPLICAR USANDO FOR, teniendo un contador que se incremente de 1 en 1
print("TABLA USANDO FOR")
for contador in range(1,12,3):
    valor = tabla * contador
    #print(str(tabla) + ' X ' + str(contador) + ' = ' + str(valor))
    print(tabla,' X ',contador,' = ',valor)