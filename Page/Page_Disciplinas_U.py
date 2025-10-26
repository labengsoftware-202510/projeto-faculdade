import streamlit as st
import Controllers.listas as lst
import Controllers.crudDisciplinas as ctb

@st.dialog('Cursos - Criação de Registros')
def altDisciplina(parametros):

    nCodDis = parametros['cod_dis']

    nNomDis = st.text_input(label='Nome da Disciplina',
                            max_chars=30,
                            value=parametros['nom_dis'],
                            )
    
    listaTipo = lst.listTabGer('tip_dis')
    tipoIndex = lst.buscaIndex(listaTipo, parametros['tipo'])
    nTipo = st.selectbox(label='Tipo da Disciplina',
                         options=listaTipo,
                         format_func=lambda x: x['descricao'],
                         index=tipoIndex,
                        )
    
    nCrgHorSemanal = st.number_input(label='Carga Horária Semanal',
                                    step=1,
                                    value=parametros['crg_hor_semanal'],
                                    )
    
    nCrgHorMinSemestral = st.number_input(label='Carga Horária Mínima Semestral',
                                    step=1,
                                    value=parametros['crg_hor_min_semestral'],
                                    )
    
    
    sit = ''
    flagDesativado = True if nCrgHorSemanal is None or nCrgHorMinSemestral is None else False
    if flagDesativado:
        st.session_state.nSitDiscplinas = False
    nSit = st.toggle(label= 'Estado do Curso',
                        value=False,
                        key='nSitDiscplinas',
                        disabled=flagDesativado,
                        )

    if nSit:
        st.write('Ativo')
        sit = 'Ativo'
    else:
        st.write('Inativo')
        sit = 'Inativo'

    parametros = {'cod_dis': nCodDis,
                  'nom_dis': nNomDis,
                  'tipo': nTipo['valor'],
                  'crg_hor_semanal': nCrgHorSemanal,
                  'crg_hor_min_semestral': nCrgHorMinSemestral,
                  'sit': sit}

    col1, col2, col3, col4, col5 = st.columns(5)
    with col5:
        altButton = st.button(label='Alterar',
                              width='stretch')
    
    if altButton:
        st.spinner()
        ctb.alterar(parametros)
        
