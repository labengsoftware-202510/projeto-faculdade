import streamlit as st
import Controllers.estSessaoMsg as statsMsg
from sqlalchemy import text 

def select(parametros):
    try:
        selectQuery = f"select cursos.cod_cur, cursos.nom_cur, cursos.dat_inc, cursos.sit, tab_ger.descricao as sit_desc, cursos.estado "
        selectQuery += f" from cursos, tab_ger "
        selectQuery += f" where cursos.sit = tab_ger.valor and tab_ger.dominio = 'sit_cur' "
        if (parametros is not None) or (parametros != ''):
            selectQuery += f"and nom_cur like '%{parametros}%'"
        selectQuery += ";"

        conn = st.connection('mysql', type='sql')
        df = conn.query(selectQuery, 
                        ttl=600,
                        show_spinner='Processando...')
        return [True, df]
    except:
        return [False,0]
        

def inserir(parametros):
    try:
        conn = st.connection('mysql', type='sql')
        with conn.session as session:
            insertCommand = f"insert into cursos (nom_cur, dat_inc, sit, estado) "
            insertCommand += f"values (:nom_cur, :dat_inc, :sit, :estado);"
            session.execute(text(insertCommand), parametros)
            session.commit()
            statsMsg.operacaoSucesso(f'Registro {parametros['nom_cur']} incluida com sucesso!') 
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
            updateCommand = f"update cursos "
            updateCommand += f"set nom_cur = :nom_cur, sit = :sit, estado = :estado "
            updateCommand += f"where cod_cur = :cod_cur;"
            session.execute(text(updateCommand), parametros)
            session.commit()
            statsMsg.operacaoSucesso(f'Registro {parametros['nom_cur']} alterada com sucesso!')
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
            deleteCommand = f"delete from cursos "
            deleteCommand += f"where cod_cur = :cod_cur;"
            session.execute(text(deleteCommand), parametros)
            session.commit()            
            statsMsg.operacaoSucesso(f'Registro {parametros['nom_cur']} deletado com sucesso!')            
            st.cache_data.clear()
            st.rerun()
    except Exception as e:
        statsMsg.operacaoErro(f'Erro: {e}')
        st.cache_data.clear()
        st.rerun()
