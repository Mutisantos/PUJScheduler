import sys
import subprocess
import os
reload (sys)
sys.setdefaultencoding("utf-8")

from clases import *
from flask import Flask, render_template,request, send_from_directory

app = Flask(__name__,static_url_path='')

#Diccionario de Lenguajes
LANGAUGE_OPTIONS = [ {"name":"C++/C","value":"1"},{"name":"Java","value":"2" }, {"name":"Python","value":"3"} ]
#Carga de Datos en memoria para la representacion de la informacion
Students = []
Subjects = []
Classes = []
Schedules = []
Inscritos = []
Slots = []

def cargar_datos_entrada():
    
    global Students
    global Schedules
    global Classes
    global Subjects
    Students = []
    Subjects = []
    Classes = []
    Schedules = []
    
    
    with open('materias.txt', 'r') as f:
        
        
        data = f.readlines()
        cont = 0
        num_mats = data[cont]
        cont = cont + 1
        num_mats = int(num_mats)
        Materias = []
        for i in range (0,num_mats):#Materia
            mat = data[cont]
            tokenizado = data[cont].split(",")
            cant = tokenizado[len(tokenizado)-1]
            cont = cont + 1
            clases = []
            for j in range (0, int(cant)):#Clase
                clase = data[cont]
                tokenizado2 = clase.split(",")
                cant_horarios = int(tokenizado2[len(tokenizado2)-1])
                Horarios = []
                cont = cont + 1
                for k in range (0,cant_horarios): #Horario
                    hora = data[cont].split(",")
                    h = Horario(hora[0],hora[1],hora[2])
                    Horarios.append(h)
                    Schedules.append(h)
                    cont = cont + 1
                clase = clase.split(",")
                c = Clase(clase[0],clase[1],clase[2],Horarios)
                clases.append(c)
                Classes.append(c)
                
            mat = mat.split(",")
            m = Materia(mat[1],mat[2],clases)
            Materias.append(m)
            Subjects.append(m)
        
  
        
        
        
                
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
            mats = []
            for j in range (0, 1):
                
                id_clases = data[cont]
                tokenizado2 = id_clases.split(",")
                cant_horarios = int(tokenizado2[len(tokenizado2)-1])
                
                for k in range(0,cant_horarios):
                    m = Subjects[k-1] #El id corresponde a la posicion
                    mats.append(m)
                cont = cont + 1
            s = Estudiante(tokenizado[0],tokenizado[1],tokenizado[2],tokenizado[3],tokenizado[4],mats)
            Students.append(s)
    
        


def cargar_archivo_salida():
    global Inscritos
    Inscritos = []
    with open('salida.txt', 'r') as f:            
        data = f.readlines()
        cont = 0
        num_students = data[cont]
        cont = cont + 1
        for i in range (0,int(num_students)):
            student = data[cont]
            tokenizado = data[cont].split(",")
            cant_ids = tokenizado[len(tokenizado)-1]
            cont = cont + 1
            est = Students[i]
            for j in range (0, 1):
                id_clases = data[cont]
                ids = id_clases.split(",")
                
                inscritas = []
                for k in ids:
                    c = Classes[int(k)-1]
                    inscritas.append(c)
                
                s = Estudiante(est.ID,est.nombre,est.creditos_aprobados,est.semestre,est.carga_academica,inscritas)    
                Inscritos.append(s)
                
                
                #print "El estudiante %s tiene las clases con id's %s " % (student ,data[cont])
                cont = cont + 1
        

def scheduleMorpher(clases):
    horario = []
    for cl in clases:
        for h in cl.horarios:
            ini = int(h.inicio)
            fin = int(h.fin)
            dia = h.dia
            diff = fin - ini
            bloque = ini - 6#Primer horario a las 7
            for i in range (0,diff):
                if("lunes" in dia):
                    sc = Slot(bloque+i,1,cl)
                    horario.append(sc)
                elif("martes" in dia):
                    sc = Slot(bloque+i,2,cl)
                    horario.append(sc)
                elif("miercoles" in dia):
                    sc = Slot(bloque+i,3,cl)
                    horario.append(sc)
                elif("jueves" in dia):
                    sc = Slot(bloque+i,4,cl)
                    horario.append(sc)
                elif("viernes" in dia):
                    sc = Slot(bloque+i,5,cl)
                    horario.append(sc)
                elif("sabado" in dia):
                    sc = Slot(bloque+i,6,cl)
                    horario.append(sc)
                elif("domingo" in dia):
                    sc = Slot(bloque+i,7,cl)
                    horario.append(sc)
                
    print horario
    return horario          




@app.route('/')
def hello_world():
    cargar_datos_entrada()
    return render_template("inicio.html", languages = LANGAUGE_OPTIONS)

@app.route('/execute/',methods=['POST'])
def executefile():

    filename = request.form['filename']
    language = request.form['language']
    command = []
    if(language == "1"):
        command.append("./"+filename)
    elif (language == "2"):
        command.append("java")
        command.append(filename)    
    elif (language == "3"):
        command.append("python")
        command.append(filename)
    print command
    subprocess.call(command)
    #Leer el archivo de texto generado
    #Interpretarlo y enviarlo al template
    cargar_archivo_salida()
    return render_template("selector.html",inscritos = Inscritos)

@app.route('/schedule/',methods=['POST'])
def schedule():
    
    global Inscritos
    estID = request.form['id']
    estudiante = None
    for i in Inscritos:
        if(i.ID == estID):
            estudiante = i
    print estudiante.materias
    slots = scheduleMorpher(estudiante.materias)#Realmente, clases
    bloques = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
    dias = [1,2,3,4,5,6,7]
    return render_template("horarios.html",estudiante = estudiante, slots = slots, bloques = bloques, dias = dias)





if __name__ == '__main__':
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.debug=True 
    app.run(port=8080, host="0.0.0.0")
