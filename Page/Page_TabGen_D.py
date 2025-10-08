import streamlit as st
import Controllers.crudTabGen as ctb

@st.dialog('Tabelas Genéricas - Exclusão de Registros')
def delTab(parametro):

    st.write(f'Tem certeza que quer excluir o registro {parametro[1]}')

    col1, col2, col3, col4, col5 = st.columns(5)
    with col5:
        delButton = st.button(label='Excluir',
                              width='stretch')
    if delButton:
        st.spinner()
        ctb.excluir([parametro[0], parametro[1]])
