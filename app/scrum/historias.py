# -*- coding: utf-8 -*-

#Agregando proyect root
import sys
import os
dir = os.path.abspath(os.path.join(os.path.abspath(__file__), '../../..'))
sys.path.append(dir)

#Dependencias flask
from flask import request, session, Blueprint, json
from sqlalchemy import create_engine
from sqlalchemy.engine.url import URL
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql.expression import text

historias = Blueprint('historias', __name__)

from base import *
from app.scrum.actor import clsActor
from app.scrum.objetivo import clsObjetivo
from app.scrum.accion import clsAccion
from app.scrum.tareas import clsTarea

@historias.route('/historias/ACrearHistoria', methods=['POST'])
def ACrearHistoria():
    #POST/PUT parameters
    params = request.get_json()
    results = [{'label':'/VHistorias', 'msg':['Historia creada']}, {'label':'/VCrearHistoria', 'msg':['Error al crear historia']}, ]
    res = results[0]
    
    #Action code goes here, res should be a list with a label and a message

    idPila = int(session['idPila'])
    his = clsHistoria(session=sessionDB,engine=engine)


    y=his.insertar(codigo=params['codigo'],idAccion=int(params['accion']),tipo=params['tipo'],idProducto=idPila, prioridad = params['prioridad'])
    
    if not y:
        res=results[1]
    else:
        idHistoria=his.obtId(params['codigo'], idPila)
        his.asociarActores(params['actores'], idHistoria)
        his.asociarObjetivos(params['objetivos'], idHistoria)

    res['label'] = res['label'] + '/' + str(idPila)

    #Action code ends here
    
    if "actor" in res:
        if res['actor'] is None:
            session.pop("actor", None)
        else:
            session['actor'] = res['actor']
    return json.dumps(res)

@historias.route('/historias/AElimHistoria')
def AElimHistoria():
    #GET parameter
    results = [{'label':'/VHistorias', 'msg':['Historia eliminada']}, {'label':'/VHistoria', 'msg':['No se pudo eliminar esta historia']}, ]
    res = results[0]
    
    #Action code goes here, res should be a list with a label and a message

    idHistoria = session['idHistoria']
    idPila = session['idPila']

    his = clsHistoria(session=sessionDB,engine=engine)
    his.eliminar(idHistoria)
    res['label'] = res['label'] + '/' + str(idPila)

    #Action code ends here
    
    if "actor" in res:
        if res['actor'] is None:
            session.pop("actor", None)
        else:
            session['actor'] = res['actor']
    return json.dumps(res)

@historias.route('/historias/AModifHistoria', methods=['POST'])
def AModifHistoria():
    #POST/PUT parameters
    params = request.get_json()
    results = [{'label':'/VHistorias', 'msg':['Historia modificada']}, {'label':'/VHistoria', 'msg':['Error al modificar historia']}, ]
    res = results[0]
   
    #Action code goes here, res should be a list with a label and a message
    idHistoria = int(session['idHistoria'])

    #session.pop("idHistoria", None)

    idPila = int(session['idPila'])
    his = clsHistoria(session=sessionDB,engine=engine)

    x=his.modificar(
                idHistoria=idHistoria,
                codigo=params['codigo'],
                idProducto=idPila,
                tipo=params['tipo'],
                idAccion=int(params['accion']),
                prioridad=params['prioridad'],
                idPapa=params['super'])
    if not x:
        res=results[1]
        res['label'] = res['label'] + '/' + str(session['idHistoria'])
    else:
        res['label'] = res['label'] + '/' + str(session['idPila'])
        his.asociarActores(params['actores'], idHistoria)
        his.asociarObjetivos(params['objetivos'], idHistoria)

    #Action code ends here

    if "actor" in res:
        if res['actor'] is None:
            session.pop("actor", None)
        else:
            session['actor'] = res['actor']
    return json.dumps(res)

@historias.route('/historias/VCrearHistoria')
def VCrearHistoria():
    res = {}
    if "actor" in session:
        res['actor']=session['actor']
    
    #Action code goes here, res should be a JSON structure

    if 'usuario' not in session:
      res['logout'] = '/'
      return json.dumps(res)
    res['usuario'] = session['usuario']
    
    #Ejemplo de relleno de listas para selectores
    act=clsActor(engine=engine,session=sessionDB)
    acc=clsAccion(engine=engine,session=sessionDB)
    hist=clsHistoria(engine=engine,session=sessionDB)
    obj=clsObjetivo(engine=engine,session=sessionDB)
    
    aux=act.listarActoresprod(int(session['idPila']))
    for x in aux:
        x['key']=x.pop('idActor')
        x['value']=x.pop('nombre')
    res['fHistoria_opcionesActores'] = aux
    aux=acc.listarAccionesprod(int(session['idPila']))
    for x in aux:
        x['key']=x.pop('idAccion')
        x['value']=x.pop('descripcion')
    res['fHistoria_opcionesAcciones'] = aux
    aux=obj.listarObjetivosprodt(int(session['idPila']))
    for x in aux:
        x['key']=x.pop('idObjetivo')
        x['value']=x.pop('descripcion')
    res['fHistoria_opcionesObjetivos'] = aux
    aux=hist.listarcodigoHistoriasprod(int(session['idPila']))
    for x in aux:
        x['key']=x.pop('idHistoria')
        x['value']=x.pop('enunciado')
    res['fHistoria_opcionesHistorias'] = aux
    res['fHistoria_opcionesTiposHistoria'] = [
      {'key':'1','value':'Opcional'},
      {'key':'2','value':'Obligatoria'}]
    res['fHistoria_opcionesPrioridad'] = hist.listarPrioridades(session['idPila'])
    res['fHistoria'] = {'super':0}
    
    #Action code ends here
    
    return json.dumps(res)

@historias.route('/historias/VHistoria')
def VHistoria():
    res = {}
    if "actor" in session:
        res['actor']=session['actor']
    
    #Action code goes here, res should be a JSON structure
    
    params = request.get_json()

    if 'usuario' not in session:
      res['logout'] = '/'
      return json.dumps(res)

    #Ejemplo de relleno de listas para selectrores
    act=clsActor(engine=engine,session=sessionDB)
    acc=clsAccion(engine=engine,session=sessionDB)
    hist=clsHistoria(engine=engine,session=sessionDB)
    obj=clsObjetivo(engine=engine,session=sessionDB)

    from app.scrum.prod import clsProducto

    oProd = clsProducto(engine,sessionDB)

    aux=act.listarActoresprod(int(session['idPila']))
    for x in aux:
        x['key']=x.pop('idActor')
        x['value']=x.pop('nombre')
    res['fHistoria_opcionesActores'] = aux

    aux=acc.listarAccionesprod(int(session['idPila']))
    for x in aux:
        x['key']=x.pop('idAccion')
        x['value']=x.pop('descripcion')
        x['id']=x['key']
    res['fHistoria_opcionesAcciones'] = aux

    aux=obj.listarObjetivosprodt(int(session['idPila']))
    for x in aux:
        x['key']=x.pop('idObjetivo')
        x['value']=x.pop('descripcion')
    res['fHistoria_opcionesObjetivos'] = aux
    

    aux=hist.listarcodigoHistoriasprod(int(session['idPila']))
    for x in aux:
        x['key']=x.pop('idHistoria')
        x['value']=x.pop('enunciado')
        x['id']=x['key']
    res['fHistoria_opcionesHistorias'] = aux


    aux=hist.listarHistoriasprod(int(session['idPila']))

    for x in aux:
        x['key']=x.pop('idHistoria')
        x['value']=x.pop('enunciado')
        x['id']=x['key']
    res['fHistoria_opcionesTiposHistoria'] = [
      {'key':1,'value':'Opcional'},
      {'key':2,'value':'Obligatoria'}]

    if(oProd.getEscala(session['idPila']) == "cualitativo"):
        res['fHistoria_opcionesPrioridad'] = [
          {'key':1, 'value':'Alta'},
          {'key':7, 'value':'Media'},
          {'key':13, 'value':'Baja'},
        ]
    else:
        res['fHistoria_opcionesPrioridad'] = []
        for i in range(1,21):
            item = {'key':i,'value':i}
            res['fHistoria_opcionesPrioridad'].append(item)

    tar=clsTarea(session=sessionDB,engine=engine)
    
    res['data2'] = tar.listarTareasHistoria(int(request.args['idHistoria']))    
         
    session['idHistoria'] = request.args['idHistoria']

    aux=hist.obtenerDatos(int(session['idHistoria']),res['fHistoria_opcionesHistorias'],res['fHistoria_opcionesAcciones'])

    res['fHistoria'] = {
    'idHistoria':int(session['idHistoria']), 
    'idPila':(session['idPila']), 
    'codigo':hist.obtCode(int(session['idHistoria'])),
    'actores':aux['actores'], 
    'accion':aux['accion'], 
    'objetivos':aux['objetivos'], 
    'tipo':aux['tipo'],
    'prioridad':aux['prioridad'],
    'super':aux['super'], }

    res['idHistoria']     = session['idHistoria']

    session['codHistoria']= hist.obtCode(int(session['idHistoria']))    

    #Action code ends here

    return json.dumps(res)

@historias.route('/historias/VHistorias')
def VHistorias():
    res = {}
    if "actor" in session:
        res['actor']=session['actor']
    
    #Action code goes here, res should be a JSON structure
    
    if 'usuario' not in session:
      res['logout'] = '/'
      return json.dumps(res)

    #Datos de prueba
    his=clsHistoria(engine=engine,session=sessionDB)
    res['idPila'] = session['idPila']
    res['data0'] = his.listarHistoriasprod(int(session['idPila']))
    
    #Action code ends here
    
    return json.dumps(res)

@historias.route('/historias/ACambiarPrioridades', methods=['POST'])
def ACambiarPrioridades():
    #POST/PUT parameters
    params = request.get_json()
    results = [{'label':'/VHistorias', 'msg':['Prioridades reasignadas']}, ]
    res = results[0]
    
    #Action code goes here, res should be a list with a label and a message
    
    hist=clsHistoria(engine=engine,session=sessionDB)
    idHistorias=[]
    prioridades=[]
    lista=params['lista']
    
    for x in lista:
        idHistorias.append(x['idHistoria'])
        prioridades.append(x['prioridad'])
        
    hist.modificarPrioridades(idHistorias,prioridades)
    res['label'] = res['label']+ "/"+str(session['idPila'])

    #Action code ends here

    if "actor" in res:
        if res['actor'] is None:
            session.pop("actor", None)
        else:
            session['actor'] = res['actor']
    return json.dumps(res)

@historias.route('/historias/VPrioridades')
def VPrioridades():
    #GET parameter
    idPila = request.args['idPila']
    res = {}
    if "actor" in session:
        res['actor']=session['actor']
    
    #Action code goes here, res should be a JSON structure
    
    if 'usuario' not in session:
      res['logout'] = '/'
      return json.dumps(res)
    res['usuario'] = session['usuario']

    his=clsHistoria(engine=engine,session=sessionDB)
    res['idPila'] = session['idPila']

    #Escala dependiente del proyecto
    res['fPrioridades_opcionesPrioridad'] = his.listarPrioridades(int(session['idPila']))

    aux = his.listarHistoriasprod(int(session['idPila']))
    
    res['fPrioridades'] = { 'idPila':session['idPila'], 'lista': aux}

    #Action code ends here
   
    return json.dumps(res)


@historias.route('/historias/VDesempeno')
def VDesempeno():
    #GET parameter
    idHistoria = request.args['idHistoria']
    res = {}
    if "actor" in session:
        res['actor']=session['actor']
    #Action code goes here, res should be a JSON structure

    res['idHistoria'] = int(idHistoria) 
    res['hola'] = 2

    #Action code ends here
    return json.dumps(res)

#Use case code starts here

# Clase historia
class clsHistoria():
    
    def __init__(self,engine=None,session=None):
        
        self.engine  = engine
        self.session = session

    def obtenerDatos(self,idHistoria,papas,acciones):
        res={}
        result = self.session.query(Historia).filter(Historia.idHistoria == idHistoria)
        res['objetivos']=[]
        res['actores']=[]


        for row in result:
            res['super']=row.idHistoriaPadre
            res['accion']=row.idAccion    


            res['prioridad']=row.prioridad
            if row.tipo=='opcional':
                res['tipo']=1
            else:
                res['tipo']=2   

        result = self.session.query(ObjetivosHistoria).filter(ObjetivosHistoria.idHistoria == idHistoria)

        for row in result:
            res['objetivos'].append(row.idObjetivo)

        result = self.session.query(ActoresHistoria).filter(ActoresHistoria.idHistoria == idHistoria)

        for row in result:
            res['actores'].append(row.idActor)

        return res


    ''' Funcion insertar
        Funcion que inserta una historia 
    '''
    def insertar(self,codigo=None,idProducto=None,idPapa=None,tipo=None,idAccion=None,prioridad=None):

        #No nulidad
        nulidadesValidas = idProducto!=None and tipo != None and codigo != None \
                           and idAccion != None and prioridad != None
        if not nulidadesValidas:
            return False

        
        #Verificaciones de entrada
        tiposCorrectos = (type(codigo)     is str) and \
                         (type(idProducto) is int) and \
                         (type(tipo)       is str) and \
                         (type(idAccion)   is int) and \
                         (type(idPapa)     is int  or   idPapa   == None) and \
                         (type(prioridad)     is int or str)    
        
        if tiposCorrectos:
            pass
        else:
            return False


        producto = self.session.query(Producto).filter(Producto.idProducto == idProducto)

        #Protecciones de funcion
        stringsVacios    = codigo == '' or tipo == ''
        estaEnDb         = self.existeHistoria(codigo=codigo,idProducto=idProducto)
        existeProducto   = producto.count() > 0
        longCharValido   = (len(codigo) <= 500) and (len(tipo) <= 15)
        tieneLoops       = self.tieneLoops(idProducto,idPapa,codigo)
        
        esValido = (not stringsVacios) and (not estaEnDb) and existeProducto\
                    and longCharValido and (not tieneLoops)
        
        if type(prioridad) is int:
            if ((prioridad<1) and (prioridad>20)):
                return False
        elif type(prioridad) is str:
            if not ((prioridad=='Alta')or(prioridad=='Media')or(prioridad=='Baja')):
                return False
        else:
            return False
        
        if esValido:

            newHis = Historia(codigo=codigo,idProducto=idProducto,idAccion=idAccion,tipo=tipo,prioridad=prioridad,idHistoriaPadre=idPapa)
            self.session.add(newHis)
            self.session.commit()
            return True
        else:
            return False
    
    ''' Funcion modificarPrioridades
         Funcion que modifica las prioridades de una historia
    '''
    def modificarPrioridades(self,idHistorias,prioridades):

        for i in range(len(idHistorias)):
            self.session.query(Historia).filter(Historia.idHistoria == idHistorias[i]).\
                 update({'prioridad' : prioridades[i] })
            self.session.commit()

    ''' Funcion modificar
        Funcion que actualiza una historia
    '''
    def modificar(
                    self,
                    idHistoria=None,
                    codigo=None,
                    idProducto=None,
                    idPapa=None,
                    tipo=None,
                    idAccion=None,
                    prioridad=None):

        #No nulidad
        nulidadesValidas = idProducto!=None and tipo != None and codigo != None \
                           and idAccion != None and prioridad != None and idHistoria!=None
        if not nulidadesValidas:
            return False

        tiposCorrectos = (type(codigo)     is str) and \
                         (type(idProducto) is int) and \
                         (type(idHistoria) is int) and \
                         (type(tipo)       is int ) and \
                         (type(idAccion)   is int) and \
                         (type(idPapa)     is int  or   idPapa   == None) and \
                         (type(prioridad)     is int or str)    


        if tiposCorrectos:
            pass
        else:
            return False

        producto = self.session.query(Producto).filter(Producto.idProducto == idProducto)

        #Protecciones de funcion
        stringsVacios    = codigo == '' or tipo == ''
        estaEnDb         = self.existeHistoria(codigo=codigo,idProducto=idProducto)
        existeProducto   = producto.count() > 0
        longCharValido   = (len(codigo) <= 500) and (tipo ==1 or tipo ==2)
        tieneLoops       = self.tieneLoops(idProducto,idPapa,codigo)
        rangoVal         = ((prioridad >=1) and (prioridad<=20))
        
        esValido = (not stringsVacios) and (not estaEnDb) and existeProducto\
                    and longCharValido and (not tieneLoops) and rangoVal
        
        self.session.query(Historia).filter(Historia.idHistoria == idHistoria).\
             update({'idHistoria' : idHistoria })
        self.session.commit()

        self.session.query(Historia).filter(Historia.idHistoria == idHistoria).\
            update({'codigo':codigo})
        self.session.commit()

        self.session.query(Historia).filter(Historia.idHistoria == idHistoria).\
            update({'idProducto':idProducto})
        self.session.commit()

        if (idPapa != None and idPapa != 0):
            self.session.query(Historia).filter(Historia.idHistoria == idHistoria).\
                update({'idHistoriaPadre':idPapa})
            self.session.commit()
        if tipo==1:
            tipo='opcional'
        else:
            tipo='obligatoria'
        self.session.query(Historia).filter(Historia.idHistoria == idHistoria).\
            update({'tipo':tipo})
        self.session.commit()

        self.session.query(Historia).filter(Historia.idHistoria == idHistoria).\
            update({'idAccion':idAccion})
        self.session.commit()

        self.session.query(Historia).filter(Historia.idHistoria == idHistoria).\
            update({'prioridad':prioridad})
        self.session.commit()

        self.session.query(ActoresHistoria).filter(
                                    ActoresHistoria.idHistoria == idHistoria).\
                delete()
        self.session.commit()

        self.session.query(ObjetivosHistoria).filter(
                                    ObjetivosHistoria.idHistoria == idHistoria).\
                delete()
        self.session.commit()

        return True
    
    ''' Funcion obtId
        Funcion para obtener el id de la historia    
    '''
    def obtId(self,codigo=None,idProducto=None):
        
        if codigo==None or idProducto==None:
            return -1
        
        res  = self.session.query(Historia).filter(Historia.codigo == codigo)
        res  = res.filter(Historia.idProducto == idProducto)
        for i in res:
            return i.idHistoria

    ''' Funcion obtCode
        Funcion para obtener el codigo de la historia
    '''
    def obtCode(self,idHistoria=None):
        
        if idHistoria==None:
            return -1
        
        res  = self.session.query(Historia).filter(Historia.idHistoria == idHistoria)
        for i in res:
            return i.codigo
    
    ''' Funcion asociarActores
        Funcion para asociar actores a una historia    
    '''
    def asociarActores(self,idActores=None,idHistoria=None):
        if idActores==[] or idHistoria==None or idActores==None:
            return False
        
        #Desasociando viejos
        res  = self.session.query(ActoresHistoria).filter(ActoresHistoria.idHistoria == idHistoria)
        res.delete()
        self.session.commit()

        for id in idActores:
            newAH = ActoresHistoria(idHistoria,id)
            self.session.add(newAH)
            self.session.commit()
            
        return True
    
    ''' Funcion asociarObjetivos
        Funcion para asociar objetivos a una historia
    '''
    def asociarObjetivos(self,idObjetivos=None,idHistoria=None):
        if idObjetivos==[] or idHistoria==None or idObjetivos==None:
            return False
        
        #Desasociando viejos
        res  = self.session.query(ObjetivosHistoria).filter(ObjetivosHistoria.idHistoria == idHistoria)
        res.delete()
        self.session.commit()

        for id in idObjetivos:
            newOH = ObjetivosHistoria(idHistoria,id)
            self.session.add(newOH)
            self.session.commit()
            
        return True

    ''' Funcion tieneLoops
         Funcion que verifica si es una epica
    '''
    def tieneLoops(self,idProducto=None,idPapa=None,codigo=None):
        
        if idProducto==None or codigo==None or idPapa==None:
            return False

        res  = self.session.query(Historia).filter(Historia.idProducto == idProducto and Historia.idHistoria == idPapa)
        
        while (res.first()).idHistoriaPadre!=None:
            if (res.first()).codigo!=codigo:
                return True
            else:
                res  = self.session.query(Historia).filter(Historia.idProducto == idProducto and Historia.idHistoria == idPapa)
                idPapa=(res.first()).idHistoria
        return False
    
    ''' Funcion existeHistoria
         Funcion que verifica la existencia de una historia    
    '''
    def existeHistoria(self,codigo,idProducto):
        
        #Verificaciones de entrada
        tiposCorrectos = (type(codigo) is str) and (type(idProducto) is int) 
        
        if tiposCorrectos:
            result  = self.session.query(Historia).filter(Historia.idProducto == idProducto).filter(Historia.codigo == codigo)
            return result.count() > 0
        else:
            return False

    ''' Funcion listarPrioridades
         Funcion que lista las prioriades
    '''
    def listarPrioridades(self,idProducto):
        res=[]
        conversion=False
        
        #Revisando escala de producto
        result = self.session.query(Producto).filter(Producto.idProducto == idProducto)
        
        for row in result:
            if row.escala=='cualitativo':
                conversion=True
                break
        
        result = self.session.query(Historia).filter(Historia.idProducto == idProducto)
        
        if conversion:
            res=[{'key':1,'value':'Alta'},{'key':7,'value':'Media'},{'key':13,'value':'Baja'}]
        else:
            for i in range(1,20):
                res+=[{'key':i,'value':str(i)}]
        
        return res
    
    ''' Funcion listarHistoriasprod
         Funcion que lista las historias ordenadad por prioridades
    '''
    def listarHistoriasprod(self,idProducto): 
        
        res = []
        orden = []
        conversion=False

        
        #Revisando escala de producto
        result = self.session.query(Producto).filter(Producto.idProducto == idProducto)
        
        for row in result:
            if row.escala=='cualitativo':
                conversion=True
                break
        
        result = self.session.query(Historia).filter(Historia.idProducto == idProducto)
        
        contador=0
        for row in result:
            
            enunciado = "En tanto que "

            actoresAsoc = self.session.query(ActoresHistoria,Actor).\
                            filter(ActoresHistoria.idHistoria == row.idHistoria).\
                            filter(ActoresHistoria.idActor == Actor.idActor)
            i = 0
            for actor in actoresAsoc:
                enunciado += actor[1].nombre  
                if(i==actoresAsoc.count()-2):
                    enunciado += " y "
                elif(i < actoresAsoc.count()-2):
                    enunciado += ", "
                else:
                    pass
                i+=1

            if (row.tipo == "obligatorio") :
                enunciado += " puedo "
            else:
                enunciado += " podria "

            accionEncontrada = self.session.query(Historia,Accion).\
                            filter(Historia.idHistoria == row.idHistoria).\
                            filter(Historia.idAccion == Accion.idAccion)

            for acc in accionEncontrada:
                enunciado += acc[1].descripcion + " para "

            objetivosAsoc = self.session.query(ObjetivosHistoria,Objetivo).\
                            filter(ObjetivosHistoria.idHistoria == row.idHistoria).\
                            filter(ObjetivosHistoria.idObjetivo == Objetivo.idObjetivo)
            
            i = 1
            for obj in objetivosAsoc:
                if (obj[1].transversal == "no transversal"):
                    enunciado += obj[1].descripcion
                    if (i==objetivosAsoc.count()-1):
                        enunciado += "."
                    elif(i==objetivosAsoc.count()-2):
                        enunciado += " y "
                    elif(i < objetivosAsoc.count()-2):
                        enunciado += ", "
                    i+=1
            
            prioridad=row.prioridad

            if conversion:
                if prioridad<=6:
                    prioridad='Alta'
                elif prioridad>=7 and prioridad<13:
                    prioridad='Media'
                else:
                    prioridad='Baja'

                    
            tareasAsociadas = self.session.query(Tarea).\
                            filter(Tarea.idHistoria == row.idHistoria)
            contadorpeso=0
            for tar in tareasAsociadas:
                contadorpeso=contadorpeso + tar.peso
                            
            rexaux={'idHistoria':row.idHistoria,'enunciado':enunciado,'prioridad':prioridad,'peso':contadorpeso}
            orden.append((row.prioridad,rexaux))

        orden.sort(key=lambda tup: tup[0])

        for x in orden:
            res.append(x[1])

        else:
            pass

        return res


    def listarcodigoHistoriasprod(self,idProducto): #Ordenar por prioridad
                                              #Eliminar verificacion de transversalidad.
        
        res = []
       
        #Revisando escala de producto
        result = self.session.query(Historia).filter(Historia.idProducto == idProducto)
        
        for row in result:
            res.append({'idHistoria':row.idHistoria,'enunciado':row.codigo})

        return res


    ''' Funcion borrarFilas
        Funcion que limpia las historias de la base de datos    
    '''
    def borrarFilas(self):
        
        self.session.query(Historia).delete()
        self.session.commit()

    ''' Funcion eliminar
        Funcion que permite eliminar la historia
    '''
    def eliminar(self,idHistoria):

        # Desasociando viejos
        res  = self.session.query(ActoresHistoria).filter(ActoresHistoria.idHistoria == idHistoria)
        res.delete()
        self.session.commit()

        # Desasociando viejos
        res  = self.session.query(ObjetivosHistoria).filter(ObjetivosHistoria.idHistoria == idHistoria)
        res.delete()
        self.session.commit()

        self.session.query(Tarea).filter(Tarea.idHistoria == idHistoria).delete()

        result = self.session.query(Historia).filter(Historia.idHistoria == idHistoria).delete()
        if result:
            return True
        else:
            return False

#Use case code ends here