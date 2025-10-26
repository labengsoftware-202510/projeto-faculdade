import streamlit as st
import Controllers.listas as lst
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
        if parametros['fNome']:
              selectQuery += f"and pes.nom_com like '%{parametros['fNome']}%' "
        if parametros['fCategoria']:
              selectQuery += f"and pes.nom_com like '%{parametros['fCategoria']}%' "
        selectQuery += f";"
        conn = st.connection('mysql', type='sql')
        df = conn.query(selectQuery, 
                        ttl=600,
                        show_spinner='Processando...')
        return [True, df]
    except:
        return [False,0]

def inserir(parametros):
    try:
        cepFor = parametros['cep']
        conn = st.connection('mysql', type='sql')
        with conn.session as session:
            lista = lst.listaCep()
            if lst.buscaCep(lista,parametros['cep']):
                insertCep = f"insert into tab_cep (cep, logradouro, bairro, cidade, estado) "
                insertCep += f"values (:cep, :logradouro, :bairro, :cidade, :estado)"
                session.execute(text(insertCommand), parametros)
                session.commit()
                msgCEP = f"CEP {cepFor[:5]}-{cepFor[5:]} {parametros['logradouro']} Incluido com Sucesso! "
            
            insertCommand = f"insert into pessoa (nom_com, cpf, dat_nas, cep, num, comp, sit, categoria) "
            insertCommand += f"values (:nom_com, :cpf, :dat_nas, :cep, :num, :comp, :sit, :categoria);"
            session.execute(text(insertCommand), parametros)
            session.commit()
            
            msgPess = f"{parametros['reg_ins']} - {parametros['nom_com']} Incluido com Sucesso! /n "
            msgSucess = msgPess + msgCEP
            statsMsg.operacaoSucesso(msgSucess)            
            st.cache_data.clear()
            st.rerun()
    except Exception as e:
        statsMsg.operacaoErro(f'Erro: {e}')
        st.cache_data.clear()
        st.rerun()

def alterar(parametros):
    # try:
    #     conn = st.connection('mysql', type='sql')
    #     with conn.session as session:
    #         nReg = {'dominio': parametros[0], 'valor': parametros[1], 'descricao': parametros[2], 'obs': parametros[3]}
    #         updateCommand = f"update tab_ger "
    #         updateCommand += f"set descricao = :descricao,  obs = :obs "
    #         updateCommand += f"where dominio = :dominio and valor = :valor "
    #         session.execute(text(updateCommand), nReg)
    #         session.commit()
    #         statsMsg.operacaoSucesso(f'Registro {parametros[1]} alterada com sucesso!')            
    #         st.cache_data.clear()
    #         st.rerun()
    # except Exception as e:
    #     statsMsg.operacaoErro(f'Erro: {e}')
    #     st.cache_data.clear()
    #     st.rerun()
        ...

def excluir(parametros):
    # try:
    #     conn = st.connection('mysql', type='sql')
    #     with conn.session as session:
    #         nReg = {'dominio': parametros[0], 'valor': parametros[1]}
    #         deleteCommand = f"delete from tab_ger "
    #         deleteCommand += f"where dominio = :dominio and valor = :valor"
    #         session.execute(text(deleteCommand), nReg)
    #         session.commit()
    #         statsMsg.operacaoSucesso(f'Registro {parametros[1]} deletado com sucesso!')            
    #         st.cache_data.clear()
    #         st.rerun()
    # except Exception as e:
    #     statsMsg.operacaoErro(f'Erro: {e}')
    #     st.cache_data.clear()
    #     st.rerun()
        ...
