import streamlit as st
import Controllers.crudCEP as ctb

@st.dialog('Tabelas Genéricas - Exclusão de Registros')
def delTab(parametro):

    st.write(f'Tem certeza que quer excluir o registro {parametro['cep']} - {parametro['logradouro']}?')

    col1, col2, col3, col4, col5 = st.columns(5)
    with col5:
        delButton = st.button(label='Excluir',
                              width='stretch')
    if delButton:
        st.spinner()
        ctb.excluir(parametro)