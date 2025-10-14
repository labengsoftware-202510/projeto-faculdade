import streamlit as st
import Controllers.crudCEP as ctb
import Controllers.colConfig as cc
import Controllers.estSessaoMsg as statsMsg #script para o status de sessão e mensagens de sistema
import Page.Page_CEP_C as Pg_C
import Page.Page_CEP_U as Pg_U
# import Page.Page_TabGen_D as Pg_D

def Reg_Cep_R(filtros):
    selIndex = []

    #menssagem de sucesso/erro
    if ('commandOk' in st.session_state) and ('statusMessage' in st.session_state):
        msg = statsMsg.mostraMensagem()

    tabela = ctb.select(filtros)

    col1, col2, col3, col4, col5 = st.columns(spec=5,
                                                gap=None,
                                                vertical_alignment='center')
    with col5:
        regButton = st.button(label='Registrar', 
                                key='insCep',
                                help='Click aqui para Inserir um novo Registro',
                                width='stretch')

    if tabela[0]:
        dtFrame = tabela[1]
        rowSel = st.dataframe(data=dtFrame,
                            height=300,
                            selection_mode='single-row',
                            on_select='rerun',
                            column_config=cc.colConfigCep())
        selRow = rowSel.selection.rows
        if selRow:
            selIndex = {'cep': dtFrame['cep'].iloc[selRow].item(),  
                        'logradouro': dtFrame['logradouro'].iloc[selRow].item(),
                        'bairro': dtFrame['bairro'].iloc[selRow].item(),
                        'cidade': dtFrame['cidade'].iloc[selRow].item(),
                        'estado': dtFrame['estado'].iloc[selRow].item()}
        st.write(selIndex)

        col6, col7, col8, col9, col10 = st.columns(spec=5,
                                                gap=None,
                                                vertical_alignment='center',
                                                )
        with col9:
            altButton = st.button(label='Alterar',
                                    key='altCep',
                                    help='Click aqui para Alteara a Tabela',
                                    width='stretch')
        
        with col10:
            delButton = st.button(label='Deletar',
                                    key='delCep',
                                    help='Click aqui para Deletar a Tabela',
                                    width='stretch')
    else:
        st.error('Houve um Problema com a pesquisa')
    
    if regButton:
        Pg_C.insCEP()
        if msg in dir():
            msg.empty()
    # if altButton:
        # Pg_U.alterar(selIndex)
        # msg.empty()
    # if delButton:
    #     Pg_D.delTab(selIndex)