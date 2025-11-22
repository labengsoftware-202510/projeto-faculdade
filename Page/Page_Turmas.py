import streamlit as st #biblioteca base
import Controllers.listas as lst
import Page.Page_Turmas_R as Pg_R   #script da página de listagem da tabelas genéricas


#parametros da pagina ao mostrar no browser
st.set_page_config(page_title= 'Turmas', 
                layout= 'wide',
                initial_sidebar_state= 'collapsed')

#titulo da página
st.title('Turmas')

listaCurso = lst.listaCursos()
listaDisciplina = lst.listaDisciplinas()

col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    fCurso = st.selectbox(label='Cursos',
                            options= listaCurso,
                            format_func= lambda reg: reg['nom_cur']
                            )
    fCurso = fCurso['cod_cur']

with col2:
    fDisciplina = st.selectbox(label='Disciplinas',
                               options= listaDisciplina,
                               format_func= lambda reg: reg['nom_dis']
                                )
    fDisciplina = fDisciplina['cod_dis']

filtros = {'curso': fCurso,
           'disciplina': fDisciplina}

#redireciona para o script de página de listagem da tabela
Pg_R.turmasR(filtros)