import streamlit as st
import Controllers.crudTabGen as ctb

@st.dialog('Tabelas Genéricas - Criação de Registros')
def insTab(parametro):

    st.text_input(label='Dominio',
                max_chars=30,
                value=parametro[0],
                disabled=True,
                )

    nValor = st.text_input(label='Valor',
                            max_chars=30,
                            placeholder='Insira o Valor de Id',
                            )
    
    nDescricao = st.text_input(label='Descrição do Registro',
                            max_chars=60,
                            placeholder='Insira uma do Registro',
                            )
    
    nObs = st.text_input(label='Observação',
                            max_chars=60,
                            placeholder='Insira uma Observação',
                            )
    col1, col2, col3, col4, col5 = st.columns(5)
    with col5:
        insButton = st.button(label='Inserir',
                              width='stretch')
    if insButton:
        if not nValor:
            st.error('Insira o Nome Nova Tabela!')
        elif not nDescricao:
            st.error('Insira a Descrição da Nova Tabela!')
        else:
            st.spinner()
            ctb.inserir([parametro[0], nValor, nDescricao, nObs])
        
