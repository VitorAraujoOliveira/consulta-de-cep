import pycep_correios
import time
#from API import *
import pandas as pd



def verifica_cep_correios(cep):
    
    k = len(cep)-1

    while cep != '00000000':


        cep = cep[:k]
        
        cep = cep + '0'*(8-k)
        k = k -1

        try:
            endereco = pycep_correios.get_address_from_cep(cep)
            return endereco
        except:
            endereco = ("CEP inválido: " + cep)
            pass
       

        print(endereco)
        #return endereco
    
    return ("Cep não encontrado")




def verifica_cep_local(cep):
    
    k = len(cep)-1

    while cep != '00000000':


        cep = cep[:k]
        
        cep = cep + '0'*(8-k)
        k = k -1

        try:
            endereco = pycep_correios.get_address_from_cep(cep)
            return endereco
        except:
            endereco = ("CEP inválido: " + cep)
            pass
       

        print(endereco)
        #return endereco
    
    return ("Cep não encontrado")


