import streamlit as st #biblioteca base
import Page.Page_Matriculas_Turmas_R as Pg_R   #script da página de listagem da tabelas genéricas
import Controllers.listas as lst


#parametros da pagina ao mostrar no browser
st.set_page_config(page_title= 'Matriculas - Turmas', 
                layout= 'wide',
                initial_sidebar_state= 'collapsed')

#titulo da página
st.title('Matriculas - Turmas')

filtro = None
pessoasFiltro = ''

col1, col2, col3 = st.columns(3)

with col1:
    pessoasFiltro = st.text_input(label='Pessoas',)

filtro = {'nom_com': pessoasFiltro}

#redireciona para o script de página de listagem da tabela
Pg_R.mTurmasR(filtro)
