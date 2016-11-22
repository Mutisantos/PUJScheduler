from clases import *


def cargar_datos_entrada():
    
    E = []
    M = {}
    

    with open('estudiantes-materias.txt', 'r') as f:            
        data = f.readlines()
        cont = 0
        num_students = data[cont]
        cont = cont + 1
        for i in range (0,int(num_students)):
            tokenizado = data[cont].split(",")
            student_id = tokenizado[0]
            cant_materias = int(tokenizado[1])
            cont = cont + 1
            clases = tokenizado[2].split(" ")
            c = []
            for j in range (0, cant_materias):
                id_clases = clases[j]
                c.append(id_clases)
                print "El estudiante %s tiene las clases con id's %s " % (student_id, id_clases)
                
            e = Estudiante(student_id, c)
            E.append(e)
        
        num_mats = data[cont]
        cont = cont + 1
        num_mats = int(num_mats)
        
       
        
        for i in range (0,num_mats):
            tokenizado = data[cont].split(",")
            id_materia = tokenizado[0]
            num_creditos = tokenizado[1]
            cont = cont + 1
            tokenizado = data[cont]
            no_clases = tokenizado[0]
            cont = cont + 1
            c = []
            
            for j in range (0, int(no_clases)):
                clase = data[cont]
                tokenizado2 = clase.split(",")
                id_clase = tokenizado2[0]
                hora_inicio = tokenizado2[1]
                hora_fin = tokenizado2[2]
                no_dia = tokenizado2[3]
                no_cupos = tokenizado2[4]
                nom_profesor = tokenizado2[5]
                print "la materia %s tiene la clase %s en el horario: %s - %s el dia %s con el profesor %s" % (id_materia ,id_clase ,hora_inicio, hora_fin, no_dia, nom_profesor)
                cont = cont + 1
                clase = Clase(id_clase, no_cupos, nom_profesor, hora_inicio,hora_fin,no_dia)
                c.append(clase)
            
            m = Materia(id_materia, num_creditos, c)
            M[id_materia] = m
            #M.append(m)
                
    return E, M
               

def  printMaxActivities(E,M):
    
    for k in range (0, len(E)):
         while(len(E[k].materias)>0):
             mat = (E[k].materias).pop()
             
             mat = mat.rstrip('\n')
             mat = mat.rstrip('\r')
             print "Numero de materia %s "% (mat)
             
             for j in range (0, len(M[mat].clases)):
                 if (M[mat].clases[j].cupos > 0):
                    ini = int(M[mat].clases[j].hora_inicio)
                    ini = ini / 100
                    fin = int(M[mat].clases[j].hora_fin) - 1
                    fin = fin / 100
                    
                    dia = int(M[mat].clases[j].dia) - 1
                    flag = True
                    for y in range (ini,fin):
                        print "y %s dia %s" % (y,dia)
                        if(E[k].horario[y][dia] != -1):#no hay espacio para esa clase en ese dia
                            flag = False
                    
                    if (flag):
                        for x in range (ini, fin):
                            E[k].horario[x][dia] = M[mat].clases[j].ID
                        M[mat].clases[j].cupos = int(M[mat].clases[j].cupos) -1
                        

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
    
    E, M = cargar_datos_entrada();
    printMaxActivities(E,M)
    #cargar_archivo_salida();
    
    
    
