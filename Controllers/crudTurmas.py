import streamlit as st
import pandas as pd
import datetime as datetime
import Controllers.estSessaoMsg as statsMsg
from sqlalchemy import text 

def select(parametros):
    try:
        selectQuery = f"select t.cod_tur, t.id_grade, c.nom_cur, d.nom_dis,"
        selectQuery += f"t.cap_max, t.dia_oco, t.periodo, t.prof_resp, t.sit "
        selectQuery += f"from turmas t, grade g, cursos c, disciplinas d "
        selectQuery += f"where t.id_grade = g.id_grade "
        selectQuery += f"and g.cod_cur = c.cod_cur "
        selectQuery += f"and g.cod_dis = d.cod_dis "
        if parametros['curso'] != '':
            selectQuery += f"and g.cod_cur = {parametros['curso']}"
        if parametros['disciplina'] != '':
            selectQuery += f"and g.cod_dis = {parametros['disciplina']}"
        selectQuery += f";"

        conn = st.connection('mysql', type='sql')
        df = conn.query(selectQuery, 
                        ttl=600,
                        show_spinner='Processando...')
        return [True, df]
    except Exception as e:
        statsMsg.operacaoErro(f'Erro: {e}')
        return [False,0]
        

def inserir(parametros):
    try:
        conn = st.connection('mysql', type='sql')
        with conn.session as session:
            insertCommand = f"insert into turmas (id_grade, cap_max, dia_oco, periodo, prof_resp, sit) "
            insertCommand += f"values (:id_grade, :cap_max, :dia_oco, :periodo, :prof_resp, :sit);"
            session.execute(text(insertCommand), parametros)
            session.commit()
            statsMsg.operacaoSucesso(f'Registro de Turma para {parametros['nom_cur']} - {parametros['nom_dis']} incluida com sucesso!')
            st.cache_data.clear()
            st.rerun()
    except Exception as e:
        statsMsg.operacaoErro(f'Erro: {e}')
        st.cache_data.clear()
        st.rerun()

def alterar(parametros):
    try:
        conn = st.connection('mysql', type='sql')
        with conn.session as session:
            updateCommand = f"update turmas "
            updateCommand += f"set id_grade = :id_grade, cap_max = :cap_max, dia_oco = :dia_oco, periodo = :periodo, "
            updateCommand += f"prof_resp = :prof_resp, sit = :sit "
            updateCommand += f"where cod_tur = :cod_tur;"
            session.execute(text(updateCommand), parametros)
            session.commit()
            statsMsg.operacaoSucesso(f'Registro de Turma {parametros['nom_cur']} - {parametros['nom_dis']} alterada com sucesso!')
            st.cache_data.clear()
            st.rerun()
    except Exception as e:
        statsMsg.operacaoErro(f'Erro: {e}')
        st.cache_data.clear()
        st.rerun()

def excluir(parametros):
    try:
        conn = st.connection('mysql', type='sql')
        with conn.session as session:
            deleteCommand = f"delete from trumas "
            deleteCommand += f"where cod_tur = :cod_tur;"
            session.execute(text(deleteCommand), parametros)
            session.commit()
            statsMsg.operacaoSucesso(f'Registro da turma {parametros['nom_cur']} - {parametros['nom_dis']} deletado com sucesso!') 
            st.cache_data.clear()
            st.rerun()
    except Exception as e:
        statsMsg.operacaoErro(f'Erro: {e}')
        st.cache_data.clear()
        st.rerun()
