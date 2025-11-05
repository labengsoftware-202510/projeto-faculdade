import streamlit as st
import Controllers.crudPessoas as ctb

@st.dialog('Pessoas - Exclusão de Registros')
def delPessoas(parametro):

    st.write(f'Tem certeza que quer excluir {parametro['nom_com']} ?')

    col1, col2, col3, col4, col5 = st.columns(5)
    with col5:
        delButton = st.button(label='Excluir',
                              width='stretch')
    if delButton:
        st.spinner()
        ctb.excluir(parametro)