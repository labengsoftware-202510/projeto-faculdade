import streamlit as st #biblioteca base
import time 
import Page.Page_TabGen_R as Pg_R   #script da página de listagem da tabelas genéricas
import Controllers.listas as lst    #script de controle de listas por query sql
import Controllers.estSessaoMsg as statsMsg #script para o status de sessão e mensagens de sistema

#parametros da pagina ao mostrar no browser
st.set_page_config(page_title= 'Tabelas Genéricas', 
                layout= 'wide',
                initial_sidebar_state= 'collapsed')

#menssagem de sucesso/erro
if ('commandOk' in st.session_state) and ('statusMessage' in st.session_state):
    statsMsg.mostraMensagem()

#titulo da página
st.title('Tabelas Genéricas')

#variável com lista para servir de filtro para a tabela
lista = lst.listTabGer('tab_tab_ger')

#variável que recebe o valor selecionado da lista no formato dicionario
opcao = st.selectbox(label= 'Filtro de Tabelas Genéricas',
                    options= lista,
                    format_func= lambda record: f'{record["descricao"]}' 
                    )

#variavel quereceve o valor do campo 'valor' da tupla selecionada
filtro = opcao['valor'] 

#redireciona para o script de página de listagem da tabela
Pg_R.Reg_Tab_Gen_R(filtro)
