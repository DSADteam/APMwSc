'''
Created on 24/9/2014
@author: Jean Carlos
Modified by: Nabil Marquez and Meggie Sanchez
'''

import uuid
import hashlib
import re

class clsAccessControl(object):
    def __init__(self):
        ohast=''

    
    def matchRegex(self,value,regularExpression):
        lc = re.compile(regularExpression)
        x= lc.findall(value)
        return x!=[] 
    

    def encript(self, value):
        # Inicializacion
        oHash=""    
        # Verificar la longitud del password
        olength_password=self.length_password(value)
        if olength_password>=8 and olength_password<=16:
            #Vericar que tenga minuscula
            if (self.matchRegex(value,'[a-z]+')):
                #Vericar que tenga mayuscula
                if (self.matchRegex(value,'[A-Z]+')):
                    #Vericar que tenga numero
                    if (self.matchRegex(value,'[0-9]+')):
                        #Vericar que tenga caracter especial
                        if (self.matchRegex(value,'(\.|\#|\!|\@|\?|\¿|\¡|\+|\-|\_|\%|\*|\(|\))+')):
                            #Vericar que no tenga otros caracteres
                            lc = re.compile('(\.|\#|\!|\@|\?|\¿|\¡|\+|\-|\_|\%|\*|\(|\)|[0-9]|[A-Z]|[a-z])')
                            x= lc.findall(value)
                            y=any(e not in x  for e in value)
                            if (not y):
                                # uuid es usado para generar numeros random
                                salt = uuid.uuid4().hex
                                # hash
                                oHash= hashlib.sha256(salt.encode() + value.encode()).hexdigest() + ':' + salt    
                                return oHash
                            else:
                                print('El password contiene caracteres invalidos.')
                                return oHash
            print('El password carece de caracteres requeridos.')
        else:
            print('El Password no posee la cantidad de caracteres requerida')
        return oHash
        
        
   

    def check_password(self, oPassworkEncript, oCheckPassword):
            oPassworkEncript, salt = oPassworkEncript.split(':')
            return oPassworkEncript == hashlib.sha256(salt.encode() + oCheckPassword.encode()).hexdigest()
    
    def length_password(self, user_password):
        # uuid es usado para generar numeros random
        return len(user_password)
    
#Para evitar que se ejecute al ser importado
def main():
    pass

if __name__ == "__main__":
        #Para encriptar un passwork  
        oPassword = input('Por favor ingrese su password: ')
        #Se crea un objeto tipo clsAccessControl
        oAccessControl=clsAccessControl()
            #Para validar el passwork introducido
        oCheckPassword = input('Para verificar su password, ingreselo nuevamente: ')
        if oAccessControl.check_password(oPassworkEncript, oCheckPassword):
            print('Ha introducido el password correcto')
        else:
            print('El password es diferente')