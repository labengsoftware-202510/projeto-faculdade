import streamlit as st #biblioteca base
import Page.Page_CEP_R as Pg_R   #script da página de listagem da tabelas genéricas
import Controllers.listas as lst    #script de controle de listas por query sql


#parametros da pagina ao mostrar no browser
st.set_page_config(page_title= 'Pessoas', 
                layout= 'wide',
                initial_sidebar_state= 'collapsed')

#titulo da página
st.title('CEP')

listaEstados = lst.listTabGer('est_brl')

#variável com lista para servir de filtro para a tabela
col1, col2, col3, col4, col5 = st.columns(spec=5,
                                          gap=None,
                                          vertical_alignment='center')
with col1:
    filtroLogradouros = st.text_input(label='Filtro por Logradouro',
                                      key= 'fLog')
with col2:
    filtroBairro = st.text_input(label='Filtro por Bairro',
                                 key='fBar')
with col3:
    filtroCidade = st.text_input(label='Filtro por Cidade',
                                 key='fCid')
with col4:
    selecEstado = st.selectbox(label= 'Filtro por Estados',
                                options= listaEstados,
                                format_func= lambda record: f'{record["descricao"]}')
    filtroEstado = selecEstado['valor']
with col5:
    filtroCEP = st.text_input(label='Filtro por CEP',
                              key='fCep',
                              )
    
filtros = ({"logradouro":filtroLogradouros,
            "bairro": filtroBairro,
            "cidade": filtroCidade,
            "estado":filtroEstado,
            "cep":filtroCEP})

st.write(filtros)

#redireciona para o script de página de listagem da tabela
Pg_R.Reg_Cep_R(filtros)
