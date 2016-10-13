from clases import *


def cargar_datos_entrada():
    
    
    with open('materias.txt', 'r') as f:
        data = f.readlines()
        cont = 0
        num_mats = data[cont]
        cont = cont + 1
        num_mats = int(num_mats)
        
        for i in range (0,num_mats):
            materia = data[cont]
            tokenizado = data[cont].split(",")
            cant = tokenizado[len(tokenizado)-1]
            cont = cont + 1
            
            for j in range (0, int(cant)):
                clase = data[cont]
                tokenizado2 = clase.split(",")
                cant_horarios = int(tokenizado2[len(tokenizado2)-1])
                cont = cont + 1
                for k in range (0,cant_horarios):
                    print "la materia %s tiene la clase %s en el horario %s" % (materia ,clase ,data[cont])
                    cont = cont + 1
                
    with open('estudiantes.txt', 'r') as f:            
        data = f.readlines()
        cont = 0
        num_students = data[cont]
        cont = cont + 1
        
        
        for i in range (0,int(num_students)):
            student = data[cont]
            tokenizado = data[cont].split(",")
            cant_ids = tokenizado[len(tokenizado)-1]
            cont = cont + 1
            for j in range (0, 1):
                id_clases = data[cont]
                tokenizado2 = id_clases.split(",")
                cant_horarios = int(tokenizado2[len(tokenizado2)-1])
                print "El estudiante %s tiene las clases con id's %s " % (student ,data[cont])
                cont = cont + 1
               

def cargar_archivo_salida():
    
    with open('salida.txt', 'r') as f:            
        data = f.readlines()
        cont = 0
        num_students = data[cont]
        cont = cont + 1
        
        print "----- archivo salida -------"
        
        for i in range (0,int(num_students)):
            student = data[cont]
            tokenizado = data[cont].split(",")
            cant_ids = tokenizado[len(tokenizado)-1]
            cont = cont + 1
            for j in range (0, 1):
                id_clases = data[cont]
                tokenizado2 = id_clases.split(",")
                cant_horarios = int(tokenizado2[len(tokenizado2)-1])
                print "El estudiante %s tiene las clases con id's %s " % (student ,data[cont])
                cont = cont + 1



if __name__ == '__main__':
    
    cargar_datos_entrada();
    cargar_archivo_salida();
    
    
    
