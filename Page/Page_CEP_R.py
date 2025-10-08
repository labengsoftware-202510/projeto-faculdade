import streamlit as st
import Controllers.crudTabGen as ctb
import Controllers.colConfig as cc
import Page.Page_TabGen_C as Pg_C
import Page.Page_TabGen_U as Pg_U
import Page.Page_TabGen_D as Pg_D

def Reg_Tab_Gen_R(filtro):

    tabela = ctb.select(filtro)

    col1, col2, col3, col4, col5 = st.columns(spec=5,
                                                gap=None,
                                                vertical_alignment='center')
    with col5:
        regButton = st.button(label='Registrar', 
                                key='insReg',
                                help='Click aqui para Inserir um novo Registro',
                                width='stretch')

    if tabela[0]:
        dtFrame = tabela[1]
        rowSel = st.dataframe(data=dtFrame,
                            height=300,
                            selection_mode='single-row',
                            on_select='rerun',
                            column_config=cc.colConfig())
        selRow = rowSel.selection.rows
        if selRow:
            selIndex = [dtFrame['dominio'].iloc[selRow].item(),  
                        dtFrame['valor'].iloc[selRow].item(),
                        dtFrame['descricao'].iloc[selRow].item(),
                        dtFrame['obs'].iloc[selRow].item()]

        col6, col7, col8, col9, col10 = st.columns(spec=5,
                                                gap=None,
                                                vertical_alignment='center',
                                                )
        with col9:
            altButton = st.button(label='Alterar',
                                    key='altTab',
                                    help='Click aqui para Alteara a Tabela',
                                    width='stretch')
        
        with col10:
            delButton = st.button(label='Deletar',
                                    key='delTab',
                                    help='Click aqui para Deletar a Tabela',
                                    width='stretch')
    else:
        st.error('Houve um Problema com a pesquisa')
    
    if regButton:
        Pg_C.insTab(selIndex)
    if altButton:
        st.write(Pg_U.altTab(selIndex))
    if delButton:
        Pg_D.delTab(selIndex)