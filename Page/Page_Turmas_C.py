import streamlit as st
import Controllers.listas as lst
import Controllers.crudTurmas as ctb

@st.dialog('Turmas - Criação de Registros')
def insTurmas():
    
    id_grade = ''
    nom_cur = ''
    nom_dis = ''
    listaGrade = lst.listaGrades()
    grade = st.selectbox(label='Grade',
                           options= listaGrade,
                           format_func=lambda reg: reg['descricao'])
    id_grade = grade['id_grade']
    nom_cur = grade['nom_cur']
    nom_dis = grade['nom_dis']

    cap_max = st.number_input(label='Capacidade Máxima',
                              min_value=1,
                              max_value=500,
                              step=1,
                              format='%d')
    
    listaDiaSemana = lst.listTabGer('dia_sem')
    dia_sem = st.selectbox(label='Dia de Ocorrência',
                           options=listaDiaSemana,
                           format_func=lambda reg: reg['descricao'])
    dia_oco = dia_sem['valor']

    listaPeriodo = lst.listTabGer('per_tur')
    periodoSel = st.selectbox(label='Período',
                           options=listaPeriodo,
                           format_func=lambda reg: reg['descricao'])
    periodo = periodoSel['valor']

    listaProfessores = lst.listaProfessores()
    profSel = st.selectbox(label='Professor Responsável',
                           options=listaProfessores,
                            format_func=lambda reg: reg['nom_com'])
    prof_resp = profSel['reg_ins']
    
    situacao = st.toggle(label='Situação',
                    value=False,)
    if situacao:
        situacao = 'Ativo'
        st.write(situacao)
    else:
        situacao = 'Inativo'
        st.write(situacao)

    parametros = {'id_grade': id_grade,
                  'cap_max': cap_max,
                  'dia_oco': dia_oco,
                  'periodo': periodo,
                  'prof_resp': prof_resp,
                  'situacao': situacao,
                  'nom_cur': nom_cur,
                  'nom_dis': nom_dis}

    col1, col2, col3, col4, col5 = st.columns(5)
    with col5:
        insButton = st.button(label='Inserir',
                              width='stretch')
    
    if insButton:
        st.spinner()
        ctb.inserir(parametros)
        
