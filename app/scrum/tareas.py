# -*- coding: utf-8 -*-
from flask import request, session, Blueprint, json

tareas = Blueprint('tareas', __name__)


@tareas.route('/tareas/ACrearTarea', methods=['POST'])
def ACrearTarea():
    #POST/PUT parameters
    params = request.get_json()
    results = [{'label':'/VHistoria', 'msg':['Tarea creada']}, {'label':'/VCrearTarea', 'msg':['No se pudo crear tarea.']}, ]
    res = results[0]
    #Action code goes here, res should be a list with a label and a message

    idHistoria = 2
    res['label'] = res['label'] + '/' + repr(idHistoria)

    #Action code ends here
    if "actor" in res:
        if res['actor'] is None:
            session.pop("actor", None)
        else:
            session['actor'] = res['actor']
    return json.dumps(res)



@tareas.route('/tareas/AElimTarea')
def AElimTarea():
    #POST/PUT parameters
    params = request.get_json()
    results = [{'label':'/VHistoria', 'msg':['Historia borrada']}, {'label':'/VTarea', 'msg':['No se pudo eliminar esta tarea']}, ]
    res = results[0]
    #Action code goes here, res should be a list with a label and a message

    res['label'] = res['label'] + '/1'

    #Action code ends here
    if "actor" in res:
        if res['actor'] is None:
            session.pop("actor", None)
        else:
            session['actor'] = res['actor']
    return json.dumps(res)



@tareas.route('/tareas/AModifTarea', methods=['POST'])
def AModifTarea():
    #POST/PUT parameters
    params = request.get_json()
    results = [{'label':'/VHistoria', 'msg':['Tarea modificada']}, {'label':'/VCrearTarea', 'msg':['No se pudo modificar esta tarea.']}, ]
    res = results[0]
    #Action code goes here, res should be a list with a label and a message

    idHistoria = 2
    res['label'] = res['label'] + '/' + repr(idHistoria)

    #Action code ends here
    if "actor" in res:
        if res['actor'] is None:
            session.pop("actor", None)
        else:
            session['actor'] = res['actor']
    return json.dumps(res)



@tareas.route('/tareas/VCrearTarea')
def VCrearTarea():
    #GET parameter
    idHistoria = request.args['idHistoria']
    res = {}
    if "actor" in session:
        res['actor']=session['actor']
    #Action code goes here, res should be a JSON structure

    if 'usuario' not in session:
      res['logout'] = '/'
      return json.dumps(res)
    res['usuario'] = session['usuario']
    res['codHistoria'] = 'H01'


    #Action code ends here
    return json.dumps(res)



@tareas.route('/tareas/VTarea')
def VTarea():
    #GET parameter
    idTarea = request.args['idTarea']
    res = {}
    if "actor" in session:
        res['actor']=session['actor']
    #Action code goes here, res should be a JSON structure

    if 'usuario' not in session:
      res['logout'] = '/'
      return json.dumps(res)
    res['usuario'] = session['usuario']
    res['codHistoria'] = 'H01'


    #Action code ends here
    return json.dumps(res)


#Use case code starts here
class clsTarea():
    
    def __init__(self,engine=None,session=None):
        
        self.engine  = engine
        self.session = session

    def insertar(self,idHistoria,descripcion):

        tiposCorrectos = (type(descripcion) is str) and \
                         (type(idHistoria)  is int)

        #unless tipos correctos
        if not tiposCorrectos:
            return false

        estaEnBd       = self.existeTarea(descripcion=descripcion)
        
        longCharValido = (len(descripcion) <= 500)

        if (not estaEnBd) and (longCharValido):
            newObj = Tarea(descripcion,idHistoria)
            self.session.add(newObj)
            self.session.commit()
            return True
        else:
            return False


    ##Me quede por aqui
    def existeTarea(self,descripcion):
        
        if not(type(descripcion) is str):
            return False
        
        if(descripcion!=None):
            result = self.session.query(Objetivo).filter(Objetivo.descripcion == descripcion)
        else:
            return False
        
        return result.count() > 0

                    
    def listarTareasHistoria(self,idHistoria):
        
        res = []
        #result = self.engine.execute("select * from \"Objetivos\" where idProducto= "+str(idProducto)+" ;")
        result = self.session.query(Objetivo).filter(Objetivo.idProducto == idProducto)
        if result!="":
            for row in result:
                res.append({'idObjetivo':row.idObjetivo,'descripcion':row.descripcion, 'transversal':row.transversal})
            else:
                print("Empty query!")
        
        return res

    
    def borrarFilas(self):
        
        self.session.query(Objetivo).delete()
        self.session.commit()


    #Funcion que permite actualizar la descripcion
    def modificar(self,descripcion=None,idHistoria=None):
        
        tipoid=(id!=None) and (type(id) is int) 
        tipodesc= (type(descripcion) is str) 

        tipotransv=(type(trans) is str)
        
        if tipoid and tipodesc and tipotransv and ((trans=="transversal") or (trans=="no transversal")):
            if(len(descripcion)>500): 
                return False
            self.session.query(Objetivo).filter(Objetivo.idObjetivo == id).\
                update({'descripcion' : descripcion })
            self.session.commit()
            
            self.session.query(Objetivo).filter(Objetivo.idObjetivo == id).\
                update({'transversal' : trans })
            self.session.commit()
            return True
        else:
            return False
       
#Use case code ends here
    """
    ESTA VAINA NO LA NECESITAMOS
    def mostrarObjetivo(self,idObjetivo):
        result = self.session.query(Objetivo).filter(Objetivo.idObjetivo == idObjetivo)
        if result!="":
            for row in result:
                res = {'idObjetivo':row.idObjetivo,'descripcion':row.descripcion, 'transversal':row.transversal}
            else:
                print("Empty query!")
        return res

    def listarTareas(self):
        
        res = []
        result = self.engine.execute("select * from \"Objetivos\";")
        if result!="":
            for row in result:
                res.append({'idObjetivo':row.idObjetivo,'descripcion':row.descripcion, 'transversal':row.transversal})
            else:
                print("Empty query!")
    def listarObjetivosprodt(self,idProducto):
        
        res = []
        #result = self.engine.execute("select * from \"Objetivos\" where idProducto= "+str(idProducto)+" ;")
        result = self.session.query(Objetivo).filter(Objetivo.idProducto == idProducto)
        if result!="":
            for row in result:
                if row.transversal=='no transversal':
                    res.append({'idObjetivo':row.idObjetivo,'descripcion':row.descripcion, 'transversal':row.transversal})
            else:
                print("Empty query!")
        
        return res
    def getProdId(self,idObjetivo):
        result = self.session.query(Objetivo).filter(Objetivo.idObjetivo == idObjetivo)
        for row in result:
            x=row.idObjetivo
        return x
    
    """
