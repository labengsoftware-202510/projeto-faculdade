import streamlit as st
import pandas as pd
import datetime as datetime
import Controllers.estSessaoMsg as statsMsg
from sqlalchemy import text 

def select(parametros):
    try:
        selectQuery = f"select g.id_grade, g.cod_cur, c.nom_cur, g.cod_dis, d.nom_dis, "
        selectQuery += f"g.sem_ind, g.estado, g.sit, g.dat_ini, g.dat_fin, "
        selectQuery += f"g.id_grade_n, g.id_grade_d "
        selectQuery += f"from grade g, cursos c, disciplinas d "
        selectQuery += f"where g.cod_cur = c.cod_cur "
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
        df['dat_ini'] = pd.to_datetime(df['dat_ini'], format='%Y-%m-%d')
        df['data_inicio'] = df['dat_ini'].dt.strftime('%d/%m/%Y')
        df['dat_fin'] = pd.to_datetime(df['dat_fin'], format='%Y-%m-%d')
        df['data_final'] = df['dat_fin'].dt.strftime('%d/%m/%Y')
        return [True, df]
    except Exception as e:
        statsMsg.operacaoErro(f'Erro: {e}')
        return [False,0]
        

def inserir(parametros):
    try:
        conn = st.connection('mysql', type='sql')
        with conn.session as session:
            insertCommand = f"insert into grade (cod_cur, cod_dis, sem_ind, estado, sit, dat_ini, dat_fin, id_grade_n, id_grade_d) "
            insertCommand += f"values (:cod_cur, :cod_dis, :sem_ind, :estado, :sit, :dat_ini, :dat_fin, :id_grade_n, :id_grade_d);"
            session.execute(text(insertCommand), parametros)
            session.commit()
            statsMsg.operacaoSucesso(f'Registro {parametros['nomCur']} - {parametros['nomDis']} incluida com sucesso!',)
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
            updateCommand = f"update grade "
            updateCommand += f"set cod_cur = :cod_cur,  cod_dis = :cod_dis, sem_ind = :sem_ind, estado = :estado, sit = :sit, "
            updateCommand += f"dat_ini = :dat_ini, dat_fin = :dat_fin, id_grade_n = :id_grade_n, id_grade_d = :id_grade_d "
            updateCommand += f"where id_grade = :id_grade;"
            session.execute(text(updateCommand), parametros)
            session.commit()
            statsMsg.operacaoSucesso(f'Registro {parametros['nom_cur']} - {parametros['nom_dis']} alterada com sucesso!')
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
            deleteCommand = f"delete from grade "
            deleteCommand += f"where id_grade = :id_grade;"
            session.execute(text(deleteCommand), parametros)
            session.commit()
            statsMsg.operacaoSucesso(f'Registro {parametros['nom_cur']} - {parametros['nom_dis']} deletado com sucesso!') 
            st.cache_data.clear()
            st.rerun()
    except Exception as e:
        statsMsg.operacaoErro(f'Erro: {e}')
        st.cache_data.clear()
        st.rerun()
