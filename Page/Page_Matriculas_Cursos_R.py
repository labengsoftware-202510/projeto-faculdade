import streamlit as st
import datetime as datetime
import Controllers.crudMatriculaCursos as ctb
import Controllers.colConfig as cc
import Controllers.estSessaoMsg as statsMsg #script para o status de sessão e mensagens de sistema
import Page.Page_Matriculas_Cursos_C as Pg_C
import Page.Page_Matriculas_Cursos_U as Pg_U
import Page.Page_Matriculas_Cursos_D as Pg_D

def mCursosR(filtros):
    fDesativado = True
    tabela = ctb.select(filtros)
    selIndex = None

    #menssagem de sucesso/erro
    if ('commandOk' in st.session_state) and ('statusMessage' in st.session_state):
        statsMsg.mostraMensagem()

    

    col1, col2, col3, col4, col5 = st.columns(spec=5,
                                                gap=None,
                                                vertical_alignment='center')
    with col5:
        regButton = st.button(label='Registrar', 
                                key='insMatriculaCurso',
                                help='Click para Matrícular',
                                width='stretch')

    if tabela[0]:
        dtFrame = tabela[1]
        rowSel = st.dataframe(data=dtFrame,
                            height=150,
                            selection_mode='single-row',
                            on_select='rerun',
                            column_config=cc.colConfigMatriculaCursos())
        selRow = rowSel.selection.rows
        
        if selRow:
            selIndex = {'reg_ins': dtFrame['reg_ins'].iloc[selRow].item(),
                        'nom_com': dtFrame['nom_com'].iloc[selRow].item(),
                        'cod_cur': dtFrame['cod_cur'].iloc[selRow].item(),
                        'nom_cur': dtFrame['nom_cur'].iloc[selRow].item(),
                        'dat_inc': dtFrame['dat_inc'].iloc[selRow].item(),
                        'dat_fin': dtFrame['dat_fin'].iloc[selRow].item(),
                        'dat_max': dtFrame['dat_max'].iloc[selRow].item(),
                        'estado': dtFrame['estado'].iloc[selRow].item(),
                        'sit': dtFrame['sit'].iloc[selRow].item(),
                        'dip_env': dtFrame['dip_env'].iloc[selRow].item(),
                        }
            fDesativado = False
        else:
            fDesativado = True
            
    else:
        st.error('Houve um Problema com a pesquisa')

    col13, col14, col15, col16, col17 = st.columns(spec=5,
                                                gap=None,
                                                vertical_alignment='center',
                                                )
        
    with col16:
        altButton = st.button(label='Alterar',
                                key='altMatriculaCurso',
                                help='Click aqui para Alteara a Matrícula',
                                width='stretch',
                                disabled=fDesativado,)
    
    with col17:
        delButton = st.button(label='Deletar',
                                key='delMatriculaCurso',
                                help='Click aqui para Deletar a Matrícula',
                                width='stretch',
                                disabled=fDesativado,)
    
    if regButton:
        Pg_C.insMatriculaCursos()
    if altButton:
        Pg_U.altMatriculaCursos(selIndex)
    if delButton:
        Pg_D.delMatriculaCurso(selIndex)