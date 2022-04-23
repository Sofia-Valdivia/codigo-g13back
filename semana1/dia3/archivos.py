"""
f = open('alumnos.txt', 'w')
f.write('sofia valdivia,bastet@gmail.com,969332510\n')
f.write('tayra pereira,tayra@gmail.com,256286\n')
f.write('marco lopez,marquito@gmail.com,984265398\n')

"""
f= open('alumnos.txt', 'r')
alumnos = f.read()
print(alumnos)

listaAlumnos = alumnos.splitlines()
print(listaAlumnos)

listaResultado = []

for dictAlumno in listaAlumnos:
    listaDiccionarioAlumnos = dictAlumno.split(',')
    print(listaDiccionarioAlumnos)
    dictAlumno ={
        'nombre': listaDiccionarioAlumnos[0],
        'email': listaDiccionarioAlumnos[1],
        'celular': listaDiccionarioAlumnos[2]
    }
    listaResultado.append(dictAlumno)    
print (listaResultado)
f.close
