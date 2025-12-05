import streamlit as st #biblioteca base
import Page.Page_Graficos_R as Pg_R   #script da página de listagem da tabelas genéricas


#parametros da pagina ao mostrar no browser
st.set_page_config(page_title= 'Gráficos', 
                layout= 'wide',
                initial_sidebar_state= 'collapsed')

#titulo da página
st.title('Gráficos')

col1, col2, col3, col4, col5 = st.columns(5)
opcoes = [{'indice': 1, 'titulo': 'Gráficos por Curso'},
          {'indice': 2, 'titulo': 'Gráficos por Disciplina'},
          {'indice': 3, 'titulo': 'Gráficos por Aluno'},]

with col1:
    fgrafico = st.selectbox(label='Gráficos',
                               options= opcoes,
                               format_func= lambda reg: reg['titulo']
                                )
    fgrafico = fgrafico['indice']

filtros = {'grafico': fgrafico}
#redireciona para o script de página de listagem da tabela
Pg_R.graficos(filtros)