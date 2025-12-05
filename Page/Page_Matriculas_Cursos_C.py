import streamlit as st
import pandas as pd
from datetime import date
from dateutil.relativedelta import relativedelta
import Controllers.listas as lst
import Controllers.crudMatriculaCursos as ctb
    
@st.dialog('Matrícula em Cursos')
def insMatriculaCursos():
    listaAlunos = lst.listaAlunos()

    #regIns - gerado automaticamente pelo banco de dados
    selAluno  = st.selectbox(label='Aluno',
                             options= listaAlunos,
                            format_func= lambda record: f'{record["nom_com"]}',
                            )
    nRegIns = selAluno['reg_ins']
    nNomCom = selAluno['nom_com']
    
    listaCursos = lst.listaCursos()
    selCurso    = st.selectbox(label='Curso',
                             options= listaCursos,
                            format_func= lambda record: f'{record["nom_cur"]}',
                            )
    nCodCur = selCurso['cod_cur']
    nNomCur = selCurso['nom_cur']
    
    listaEstado = lst.listTabGer('sit_alu_cur')
    estado  = st.selectbox(label='Situação da Matrícula',
                             options= listaEstado,
                            format_func= lambda record: f'{record["descricao"]}',
                            )
    nEstado = estado['valor']
    
    sit = ''
    nSit = st.toggle(label= 'Situação',
                    value=False,
                    key='tSit',
                    )

    if nSit:
        st.write('Ativo')
        sit = 'Ativo'
    else:
        st.write('Inativo')
        sit = 'Inativo'
    
    nDipEnv   = st.checkbox(label='Diploma Enviado',
                            value=False,
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
                   'dat_inc': date.today(),
                   'dat_fin': None,
                   'dat_max': date.today() + relativedelta(years=8),
                  }

    col1, col2, col3, col4, col5 = st.columns(5)
    with col5:
        insButton = st.button(label='Inserir',
                              width='stretch')
    
    if insButton:
        st.spinner()
        ctb.inserir(parametros)
