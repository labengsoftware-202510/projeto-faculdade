import streamlit as st

def colConfigTabGer():
    config = {
        'dominio': None,   
        'valor': st.column_config.Column(label='Valor',
                                         disabled=True,),
        'descricao': st.column_config.Column(label='Descrição',
                                         disabled=True,),
        'obs': st.column_config.Column(label='Observação',
                                         disabled=True,)
    }
    return config

def colConfigCep():
    config = {
        'cep':None,
        'cep_format': st.column_config.Column(label='CEP',
                                         disabled=True,),
        'logradouro': st.column_config.Column(label='Logradouro',
                                         disabled=True,),
        'bairro': st.column_config.Column(label='Bairro',
                                         disabled=True,),
        'cidade': st.column_config.Column(label='Cidade',
                                         disabled=True,),
        'estado': st.column_config.Column(label='Estado',
                                         disabled=True,)
    }
    return config

def colConfigCursos():
    config = {
        'cod_cur':None,
        'nom_cur': st.column_config.Column(label='Nome do Curso',
                                         disabled=True,),
        'dat_inc': st.column_config.Column(label='Data de Inclusão',
                                         disabled=True,),
        'sit': st.column_config.Column(label='Situação',
                                         disabled=True,),
        'estado': None,
        'est_desc': st.column_config.Column(label='Estado',
                                         disabled=True,)
    }
    return config

def colConfigDisciplina():
    config = {
        'cod_dis':None,
        'nom_dis': st.column_config.Column(label='Nome da Disciplina',
                                         disabled=True,),
        'dat_inc': st.column_config.Column(label='Data de Inclusão',
                                         disabled=True,),
        'tipo': None,
        'tipo_desc':st.column_config.Column(label='Tipo',
                                         disabled=True,),
        'crg_hor_semanal':st.column_config.Column(label='Carga Horária Semanal',
                                                  disabled=True,),
        'crg_hor_min_semestral': st.column_config.Column(label='Carga Horária minima Semestral',
                                                         disabled=True,),
        'sit': st.column_config.Column(label='Situação',
                                         disabled=True,),
        'estado': st.column_config.Column(label='Estado',
                                         disabled=True,)
    }
    return config

def colConfigPessoas():
    config = {
        'reg_ins':st.column_config.Column(label='Registro Institucional',
                                         disabled=True,),
        'categoria': None,
        'descricao': st.column_config.Column(label='Categoria',
                                         disabled=True,),
        'nom_com': st.column_config.Column(label='Nome Completo',
                                         disabled=True,),
        'cpf': None,
        'cpf_format': st.column_config.Column(label='CPF',
                                         disabled=True,),
        'dat_nas':None,
        'Data':st.column_config.Column(label='Data de Nascimento',
                                                  disabled=True,),
        'sit': st.column_config.Column(label='Situação',
                                         disabled=True,),
        'cep': None,
        'cep_format': None,
        'logradouro': None,
        'num': None,
        'comp': None,
        'bairro': None,
        'cidade': None,
        'estado': None,
    }
    return config

def colConfigGrade():
    config = {
        'id_grade':st.column_config.Column(label='Código da Grade',
                                         disabled=True,),
        'cod_cur': None,
        'nom_cur': st.column_config.Column(label='Curso',
                                         disabled=True,),
        'cod_dis': None,
        'nom_dis': st.column_config.Column(label='Disciplina',
                                         disabled=True,),
        'sem_ind': st.column_config.Column(label='Semestre Indicado',
                                         disabled=True,),
        'estado':st.column_config.Column(label='Estado',
                                         disabled=True,),
        'sit': st.column_config.Column(label='Situação',
                                         disabled=True,),
        'dat_ini':None,
        'data_inicio':st.column_config.Column(label='Data de Início',
                                              disabled=True,),
        'dat_fin':None,
        'data_final':st.column_config.Column(label='Data de Término',  
                                              disabled=True,),
        'id_grade_n':st.column_config.Column(label='Grade Substituta',
                                         disabled=True,),
        'id_grade_d':st.column_config.Column(label='Grade Dependente',
                                         disabled=True,)
    }
    return config

def colConfigTurmas():
    config = {
        'cod_tur':st.column_config.Column(label='Código da Turma',
                                         disabled=True,),
        'id_grade': None,
        'nom_cur': st.column_config.Column(label='Curso',
                                         disabled=True,),
        'nom_dis': st.column_config.Column(label='Disciplina',
                                         disabled=True,),
        'cap_max': st.column_config.Column(label='Capacidade Máxima',
                                         disabled=True,),
        'dia_oco': st.column_config.Column(label='Dia de Ocorrência',
                                         disabled=True,),
        'periodo': st.column_config.Column(label='Período',
                                         disabled=True,),
        'prof_resp': st.column_config.Column(label='Professor Responsável',
                                         disabled=True,),
        'sit': st.column_config.Column(label='Situação',
                                         disabled=True,),
    }
    return config