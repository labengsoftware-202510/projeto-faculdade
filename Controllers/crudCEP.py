import streamlit as st
import Controllers.estSessaoMsg as statsMsg
from sqlalchemy import text 

def select(parametros):
    try:
        selectQuery = f"select cep, substr(cep, 1, 5)||'-'||substr(cep, 6, 3) as cep_format, logradouro, bairro, cidade, estado "
        selectQuery += f" from tab_cep "
        wherePart = ''
        for key in list(parametros.keys()):
            if key != 'cep':
                if parametros.get(key):
                    if wherePart:
                        wherePart += f"and {key} like '%{parametros.get(key)}%' "
                    else:
                        wherePart = f"where {key} like '%{parametros.get(key)}%' "
            else:
                if parametros.get(key):
                    if wherePart:
                        wherePart += f"and {key} = '{parametros.get(key)}' "
                    else:
                        wherePart = f"where {key} = '{parametros.get(key)}' "
        selectQuery += (wherePart +";")

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
            insertCommand = f"insert into tab_cep (logradouro, bairro, cidade, estado, cep) "
            insertCommand += f"values (:logradouro, :bairro, :cidade, :estado, :cep);"
            session.execute(text(insertCommand), parametros)
            session.commit()
            cepMsg = parametros['cep']
            cepFmt = f'{cepMsg[:5]}-{cepMsg[5:]}'
            statsMsg.operacaoSucesso(f'Registro {cepFmt} incluida com sucesso!') 
            st.cache_data.clear()
            st.rerun()
    except Exception as e:
        statsMsg.operacaoErro(f'Erro: {e}')
        st.cache_data.clear()
        st.rerun()

def alterar(parametros):
    try:
        conn = st.connection('mysql', type='sql')
        keys = list(parametros[0].keys())
        with conn.session as session:
            updateCommand = f"update tab_cep "
            updateCommand += f"set {keys[1]} = :logradouro,  {keys[2]} = :bairro, {keys[3]} = :cidade, {keys[4]} = :estado "
            updateCommand += f"where {keys[0]} = :cep;"
            session.execute(text(updateCommand), parametros)
            session.commit()
            cepMsg = parametros['cep']
            cepFmt = f'{cepMsg[:5]}-{cepMsg[5:]}'
            statsMsg.operacaoSucesso(f'Registro {cepFmt} alterada com sucesso!')
            st.cache_data.clear()
            st.rerun()
    except Exception as e:
        statsMsg.operacaoErro(f'Erro: {e}')
        st.cache_data.clear()
        st.rerun()

def excluir(parametros):
    try:
        conn = st.connection('mysql', type='sql')
        keys = list(parametros[0].keys())
        with conn.session as session:
            deleteCommand = f"delete from tab_cep "
            deleteCommand += f"where {keys[0]} = :cep;"
            session.execute(text(deleteCommand), parametros)
            session.commit()            
            cepMsg = parametros['cep']
            cepFmt = f'{cepMsg[:5]}-{cepMsg[5:]}'
            statsMsg.operacaoSucesso(f'Registro {cepFmt} deletado com sucesso!')            
            st.cache_data.clear()
            st.rerun()
    except Exception as e:
        statsMsg.operacaoErro(f'Erro: {e}')
        st.cache_data.clear()
        st.rerun()
