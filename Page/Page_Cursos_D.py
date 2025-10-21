import streamlit as st
import Controllers.crudCursos as ctb

@st.dialog('Cursos - Exclusão de Registros')
def delCursos(parametro):

    st.write(f'Tem certeza que quer excluir o registro {parametro['nom_cur']}?')

    col1, col2, col3, col4, col5 = st.columns(5)
    with col5:
        delButton = st.button(label='Excluir',
                              width='stretch')
    if delButton:
        st.spinner()
        ctb.excluir(parametro)