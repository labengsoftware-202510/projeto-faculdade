import streamlit as st
import Controllers.crudDisciplinas as ctb
import Controllers.colConfig as cc
import Controllers.estSessaoMsg as statsMsg #script para o status de sessão e mensagens de sistema
import Page.Page_Disciplinas_C as Pg_C
import Page.Page_Disciplinas_U as Pg_U
import Page.Page_Disciplinas_D as Pg_D

def materiasR(filtros = None):
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
                                key='insDisciplinas',
                                help='Click aqui para Inserir um novo Curso',
                                width='stretch')

    if tabela[0]:
        dtFrame = tabela[1]
        rowSel = st.dataframe(data=dtFrame,
                            height=300,
                            selection_mode='single-row',
                            on_select='rerun',
                            column_config=cc.colConfigDisciplina())
        selRow = rowSel.selection.rows
        if selRow:
            selIndex = {'cod_dis': dtFrame['cod_dis'].iloc[selRow].item(),
                        'nom_dis': dtFrame['nom_dis'].iloc[selRow].item(),
                        'dat_inc': dtFrame['dat_inc'].iloc[selRow].item(),
                        'tipo': dtFrame['tipo'].iloc[selRow].item(),
                        'crg_hor_semanal': dtFrame['crg_hor_semanal'].iloc[selRow].item(),
                        'crg_hor_min_semestral': dtFrame['crg_hor_min_semestral'].iloc[selRow].item(),                        
                        'sit': dtFrame['sit'].iloc[selRow].item()}
            fDesativado = False
        else:
            fDesativado = True

        col6, col7, col8, col9, col10 = st.columns(spec=5,
                                                gap=None,
                                                vertical_alignment='center',
                                                )
        
        with col9:
            altButton = st.button(label='Alterar',
                                    key='altDisciplinas',
                                    help='Click aqui para Alteara a Tabela',
                                    width='stretch',
                                    disabled=fDesativado,)
        
        with col10:
            delButton = st.button(label='Deletar',
                                    key='delDisciplinas',
                                    help='Click aqui para Deletar a Tabela',
                                    width='stretch',
                                    disabled=fDesativado,)
    else:
        st.error('Houve um Problema com a pesquisa')
    
    if regButton:
        Pg_C.insDisciplina()
    if altButton:
        Pg_U.altDisciplina(selIndex)
    if delButton:
        Pg_D.delDisciplinas(selIndex)