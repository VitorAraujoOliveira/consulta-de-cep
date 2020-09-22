import pycep_correios
import time
#from API import *
import pandas as pd
import warnings
import numpy as np
warnings.simplefilter(action='ignore', category=FutureWarning)

import json

def verifica_cep_correios(cep):
    
    k = len(cep)-1

    while cep != '00000000':
        try:
            endereco = pycep_correios.get_address_from_cep(cep)
            return json.dumps(endereco)
        except:
            endereco = ("CEP inválido: " + cep)
            pass
       

        cep = cep[:k]
        
        cep = cep + '0'*(8-k)
        k = k -1



        print(endereco)
        #return endereco
    
    return ("Cep não encontrado")




def verifica_cep_local(cep):
    
    k = len(cep)-1

    while cep != '00000000':

        df = pd.read_csv("..\\Base de Ceps\\ceps.csv",error_bad_lines=False, 
        delimiter=';',low_memory=False,  dtype={'cep': object, 'complemento1': object, 'complemento2': object, 'info': object})


        #print(df[df['cep']==cep]['cep'].values[0])
        if(df[df['cep']==cep]['cep'].values):

            cep = (df[df['cep']==cep]['cep'].values[0])
            logra = (df[df['cep']==cep]['logradouro'].values[0])
            cidade = (df[df['cep']==cep]['cidade/estado'].values[0].split('/')[0])
            estado = (df[df['cep']==cep]['cidade/estado'].values[0].split('/')[1])
            bairro = (df[df['cep']==cep]['bairro'].values[0])

            if str(df[df['cep']==cep]['info'].values[0]) != 'nan':
                complemento = (str(df[df['cep']==cep]['info'].values[0]) + ' ' 
                        + str(df[df['cep']==cep]['complemento1'].values[0]) + ' ' 
                        + str(df[df['cep']==cep]['complemento2'].values[0])),
            else:
                complemento = ''

            return ({'bairro': bairro, 
                    'cep': cep, 
                    'cidade': cidade, 
                    'logradouro': logra, 
                    'uf': estado, 
                    'complemento': complemento})

        cep = cep[:k]
        
        cep = cep + '0'*(8-k)
        k = k -1
    
    return ("Cep não encontrado")



def salva_log(resultado_consulta):
    return '' 


def busca_log():
    return ''