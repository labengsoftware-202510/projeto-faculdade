import streamlit as st #biblioteca base
import Page.Page_CEP_R as Pg_R   #script da página de listagem da tabelas genéricas
import Controllers.listas as lst    #script de controle de listas por query sql
import Controllers.estSessaoMsg as statsMsg #script para o status de sessão e mensagens de sistema

#parametros da pagina ao mostrar no browser
st.set_page_config(page_title= 'Pessoas', 
                layout= 'wide',
                initial_sidebar_state= 'collapsed')

#menssagem de sucesso/erro
if ('commandOk' in st.session_state) and ('statusMessage' in st.session_state):
    statsMsg.mostraMensagem()

#titulo da página
st.title('CEP')

#variável com lista para servir de filtro para a tabela
# col1, col2, col3, col4, col5 = st.columns(spec=5,
#                                           gap=None,
#                                           vertical_alignment='center')
# with col1:
#     filtroNome = st.text_input()
#     listaNomes = lst.listPessoas(filtroNome)

# #variável que recebe o valor selecionado da lista no formato dicionario
# opcao = st.selectbox(label= 'Filtro de Tabelas Genéricas',
#                     options= lista,
#                     format_func= lambda record: f'{record["descricao"]}' 
#                     )

# #variavel quereceve o valor do campo 'valor' da tupla selecionada
# filtro = opcao['valor'] 

# #redireciona para o script de página de listagem da tabela
# Pg_R.Reg_Tab_Gen_R(filtro)
