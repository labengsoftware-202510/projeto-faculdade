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

def buscaIndex(lista, valorBuscado):
    for index, item in enumerate(lista):
        if item['valor'] == valorBuscado:
            return index
    return None
###################################################################################################
def listaCep():
    selectQuery = f"select cep, concat(substr(lpad(cep,8,'0'), 1, 5),'-',substr(lpad(cep,8,'0'), 6, 3)) as cep_format "
    selectQuery += f"from tab_cep "
    conn = st.connection('mysql', type='sql')
    df = pd.DataFrame([{'cep':'',
                        'cep_format':'Selecione...'}])
    addRow = conn.query(selectQuery,
                        ttl=600)
    
    dfRetorno = pd.concat([df,addRow],ignore_index=True)
    return dfRetorno.to_dict('records')

def buscaCep(lista, valorBuscado):
    for item in enumerate(lista):
        if item['cep'] == valorBuscado:
            return True
    return False

def buscaIndexCep(lista, valorBuscado):
    for index, item in enumerate(lista):
        if item['cep'] == valorBuscado:
            return index
    return None
###################################################################################################
def listaCursos():
    selectQuery = f"select cod_cur, nom_cur "
    selectQuery += f"from cursos "
    conn = st.connection('mysql', type='sql')
    df = pd.DataFrame([{'cod_cur':'',
                        'nom_cur':'Selecione...'}])
    addRow = conn.query(selectQuery,
                        ttl=600)
    dfRetorno = pd.concat([df,addRow],ignore_index=True)
    return dfRetorno.to_dict('records')

def buscaIndexCursos(lista, valorBuscado):
    for index, item in enumerate(lista):
        if item['cod_cur'] == valorBuscado:
            return index
    return None
###################################################################################################
def listaDisciplinas():
    selectQuery = f"select cod_dis, nom_dis "
    selectQuery += f"from disciplinas "
    conn = st.connection('mysql', type='sql')
    df = pd.DataFrame([{'cod_dis':'',
                        'nom_dis':'Selecione...'}])
    addRow = conn.query(selectQuery,
                        ttl=600)
    dfRetorno = pd.concat([df,addRow],ignore_index=True)
    return dfRetorno.to_dict('records')

def buscaIndexDisciplinas(lista, valorBuscado):
    for index, item in enumerate(lista):
        if item['cod_dis'] == valorBuscado:
            return index
    return None
###################################################################################################
def listaGradeDependente(parametros):
    selectQuery = f"select g.id_grade, concat(c.nom_cur, ' - ', d.nom_dis) as descricao "
    selectQuery += f"from grade g, cursos c, disciplinas d "
    selectQuery += f"where g.cod_cur = c.cod_cur "
    selectQuery += f"and g.cod_dis = d.cod_dis "
    selectQuery += f"and g.cod_cur = {parametros['cod_cur']} "
    selectQuery += f"and g.sem_ind < cast({parametros['sem_ind']} as unsigned);"
    conn = st.connection('mysql', type='sql')
    df = pd.DataFrame([{'id_grade':'',
                        'descricao':'Selecione...'}])
    addRow = conn.query(selectQuery,
                        ttl=600)
    dfRetorno = pd.concat([df,addRow],ignore_index=True)
    return dfRetorno.to_dict('records')

def buscaIndexGradeDependente(lista, valorBuscado):
    for index, item in enumerate(lista):
        if item['id_grade'] == valorBuscado:
            return index
    return 0

def listaGradeSubstituta(parametros):
    selectQuery = f"select g.id_grade, concat(c.nom_cur, ' - ', d.nom_dis) as descricao "
    selectQuery += f"from grade g, cursos c, disciplinas d "
    selectQuery += f"where g.cod_cur = c.cod_cur "
    selectQuery += f"and g.cod_dis = d.cod_dis "
    selectQuery += f"and g.cod_cur = {parametros['cod_cur']} "
    conn = st.connection('mysql', type='sql')
    df = pd.DataFrame([{'id_grade':'',
                        'descricao':'Selecione...'}])
    addRow = conn.query(selectQuery,
                        ttl=600)
    dfRetorno = pd.concat([df,addRow],ignore_index=True)
    return dfRetorno.to_dict('records')

def buscaIndexGradeSubstituta(lista, valorBuscado):
    for index, item in enumerate(lista):
        if item['id_grade'] == valorBuscado:
            return index
    return 0