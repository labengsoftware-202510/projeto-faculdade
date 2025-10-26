import streamlit as st
import Controllers.listas as lst
import Controllers.crudCursos as ctb

@st.dialog('Cursos - Criação de Registros')
def altCursos(parametros):
    
    nNomCur = st.text_input(label='Nome do Curso',
                            max_chars=30,
                            value=parametros['nom_cur'],
                            )
    
    lista = lst.listTabGer('sit_cur')
    sitCurIndex = lst.buscaIndex(lista, parametros['sit'])
    escEstado = st.selectbox(label='Situação do Curso',
                        options=lista,
                        placeholder='Insira a Cidade',
                        format_func=lambda x: x['descricao'],
                        index=sitCurIndex,
                        ) 
    nEstado = escEstado['valor']

    flagDestivado = False if nEstado == '1' else True
    if flagDestivado:
        st.session_state.tSit = False
    
    sit = ''
    nSit = st.toggle(label= 'Estado do Curso',
                        disabled=flagDestivado,
                        value=(parametros['estado'] == 'Ativo'),
                        key='tSit',
                        )
    if nSit:
        st.write('Ativo')
        sit = 'Ativo'
    else:
        st.write('Inativo')
        sit = 'Inativo'

    parametros = {'cod_cur': parametros['cod_cur'],
                  'nom_cur': nNomCur,
                  'sit': sit,
                  'estado': nEstado}

    col1, col2, col3, col4, col5 = st.columns(5)
    with col5:
        altButton = st.button(label='Alterar',
                              width='stretch')
    
    if altButton:
        st.spinner()
        ctb.alterar(parametros)
        
