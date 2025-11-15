import streamlit as st
import datetime
import Controllers.listas as lst
import Controllers.crudGrade as ctb

@st.dialog('Grade de Disciplina - Alteração de Registros')
def altGrade(parametrosAntigos):
    
    codCur = ''
    nomCur = ''
    listaCurso = lst.listaCursos()
    indexCurso = lst.buscaIndexCursos(listaCurso, parametrosAntigos['cod_cur'])
    nCodCur = st.selectbox(label='Curso',
                           options= listaCurso,
                           format_func=lambda reg: reg['nom_cur'],
                           index=indexCurso)
    codCur = nCodCur['cod_cur']
    nomCur = nCodCur['nom_cur']
        
    codDis = ''
    nomDis = ''
    listaDisciplina = lst.listaDisciplinas()
    indexDisciplina = lst.buscaIndexDisciplinas(listaDisciplina, parametrosAntigos['cod_dis'])
    nCodDis = st.selectbox(label='Disciplina',
                           options= listaDisciplina,
                           format_func=lambda reg: reg['nom_dis'],
                           index=indexDisciplina)
    codDis = nCodDis['cod_dis']
    nomDis = nCodDis['nom_dis']
    
    nSemInd = st.number_input(label='Semestre Indicado',
                              value=parametrosAntigos['sem_ind'],
                              min_value=1,
                              max_value=10,
                              step=1,
                              format='%d',)
    
    listaEstado = lst.listTabGer('est_gra_cur')
    indexEstado = lst.buscaIndex(listaEstado, parametrosAntigos['estado'])
    nEstado = st.selectbox(label='Estado da Grade',
                           options=listaEstado,
                           format_func=lambda reg: reg['descricao'],
                           index=indexEstado)
    estado = nEstado['valor']
    
    nGradeNova=''
    if codCur and estado == 'S':
        fGrade={'cod_cur': codCur}
        listaGradeSubstituta = lst.listaGradeSubstituta(fGrade)
        indexGSubstituta = lst.buscaIndexGradeSubstituta(listaGradeSubstituta, parametrosAntigos['id_grade_n'])
        nGradeNova = st.selectbox(label='Grade Substituta',
                                    options=listaGradeSubstituta,
                                    format_func=lambda reg: reg['descricao'],
                                    index=indexGSubstituta)
        nGradeNova = nGradeNova['id_grade']
    
    nGradeDepe = ''
    if codCur and (nSemInd > 1):
        fGrade={'cod_cur': str(codCur),
                'sem_ind': str(nSemInd)}
        listaGradeDependente = lst.listaGradeDependente(fGrade)
        indexGDependente = lst.buscaIndexGradeDependente(listaGradeDependente, parametrosAntigos['id_grade_d'])
        nGradeDepe = st.selectbox(label='Grade de Dependência',
                                    options=listaGradeDependente,
                                    format_func=lambda reg: reg['descricao'],
                                    index=indexGDependente)
        nGradeDepe = nGradeDepe['id_grade']

    nDatIni = st.date_input(label='Data de Inicio de Vigência',
                            min_value=datetime.date(1900,1,1),
                            value=parametrosAntigos['dat_ini'],)
    if not nDatIni and estado == 'C':
        nDatIni = datetime.date.today()
    
    nDatFin = st.date_input(label='Data de Final de Vigência',
                            min_value=datetime.date(1900,1,1),
                            value=parametrosAntigos['dat_fin'],)
    if not nDatFin and estado == 'C':
        nDatFin = datetime.date.today()
    
    sit = ''
    flagDesativado = True if (estado != 'U') else False
    if flagDesativado:
        st.session_state.nSitDiscplinas = False
    nSit = st.toggle(label= 'Estado do Curso',
                        value=True if parametrosAntigos['sit'] == 'Ativo' else False,
                        key='nSitDiscplinas',
                        disabled=flagDesativado,
                        )

    if nSit:
        st.write('Ativo')
        sit = 'Ativo'
    else:
        st.write('Inativo')
        sit = 'Inativo'

    parametros = {'id_grade':parametrosAntigos['id_grade'],
                  'cod_cur': codCur,
                  'cod_dis': codDis,
                  'sem_ind': nSemInd,
                  'estado': estado,
                  'sit': sit,
                  'dat_ini': nDatIni,
                  'dat_fin': nDatFin,
                  'id_grade_n': None if not nGradeNova else nGradeNova,
                  'id_grade_d': None if not nGradeDepe else nGradeDepe,
                  'nom_cur': nomCur,
                  'nom_dis': nomDis}

    col1, col2, col3, col4, col5 = st.columns(5)
    with col5:
        insButton = st.button(label='Alterar',
                              width='stretch')
    
    if insButton:
        st.spinner()
        ctb.alterar(parametros)
        
