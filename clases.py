
class Estudiante(object):
   
    
    def __init__(self, ID ,materias):
        self.ID = ID
        self.materias = materias
        self.horario = [[-1]*7 for i in range(23)]
        
    def __repr__(self):
     return "Id: "+self.ID+" - Materias: "
    
class Materia:
    
    
    def __init__(self, ID, numero_creditos, clases):
        self.ID = ID
        self.numero_creditos = numero_creditos
        self.clases = clases
    def __repr__(self):
     return ""+self.ID+"-"+self.numero_creditos       
    
class Clase:
   
    
    def __init__(self, ID, cupos, nom_profesor, hora_inicio, hora_fin, dia):
        self.ID = ID
        self.cupos = cupos
        self.dia = dia
        self.nom_profesor = nom_profesor
        self.hora_inicio = hora_inicio
        self.hora_fin = hora_fin
    def __repr__(self):
     return ""+self.ID+"-"+self.nom_profesor
    

class Slot:

    def __init__(self, posicion, dia, clase):
        self.posicion = posicion
        self.dia = dia
        self.clase = clase
    def __repr__(self):
     return ""+str(self.posicion)+"-"+str(self.dia)+"-"+self.clase.profesor
