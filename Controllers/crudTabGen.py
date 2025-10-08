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
        ...

def inserir(parametros):
    try:
        conn = st.connection('mysql', type='sql')
        with conn.session as session:
            nReg = {'dominio': parametros[0], 'valor': parametros[1], 'descricao': parametros[2], 'obs': parametros[3]}
            insertCommand = f"insert into tab_ger (dominio, valor, descricao, obs) "
            insertCommand += f"values (:dominio, :valor, :descricao, :obs);"
            session.execute(text(insertCommand), nReg)
            session.commit()
            statsMsg.operacaoSucesso(f'Registro {parametros[1]} incluida com sucesso!')            
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
            nReg = {'dominio': parametros[0], 'valor': parametros[1], 'descricao': parametros[2], 'obs': parametros[3]}
            updateCommand = f"update tab_ger "
            updateCommand += f"set descricao = :descricao,  obs = :obs "
            updateCommand += f"where dominio = :dominio and valor = :valor "
            session.execute(text(updateCommand), nReg)
            session.commit()
            statsMsg.operacaoSucesso(f'Registro {parametros[1]} alterada com sucesso!')            
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
            nReg = {'dominio': parametros[0], 'valor': parametros[1]}
            deleteCommand = f"delete from tab_ger "
            deleteCommand += f"where dominio = :dominio and valor = :valor"
            session.execute(text(deleteCommand), nReg)
            session.commit()
            statsMsg.operacaoSucesso(f'Registro {parametros[1]} deletado com sucesso!')            
            st.cache_data.clear()
            st.rerun()
    except Exception as e:
        statsMsg.operacaoErro(f'Erro: {e}')
        st.cache_data.clear()
        st.rerun()
