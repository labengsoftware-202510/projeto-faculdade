import streamlit as st
import pandas as pd
import datetime as datetime
import Controllers.estSessaoMsg as statsMsg
from sqlalchemy import text 

def select(parametros):
    try:
        selectQuery = f"select mt.reg_ins, p.nom_com, mt.cod_tur, c.nom_cur, d.nom_dis, mt.estado, mt.faltas, "
        selectQuery += f"mt.nota1, mt.nota2, mt.nota3, mt.nota4, mt.media, mt.dat_ini, mt.dat_fin "
        selectQuery += f"from matriculas_turmas mt,  pessoas p, turmas t, grade gd, cursos c, disciplinas d "
        selectQuery += f"where mt.cod_tur = t.cod_tur "
        selectQuery += f"and t.id_grade = gd.id_grade "
        selectQuery += f"and gd.cod_cur = c.cod_cur "
        selectQuery += f"and gd.cod_dis = d.cod_dis "
        if parametros['nom_com'] != '':
            selectQuery += f"and p.nom_com like '%{parametros['nom_com']}%'"
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
            insertCommand = f"insert into matriculas_turmas "
            insertCommand +=f"(reg_ins, cod_tur, estado, faltas, nota1, nota2, nota3, nota4, media, dat_ini, dat_fin) "
            insertCommand += f"values (:reg_ins, :cod_tur, :estado, :faltas, :nota1, :nota2, :nota3, :nota4, :media, :dat_ini, :dat_fin);"
            session.execute(text(insertCommand), parametros)
            session.commit()
            statsMsg.operacaoSucesso(f'Matrícula {parametros['nom_com']} - {parametros['nom_cur']} / {parametros['nom_dis']} feita com sucesso!',)
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
            updateCommand = f"update matriculas_turmas "
            updateCommand += f"set estado = :estado,  faltas = :faltas, nota1 = :nota1, nota2 = :nota2, nota3 = :nota3, nota4 = :nota4, media = :media, dat_fin = :dat_fin "
            updateCommand += f"where reg_ins = :reg_ins "
            updateCommand += f"and cod_tur = :cod_tur "
            updateCommand += f"and DATE_FORMAT(dat_ini, '%Y-%m-%d') = ':dat_ini';"
            session.execute(text(updateCommand), parametros)
            session.commit()
            statsMsg.operacaoSucesso(f'Matrícula {parametros['nom_com']} - {parametros['nom_cur']} / {parametros['nom_dis']} alterada com sucesso!')
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
            deleteCommand = f"delete from matriculas_turmas "
            deleteCommand += f"where reg_ins = :reg_ins "
            deleteCommand += f"and cod_tur = :cod_tur "
            deleteCommand += f"and DATE_FORMAT(dat_ini, '%Y-%m-%d') = ':dat_ini';"
            session.execute(text(deleteCommand), parametros)
            session.commit()
            statsMsg.operacaoSucesso(f'Registro {parametros['nom_com']} - {parametros['nom_cur']} / {parametros['nom_dis']} deletado com sucesso!') 
            st.cache_data.clear()
            st.rerun()
    except Exception as e:
        statsMsg.operacaoErro(f'Erro: {e}')
        st.cache_data.clear()
        st.rerun()
