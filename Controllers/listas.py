import streamlit as st
import pandas as pd

def listTabGer(filtro):
    selectQuery = f"select *"
    selectQuery += f" from tab_ger"
    if filtro is None:
        selectQuery += f";"
    else:
        selectQuery += f" where dominio = '{filtro}';"

    conn = st.connection('mysql', type='sql')
    df = pd.DataFrame([{'dominio':filtro, 
                            'valor':'',
                            'descricao':'Selecione...',
                            'obs':''}])
    addRow = conn.query(selectQuery,
                        ttl=600)
    
    dfRetorno = pd.concat([df,addRow],ignore_index=True)
    return dfRetorno.to_dict('records')

def listaCep():
    selectQuery = f"select cep "
    selectQuery += f"from tab_ger "
    conn = st.connection('mysql', type='sql')
    df = pd.DataFrame([{'cep':''}])
    addRow = conn.query(selectQuery,
                        ttl=600)
    
    dfRetorno = pd.concat([df,addRow],ignore_index=True)
    return dfRetorno.to_dict('records')

def buscaCep(lista, valorBuscado):
    for item in enumerate(lista):
        if item['cep'] == valorBuscado:
            return True
    return False

def buscaIndex(lista, valorBuscado):
    for index, item in enumerate(lista):
        if item['valor'] == valorBuscado:
            return index
    return None