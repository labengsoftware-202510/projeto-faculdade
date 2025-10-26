import streamlit as st
import Controllers.crudTabGen as ctb

@st.dialog('Tabelas Genéricas - Atualização de Registros')
def altTab(parametro):

    dominio = st.text_input(label='Dominio',
                value=parametro['dominio'],
                disabled=True,
                )

    valor = st.text_input(label='Valor',
                  value=parametro['valor'],
                  disabled=True,
                  )
    
    nDescricao = st.text_input(label='Descrição da Tabela',
                               value=parametro['descricao'],
                               max_chars=60,
                               placeholder='Insira uma Descrição da Tabela',
                               )
    
    nObs = st.text_input(label='Observação',
                         value=parametro['obs'],
                         max_chars=60,
                         placeholder='Insirao uma Observação',
                         )
    
    valores = {'dominio': dominio,
               'valor': valor,
               'descricao': nDescricao,
               'obs': nObs}
    
    col1, col2, col3, col4, col5 = st.columns(5)
    with col5:
        altButton = st.button(label='Alterar',
                              width='stretch')
    if altButton:
        if not nDescricao:
            st.error('Insira a Descrição da Nova Tabela!')
        else:
            st.spinner()
            ctb.alterar(valores)
