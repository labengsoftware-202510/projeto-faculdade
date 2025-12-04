import streamlit as st
import Controllers.crudMatriculaCursos as ctb

@st.dialog('Matricula - Exclusão de Registros')
def delMatriculaCurso(parametro):

    st.write(f'Tem certeza que quer excluir a matrícula de {parametro['nom_com']}?')

    col1, col2, col3, col4, col5 = st.columns(5)
    with col5:
        delButton = st.button(label='Excluir',
                              width='stretch')
    if delButton:
        st.spinner()
        ctb.excluir(parametro)