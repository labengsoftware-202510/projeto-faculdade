import streamlit as st
import Controllers.crudGrade as ctb

@st.dialog('Grade de Disciplina - Exclusão de Registros')
def delGrade(parametro):

    st.write(f'Tem certeza que quer excluir o registro {parametro['nom_cur']} - {parametro['nom_dis']}?')

    col1, col2, col3, col4, col5 = st.columns(5)
    with col5:
        delButton = st.button(label='Excluir',
                              width='stretch')
    if delButton:
        st.spinner()
        ctb.excluir(parametro)