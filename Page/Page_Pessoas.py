import streamlit as st #biblioteca base
import Page.Page_Pessoas_R as Pg_R   #script da página de listagem da tabelas genéricas
import Controllers.listas as lst


#parametros da pagina ao mostrar no browser
st.set_page_config(page_title= 'Disciplinas', 
                layout= 'wide',
                initial_sidebar_state= 'collapsed')

#titulo da página
st.title('Pessoas')

filtro = None

col1, col2, col3 = st.columns(3)

with col1:
    pessoasFiltro = st.text_input(label='Pessoas',)
with col2:
    lista = lst.listTabGer('cat_pes')
    categoriaFiltro = st.selectbox(label='Categoria',
                                    options=lista,
                                    format_func=lambda x:x['descricao'])

filtro = {'fNome': pessoasFiltro,
          'fCategoria': categoriaFiltro}

#redireciona para o script de página de listagem da tabela
Pg_R.pessoasR(filtro)
