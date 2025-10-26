import streamlit as st
import datetime
import Controllers.listas as lst
import Controllers.crudCursos as ctb

@st.dialog('Cursos - Criação de Registros')
def insCursos():

    nNomCur = st.text_input(label='Nome do Curso',
                                max_chars=30,
                                )
    
    escEstado = st.selectbox(label='Situação do Curso',
                            options=lst.listTabGer('sit_cur'),
                            placeholder='Insira a Cidade',
                            format_func=lambda x: x['descricao']
                            )
    nEstado = escEstado['valor']

    flagDestivado = False if nEstado == '1' else True
    if flagDestivado:
        st.session_state.tSit = False
    
    
    sit = ''
    nSit = st.toggle(label= 'Estado do Curso',
                        disabled=flagDestivado,
                        value=False,
                        key='tSit'
                        )

    if nSit:
        st.write('Ativo')
        sit = 'Ativo'
    else:
        st.write('Inativo')
        sit = 'Inativo'

    nDatInc = datetime.date.today()

    parametros = {'nom_cur': nNomCur,
                  'dat_inc': nDatInc,
                  'sit': sit,
                  'estado': nEstado}

    col1, col2, col3, col4, col5 = st.columns(5)
    with col5:
        insButton = st.button(label='Inserir',
                              width='stretch')
    
    if insButton:
        st.spinner()
        ctb.inserir(parametros)
        
