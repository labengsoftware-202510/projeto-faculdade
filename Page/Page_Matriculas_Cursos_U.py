import streamlit as st
import pandas as pd
from datetime import date
from dateutil.relativedelta import relativedelta
import Controllers.listas as lst
import Controllers.crudMatriculaCursos as ctb
    
@st.dialog('Matrícula em Cursos')
def altMatriculaCursos(parametros):

    listaAlunos = lst.listaAlunos()
    indexAluno = lst.buscaIndexAlunos(listaAlunos, parametros['reg_ins'])
    selAluno  = st.selectbox(label='Aluno',
                             options= listaAlunos,
                            format_func= lambda record: f'{record["nom_com"]}',
                            index= indexAluno,
                            )
    nRegIns = selAluno['reg_ins']
    nNomCom = selAluno['nom_com']
    
    listaCursos = lst.listaCursos()
    indexCurso = lst.buscaIndexCursos(listaCursos, parametros['cod_cur'])
    selCurso    = st.selectbox(label='Curso',
                             options= listaCursos,
                            format_func= lambda record: f'{record["nom_cur"]}',
                            index= indexCurso,
                            )
    nCodCur = selCurso['cod_cur']
    nNomCur = selCurso['nom_cur']
    
    listaEstado = lst.listTabGer('sit_alu_cur')
    indexEstado = lst.buscaIndex(listaEstado, parametros['estado'])
    estado  = st.selectbox(label='Situação da Matrícula',
                             options= listaEstado,
                            format_func= lambda record: f'{record["descricao"]}',
                            index= indexEstado,
                            )
    nEstado = estado['valor']
    
    sit = ''
    nSit = st.toggle(label= 'Situação',
                    value=True if parametros['sit']=='Ativo' else False,
                    key='tSit',
                    )

    if nSit:
        st.write('Ativo')
        sit = 'Ativo'
    else:
        st.write('Inativo')
        sit = 'Inativo'
    
    nDipEnv   = st.checkbox(label='Diploma Enviado',
                            value=True if parametros['dip_env']=='S' else False,
                           )
    if nDipEnv:
        dipEnv = 'S'
    else:
        dipEnv = 'N'
    

    parametros = {'reg_ins': nRegIns,
                   'nom_com': nNomCom,
                   'cod_cur': nCodCur,
                   'nom_cur': nNomCur,
                   'estado': nEstado,
                   'sit': sit,
                   'dip_env': dipEnv,
                   'dat_inc': parametros['dat_inc'],
                   'dat_fin': parametros['dat_fin'],
                  }

    col1, col2, col3, col4, col5 = st.columns(5)
    with col5:
        insButton = st.button(label='Alterar',
                              width='stretch')
    
    if insButton:
        st.spinner()
        ctb.alterar(parametros)
