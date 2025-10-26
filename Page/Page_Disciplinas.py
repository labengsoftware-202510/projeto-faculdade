import streamlit as st #biblioteca base
import Page.Page_Disciplinas_R as Pg_R   #script da página de listagem da tabelas genéricas


#parametros da pagina ao mostrar no browser
st.set_page_config(page_title= 'Disciplinas', 
                layout= 'wide',
                initial_sidebar_state= 'collapsed')

#titulo da página
st.title('Disciplinas')

disciplinaFiltro = st.text_input(label='Disciplinas',
                             )

#redireciona para o script de página de listagem da tabela
Pg_R.materiasR(disciplinaFiltro)
