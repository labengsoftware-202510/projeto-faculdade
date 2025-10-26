import streamlit as st
import Controllers.estSessaoMsg as statsMsg
from sqlalchemy import text 

def select(parametros = None):
    try:
        st.spinner()
        selectQuery = f"select *"
        selectQuery += f" from tab_ger"
        selectQuery += f" where dominio = '{parametros}';"
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
            insertCommand = f"insert into tab_ger (dominio, valor, descricao, obs) "
            insertCommand += f"values (:dominio, :valor, :descricao, :obs);"
            session.execute(text(insertCommand), parametros)
            session.commit()
            statsMsg.operacaoSucesso(f'Registro {parametros['valor']} - {parametros['descricao']} incluida com sucesso!')            
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
            updateCommand = f"update tab_ger "
            updateCommand += f"set descricao = :descricao,  obs = :obs "
            updateCommand += f"where dominio = :dominio and valor = :valor "
            session.execute(text(updateCommand), parametros)
            session.commit()
            statsMsg.operacaoSucesso(f'Registro {parametros['valor']} - {parametros['descricao']} alterada com sucesso!')            
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
            deleteCommand = f"delete from tab_ger "
            deleteCommand += f"where dominio = :dominio and valor = :valor"
            session.execute(text(deleteCommand), parametros)
            session.commit()
            statsMsg.operacaoSucesso(f'Registro {parametros['valor']} - {parametros['descricao']} deletado com sucesso!')            
            st.cache_data.clear()
            st.rerun()
    except Exception as e:
        statsMsg.operacaoErro(f'Erro: {e}')
        st.cache_data.clear()
        st.rerun()
