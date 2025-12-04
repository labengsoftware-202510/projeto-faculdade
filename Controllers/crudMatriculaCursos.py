import streamlit as st
import pandas as pd
import datetime as datetime
import Controllers.estSessaoMsg as statsMsg
from sqlalchemy import text 

def select(parametros):
    try:
        selectQuery = f"select mc.reg_ins,p.nom_com, mc.cod_cur, c.nom_cur, "
        selectQuery += f"mc.dat_inc, mc.dat_fin, mc.dat_max, mc.estado, mc.sit, mc.dip_env " 
        selectQuery += f"from matriculas_cursos mc, cursos c, pessoas p "
        selectQuery += f"where mc.reg_ins = p.reg_ins "
        selectQuery += f"and mc.cod_cur = c.cod_cur "
        if parametros['nom_com'] != '':
            selectQuery += f"and p.nom_com like '%{parametros['nom_com']}%'"
        selectQuery += f";" 

        conn = st.connection('mysql', type='sql')
        df = conn.query(selectQuery, 
                        ttl=600,
                        show_spinner='Processando...')
        df['dat_inc'] = pd.to_datetime(df['dat_inc'], format='%Y-%m-%d')
        df['data_inicio'] = df['dat_inc'].dt.strftime('%d/%m/%Y')
        df['dat_fin'] = pd.to_datetime(df['dat_fin'], format='%Y-%m-%d')
        df['data_final'] = df['dat_fin'].dt.strftime('%d/%m/%Y')
        df['dat_max'] = pd.to_datetime(df['dat_max'], format='%Y-%m-%d')
        df['data_max'] = df['dat_max'].dt.strftime('%d/%m/%Y')
        return [True, df]
    except Exception as e:
        statsMsg.operacaoErro(f'Erro: {e}')
        return [False,0]
        

def inserir(parametros):
    try:
        conn = st.connection('mysql', type='sql')
        with conn.session as session:
            insertCommand = f"insert into matriculas_cursos "
            insertCommand +=f"(reg_ins, cod_cur, dat_inc, dat_fin, dat_max, estado, sit, dip_env) "
            insertCommand += f"values (:reg_ins, :cod_cur, :dat_inc, :dat_fin, :dat_max, :estado, :sit, :dip_env);"
            session.execute(text(insertCommand), parametros)
            session.commit()
            statsMsg.operacaoSucesso(f'Matrícula {parametros['nom_com']} - {parametros['nom_cur']} incluida com sucesso!',)
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
            updateCommand = f"update matriculas_cursos "
            updateCommand += f"set dat_fin = :dat_fin,  estado = :estado, sit = :sit, dip_env = :dip_env "
            updateCommand += f"where reg_ins = :reg_ins "
            updateCommand += f"and cod_cur = :cod_cur "
            updateCommand += f"and DATE_FORMAT(dat_inc, '%Y-%m-%d') = ':dat_inc';"
            session.execute(text(updateCommand), parametros)
            session.commit()
            statsMsg.operacaoSucesso(f'Matrícula {parametros['nom_com']} - {parametros['nom_cur']} alterada com sucesso!')
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
            deleteCommand = f"delete from matriculas_cursos "
            deleteCommand += f"where reg_ins = :reg_ins "
            deleteCommand += f"and cod_cur = :cod_cur "
            deleteCommand += f"and DATE_FORMAT(dat_inc, '%Y-%m-%d') = ':dat_inc';"
            session.execute(text(deleteCommand), parametros)
            session.commit()
            statsMsg.operacaoSucesso(f'Registro {parametros['nom_cur']} - {parametros['nom_dis']} deletado com sucesso!') 
            st.cache_data.clear()
            st.rerun()
    except Exception as e:
        statsMsg.operacaoErro(f'Erro: {e}')
        st.cache_data.clear()
        st.rerun()
