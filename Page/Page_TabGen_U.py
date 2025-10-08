import streamlit as st
import Controllers.crudTabGen as ctb

@st.dialog('Tabelas Genéricas - Atualização de Registros')
def altTab(parametro):

    dominio = st.text_input(label='Dominio',
                value=parametro[0],
                disabled=True,
                )

    valor = st.text_input(label='Valor',
                  value=parametro[1],
                  disabled=True,
                  )
    
    nDescricao = st.text_input(label='Descrição da Tabela',
                               value=parametro[2],
                               max_chars=60,
                               placeholder='Insira uma Descrição da Tabela',
                               )
    
    nObs = st.text_input(label='Observação',
                         value=parametro[3],
                         max_chars=60,
                         placeholder='Insirao uma Observação',
                         )
    col1, col2, col3, col4, col5 = st.columns(5)
    with col5:
        altButton = st.button(label='Alterar',
                              width='stretch')
    if altButton:
        if not nDescricao:
            st.error('Insira a Descrição da Nova Tabela!')
        else:
            st.spinner()
            ctb.alterar([dominio, valor, nDescricao, nObs])
