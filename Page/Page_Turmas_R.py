import streamlit as st
import Controllers.crudTurmas as ctb
import Controllers.colConfig as cc
import Controllers.estSessaoMsg as statsMsg #script para o status de sessão e mensagens de sistema
import Page.Page_Turmas_C as Pg_C
import Page.Page_Turmas_U as Pg_U
import Page.Page_Turmas_D as Pg_D

def turmasR(filtros = None):
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
                                key='insTurma',
                                help='Click aqui para Inserir uma nova Turma',
                                width='stretch')

    if tabela[0]:
        dtFrame = tabela[1]
        rowSel = st.dataframe(data=dtFrame,
                            height=300,
                            selection_mode='single-row',
                            on_select='rerun',
                            column_config=cc.colConfigTurmas())
        selRow = rowSel.selection.rows
        if selRow:
            selIndex = {'cod_tur': dtFrame.loc[selRow[0], 'cod_tur'],
                        'id_grade': dtFrame.loc[selRow[0], 'id_grade'],
                        'nom_cur': dtFrame.loc[selRow[0], 'nom_cur'],
                        'nom_dis': dtFrame.loc[selRow[0], 'nom_dis'],
                        'cap_max': dtFrame.loc[selRow[0], 'cap_max'],
                        'dia_oco': dtFrame.loc[selRow[0], 'dia_oco'],
                        'periodo': dtFrame.loc[selRow[0], 'periodo'],
                        'prof_resp': dtFrame.loc[selRow[0], 'prof_resp'],
                        'sit': dtFrame.loc[selRow[0], 'sit'],}
            fDesativado = False
        else:
            fDesativado = True

        col6, col7, col8, col9, col10 = st.columns(spec=5,
                                                gap=None,
                                                vertical_alignment='center',
                                                )
        
        with col9:
            altButton = st.button(label='Alterar',
                                    key='altTruma',
                                    help='Click aqui para Alteara a Turma',
                                    width='stretch',
                                    disabled=fDesativado,)
        
        with col10:
            delButton = st.button(label='Deletar',
                                    key='delGrade',
                                    help='Click aqui para Deletar a Turma',
                                    width='stretch',
                                    disabled=fDesativado,)
    else:
        st.error('Houve um Problema com a pesquisa')
    
    if regButton:
        Pg_C.insTurmas()
    if altButton:
        Pg_U.altTurmas(selIndex)
    if delButton:
        Pg_D.delTurmas(selIndex)