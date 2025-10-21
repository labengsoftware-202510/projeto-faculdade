import streamlit as st #biblioteca base
import Page.Page_Cursos_R as Pg_R   #script da página de listagem da tabelas genéricas


#parametros da pagina ao mostrar no browser
st.set_page_config(page_title= 'Cursos', 
                layout= 'wide',
                initial_sidebar_state= 'collapsed')

#titulo da página
st.title('Cursos')

cursoFiltro = st.text_input(label='Curso',
                             )

#redireciona para o script de página de listagem da tabela
Pg_R.cursosR(cursoFiltro)
