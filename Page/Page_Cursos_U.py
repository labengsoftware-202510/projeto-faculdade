import streamlit as st
import Controllers.listas as lst
import Controllers.crudCursos as ctb

@st.dialog('Cursos - Criação de Registros')
def altCursos(parametros):
    est = ''
    lista = lst.listTabGer('sit_cur')

    nNomCur = st.text_input(label='Nome do Curso',
                            max_chars=30,
                            value=parametros['nom_cur'],
                            )
    
    sitCurIndex = lst.buscaIndex(lista, parametros['sit'])
    escSit = st.selectbox(label='Situação do Curso',
                        options=lista,
                        placeholder='Insira a Cidade',
                        format_func=lambda x: x['descricao'],
                        index=sitCurIndex,
                        ) 
    nSit = escSit['valor']

    flagDestivado = False if nSit == '1' else True
    if flagDestivado:
        st.session_state.tEst = False
    
    nEstado = st.toggle(label= 'Estado do Curso',
                        disabled=flagDestivado,
                        value=(parametros['estado'] == 'Ativo'),
                        key='tEst',
                        )
    if nEstado:
        st.write('Ativo')
        est = 'Ativo'
    else:
        st.write('Inativo')
        est = 'Inativo'

    parametros = {'cod_cur': parametros['cod_cur'],
                  'nom_cur': nNomCur,
                  'sit': nSit,
                  'estado': est}

    col1, col2, col3, col4, col5 = st.columns(5)
    with col5:
        altButton = st.button(label='Alterar',
                              width='stretch')
    
    if altButton:
        st.spinner()
        ctb.alterar(parametros)
        
