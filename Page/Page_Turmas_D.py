import streamlit as st
import Controllers.crudTurmas as ctb

@st.dialog('Cursos - Exclusão de Registros')
def delTurmas(parametro):

    st.write(f'Tem certeza que quer excluir a Truma {parametro['nom_cur']} - {parametro['nom_dis']}?')

    col1, col2, col3, col4, col5 = st.columns(5)
    with col5:
        delButton = st.button(label='Excluir',
                              width='stretch')
    if delButton:
        st.spinner()
        ctb.excluir(parametro)