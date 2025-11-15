import streamlit as st
import Controllers.crudGrade as ctb
import Controllers.colConfig as cc
import Controllers.estSessaoMsg as statsMsg #script para o status de sessão e mensagens de sistema
import Page.Page_Grade_C as Pg_C
import Page.Page_Grade_U as Pg_U
import Page.Page_Grade_D as Pg_D

def gradesR(filtros = None):
    selIndex = None
    fDesativado = True

    #menssagem de sucesso/erro
    if ('commandOk' in st.session_state) and ('statusMessage' in st.session_state):
        statsMsg.mostraMensagem()

    tabela = ctb.select(filtros)

    col1, col2, col3, col4, col5 = st.columns(spec=5,
                                                gap=None,
                                                vertical_alignment='center')
    with col5:
        regButton = st.button(label='Registrar', 
                                key='insGrade',
                                help='Click aqui para Inserir uma nova Grade',
                                width='stretch')

    if tabela[0]:
        dtFrame = tabela[1]
        rowSel = st.dataframe(data=dtFrame,
                            height=300,
                            selection_mode='single-row',
                            on_select='rerun',
                            column_config=cc.colConfigGrade())
        selRow = rowSel.selection.rows
        if selRow:
            selIndex = {'id_grade': dtFrame['id_grade'].iloc[selRow].item(),
                        'cod_cur': dtFrame['cod_cur'].iloc[selRow].item(),
                        'cod_dis': dtFrame['cod_dis'].iloc[selRow].item(),
                        'sem_ind': dtFrame['sem_ind'].iloc[selRow].item(),
                        'estado': dtFrame['estado'].iloc[selRow].item(),
                        'sit': dtFrame['sit'].iloc[selRow].item(),                        
                        'dat_ini': dtFrame['dat_ini'].iloc[selRow].item(),
                        'dat_fin': dtFrame['dat_fin'].iloc[selRow].item(),
                        'id_grade_n': dtFrame['id_grade_n'].iloc[selRow].item(),
                        'id_grade_d': dtFrame['id_grade_d'].iloc[selRow].item(),
                        'nom_cur': dtFrame['nom_cur'].iloc[selRow].item(),
                        'nom_dis': dtFrame['nom_dis'].iloc[selRow].item(),}
            fDesativado = False
        else:
            fDesativado = True

        col6, col7, col8, col9, col10 = st.columns(spec=5,
                                                gap=None,
                                                vertical_alignment='center',
                                                )
        
        with col9:
            altButton = st.button(label='Alterar',
                                    key='altGrade',
                                    help='Click aqui para Alteara a Tabela',
                                    width='stretch',
                                    disabled=fDesativado,)
        
        with col10:
            delButton = st.button(label='Deletar',
                                    key='delGrade',
                                    help='Click aqui para Deletar a Tabela',
                                    width='stretch',
                                    disabled=fDesativado,)
    else:
        st.error('Houve um Problema com a pesquisa')
    
    if regButton:
        Pg_C.insGrade()
    if altButton:
        Pg_U.altGrade(selIndex)
    if delButton:
        Pg_D.delGrade(selIndex)