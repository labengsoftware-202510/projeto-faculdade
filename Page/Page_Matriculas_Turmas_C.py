import streamlit as st
import pandas as pd
from datetime import date
from dateutil.relativedelta import relativedelta
import Controllers.listas as lst
import Controllers.crudMatriculaTurmas as ctb
    
@st.dialog('Matrícula em Cursos')
def insMatriculaTurmas():
    listaAlunos = lst.listaAlunos()

    #regIns - gerado automaticamente pelo banco de dados
    selAluno  = st.selectbox(label='Aluno',
                             options= listaAlunos,
                            format_func= lambda record: f'{record["nom_com"]}',
                            )
    nRegIns = selAluno['reg_ins']
    nNomCom = selAluno['nom_com']
    
    listaTurmas = lst.listaTurmas()
    selCurso    = st.selectbox(label='Curso',
                               options= listaTurmas,
                               format_func= lambda record: f'{record["turma"]}',
                              )
    nCodTur = selCurso['cod_tur']
    nNomTur = selCurso['turma']
    
    listaEstado = lst.listTabGer('sit_alu_tur')
    estado  = st.selectbox(label='Situação da Matrícula',
                             options= listaEstado,
                            format_func= lambda record: f'{record["descricao"]}',
                            )
    nEstado = estado['valor']

    nFaltas = st.number_input(label='Número de Faltas',
                              min_value=0,
                              max_value=200,
                              value=0,
                             )
    nNota1 = st.number_input(label='Nota 1',
                              min_value=0.0,
                                max_value=10.0,
                                value=0.0,
                                format="%.2f",
                             )
    nNota2 = st.number_input(label='Nota 2',
                              min_value=0.0,
                                max_value=10.0,
                                value=0.0,
                                format="%.2f",
                             )
    nNota3 = st.number_input(label='Nota 3',
                              min_value=0.0,
                                max_value=10.0,
                                value=0.0,
                                format="%.2f",
                             )
    nNota4 = st.number_input(label='Nota 4',
                              min_value=0.0,
                                max_value=10.0,
                                value=0.0,
                                format="%.2f",
                             )
    nMedia = st.number_input(label='Média',
                              value=(nNota1 + nNota2 + nNota3 + nNota4) / 4,
                                format="%.2f",
                                disabled=True,
                                )
    
    nCodCurat_ini = st.date_input(label='Data de Início',
                            value=date.today(), 
                            )
    
    nDat_fin = st.date_input(label='Data de Término',
                            value=date.today(),
                            )

    parametros = {'reg_ins': nRegIns,
                   'nom_com': nNomCom,
                   'cod_tur': nCodTur,
                   'nom_tur': nNomTur,
                   'estado': nEstado,
                    'faltas': nFaltas,
                    'nota1': nNota1,
                    'nota2': nNota2,
                    'nota3': nNota3,
                    'nota4': nNota4,
                    'media': nMedia,
                    'dat_ini': nCodCurat_ini,
                    'dat_fin': nDat_fin
                  }

    col1, col2, col3, col4, col5 = st.columns(5)
    with col5:
        insButton = st.button(label='Inserir',
                              width='stretch')
    
    if insButton:
        st.spinner()
        ctb.inserir(parametros)
