import streamlit as st
import datetime
import Controllers.listas as lst
import Controllers.crudDisciplinas as ctb

@st.dialog('Matérias - Criação de Registros')
def insDisciplina():

    nNomDis = st.text_input(label='Nome da Disciplina',
                                max_chars=30,
                                )
    
    listaTipo = lst.listTabGer('tip_dis')
    selectTipo = st.selectbox(label='Tipo da Disciplina',
                         options=listaTipo,
                         format_func=lambda x: x['descricao'],
                        )
    nTipo = selectTipo['valor']
    
    nCrgHorSemanal = st.number_input(label='Carga Horária Semanal',
                                    step=1,
                                    )
    
    nCrgHorMinSemestral = st.number_input(label='Carga Horária Mínima Semestral',
                                    step=1,
                                    )
    
    sit = ''
    flagDesativado = True if (nCrgHorSemanal == 0 or nCrgHorMinSemestral == 0) else False
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

    nDatInc = datetime.date.today()

    parametros = {'nom_dis': nNomDis,
                  'tipo': nTipo,
                  'crg_hor_semanal': nCrgHorSemanal,
                  'crg_hor_min_semestral': nCrgHorMinSemestral,
                  'dat_inc': nDatInc,
                  'sit': sit}

    col1, col2, col3, col4, col5 = st.columns(5)
    with col5:
        insButton = st.button(label='Inserir',
                              width='stretch')
    
    if insButton:
        st.spinner()
        ctb.inserir(parametros)
        
