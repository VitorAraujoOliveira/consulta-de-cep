import pycep_correios
import time
#from API import *
import pandas as pd
import warnings
import numpy as np
warnings.simplefilter(action='ignore', category=FutureWarning)
from datetime import datetime
from datetime import date

import json



def verifica_cep_correios(cep):
    cep_inicial = cep
    k = len(cep)-1

    while cep != '00000000':
        try:
            endereco = pycep_correios.get_address_from_cep(cep)

            salva_log('Correios' + ';' + 'CEP encontrado' + ';' 
                + cep_inicial + ';' + endereco['cep'] + ';' 
                + endereco['cidade'] + ';' + endereco['uf'] + ';' 
                + endereco['logradouro'] + ';' + endereco['bairro'])
            
            return (endereco)

        except Exception as err:
            endereco = ("CEP inválido: " + cep + str(err))
            pass
       

        
        cep = cep[:k]
        
        cep = cep + '0'*(8-k)
        k = k -1




        #return endereco
    
    salva_log('Correios' + ';' + "Cep não encontrado")
    return ("Cep não encontrado")




def verifica_cep_local(cep):
    cep_inicial = cep
    k = len(cep)-1

    while cep != '00000000':

        df = pd.read_csv("..\\Base de Ceps\\ceps.csv",error_bad_lines=False, encoding = "ISO-8859-1",
        delimiter=';',low_memory=False,  dtype={'cep': object, 'complemento1': object, 'complemento2': object, 'info': object})


        #print(df[df['cep']==cep]['cep'].values[0])
        if(df[df['cep']==cep]['cep'].values):

            ceps = (df[df['cep']==cep]['cep'].values[0])
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


            retorno = ({'bairro': bairro, 
                    'cep': ceps, 
                    'cidade': cidade, 
                    'logradouro': logra, 
                    'uf': estado, 
                    'complemento': complemento})


            
            salva_log('Local' + ';' + 'CEP encontrado' + ';' + cep_inicial + ';' + ceps + ';' 
                    + cidade + ';' + estado + ';' + logra + ';' + bairro)
            return retorno

        cep = cep[:k]
        
        cep = cep + '0'*(8-k)
        k = k -1

    salva_log('Local' + ';' + "Cep não encontrado" + ';' + ';' + ';' + ';' + ';' + ';' )
    return ("Cep não encontrado")



def salva_log(resultado_consulta):
    now = datetime.now()
    data = now.strftime("%d/%m/%Y %H:%M:%S")
    with open("..\\LOGs\\logs.csv", "a") as myfile:
        myfile.write(resultado_consulta + ';' + data + '\n')



def busca_log():
    df = pd.read_csv("..\\LOGs\\logs.csv",error_bad_lines=False, encoding = "ISO-8859-1",
        delimiter=';',low_memory=False,  dtype={'cep_pesquisado': object, 'cep_retornado': object})

    return df.to_json()

