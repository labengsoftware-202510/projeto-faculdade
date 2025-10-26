import streamlit as st
import Controllers.estSessaoMsg as statsMsg
from sqlalchemy import text 

def select(parametros):
    try:
        selectQuery = f"select disc.cod_dis, disc.nom_dis, disc.dat_inc, disc.tipo, ger.descricao as tipo_desc, disc.crg_hor_semanal, disc.crg_hor_min_semestral, disc.sit"
        selectQuery += f" from disciplinas disc, tab_ger ger "
        selectQuery += f"where ger.dominio = 'tip_dis' "
        selectQuery += f"and ger.valor = disc.tipo "
        if (parametros is not None) or (parametros != ''):
            selectQuery += f"and nom_dis like '%{parametros}%'"
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
            insertCommand = f"insert into disciplinas (nom_dis, dat_inc, tipo, crg_hor_semanal, crg_hor_min_semestral, sit) "
            insertCommand += f"values (:nom_dis, :dat_inc, :tipo, :crg_hor_semanal, :crg_hor_min_semestral, :sit);"
            session.execute(text(insertCommand), parametros)
            session.commit()
            statsMsg.operacaoSucesso(f'Registro {parametros['nom_dis']} incluida com sucesso!') 
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
            updateCommand = f"update disciplinas "
            updateCommand += f"set nom_dis = :nom_dis, tipo = :tipo, crg_hor_semanal = :crg_hor_semanal, crg_hor_min_semestral = :crg_hor_min_semestral, sit = :sit "
            updateCommand += f"where cod_dis = :cod_dis;"
            session.execute(text(updateCommand), parametros)
            session.commit()
            statsMsg.operacaoSucesso(f'Registro {parametros['nom_dis']} alterada com sucesso!')
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
            deleteCommand = f"delete from disciplinas "
            deleteCommand += f"where cod_dis = :cod_dis;"
            session.execute(text(deleteCommand), parametros)
            session.commit()            
            statsMsg.operacaoSucesso(f'Registro {parametros['nom_dis']} deletado com sucesso!')            
            st.cache_data.clear()
            st.rerun()
    except Exception as e:
        statsMsg.operacaoErro(f'Erro: {e}')
        st.cache_data.clear()
        st.rerun()
