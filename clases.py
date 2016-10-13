class Estudiante(object):
   
    
    def __init__(self, ID, nombre, creditos_aprobados, semestre, carga_academica, materias):
        self.ID = ID
        self.nombre = nombre
        self.creditos_aprobados = creditos_aprobados
        self.semestre = semestre
        self.carga_academica = carga_academica
        self.materias = materias
        
    def __repr__(self):
     return ""+self.ID+"-"+self.nombre
    
class Materia:
    
    
    def __init__(self, ID, numero_creditos, clases):
        self.ID = ID
        self.numero_creditos = numero_creditos
        self.clases = clases
    def __repr__(self):
     return ""+self.ID+"-"+self.numero_creditos       
    
class Clase:
   
    
    def __init__(self, ID, cupos, profesor, horarios):
        self.ID = ID
        self.cupos = cupos
        self.profesor = profesor
        self.horarios = horarios
    def __repr__(self):
     return ""+self.ID+"-"+self.profesor
    
class Horario:
   
    
    def __init__(self, inicio, fin, dia):
        self.inicio = inicio
        self.fin = fin
        self.dia = dia
    def __repr__(self):
     return ""+self.inicio+"-"+self.fin+"-"+self.dia
    