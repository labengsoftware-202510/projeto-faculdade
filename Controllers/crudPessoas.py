import streamlit as st
import pandas as pd
import datetime as datetime
import Controllers.estSessaoMsg as statsMsg
from sqlalchemy import text 

def select(parametros):
    try:
        st.spinner()
        selectQuery = f"select pes.reg_ins, pes.categoria, ger.descricao, pes.nom_com, pes.cpf, "
        selectQuery += f"concat(substr(lpad(pes.cpf,11,0),1,3),'.',substr(lpad(pes.cpf,11,0),4,3),'.',substr(lpad(pes.cpf,11,0),7,3),'-',substr(lpad(pes.cpf,11,0),10,2)) as cpf_format, "
        selectQuery += f"pes.dat_nas, pes.sit, pes.cep, "
        selectQuery += f"concat(substr(lpad(pes.cep,8,'0'), 1, 5),'-',substr(lpad(pes.cep,8,'0'), 6, 3)) as cep_format, "
        selectQuery += f"cep.logradouro, pes.num, pes.comp, cep.bairro, cep.cidade, cep.estado "
        selectQuery += f"from pessoas pes, tab_cep cep, tab_ger ger "
        selectQuery += f"where pes.cep = cep.cep "
        selectQuery += f"and ger.dominio = 'crg_pes' "
        selectQuery += f"and pes.categoria = ger.valor "
        if parametros:
            if parametros['fNome']:
                selectQuery += f"and pes.nom_com like '%{parametros['fNome']}%' "
            if parametros['fCategoria']:
                selectQuery += f"and pes.nom_com like '%{parametros['fCategoria']}%' "
        selectQuery += f";"
        conn = st.connection('mysql', type='sql')
        df = conn.query(selectQuery, 
                        ttl=600,
                        show_spinner='Processando...')
        df['dat_nas'] = pd.to_datetime(df['dat_nas'], format='%Y-%m-%d')
        df['Data'] = df['dat_nas'].dt.strftime('%d/%m/%Y')
        return [True, df]
    except Exception as e:
        return [False,e]

def inserir(parametros):
    try:
        conn = st.connection('mysql', type='sql')
        with conn.session as session:            
            insertCommand = f"insert into pessoas (nom_com, cpf, dat_nas, cep, num, comp, sit, categoria) "
            insertCommand += f"values (:nom_com, :cpf, :dat_nas, :cep, :num, :comp, :sit, :categoria);"
            session.execute(text(insertCommand), parametros)
            session.commit()
            statsMsg.operacaoSucesso(f"{parametros['nom_com']} Incluido com Sucesso!")            
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
            updateCommand = f"update pessoas "
            updateCommand += f"set nom_com = :nom_com, cpf = :cpf, dat_nas = :dat_nas, cep = :cep, "
            updateCommand += f"num = :num, comp = :comp, sit = :sit, categoria = :categoria "
            updateCommand += f"where reg_ins = :reg_ins;"
            session.execute(text(updateCommand), parametros)
            session.commit()
            statsMsg.operacaoSucesso(f'Registro {parametros['nom_com']} alterada com sucesso!')            
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
            deleteCommand = f"delete from pessoas "
            deleteCommand += f"where reg_ins = :reg_ins;"
            session.execute(text(deleteCommand), parametros)
            session.commit()
            statsMsg.operacaoSucesso(f'Registro {parametros['nom_com']} deletado com sucesso!')            
            st.cache_data.clear()
            st.rerun()
    except Exception as e:
        statsMsg.operacaoErro(f'Erro: {e}')
        st.cache_data.clear()
        st.rerun()
