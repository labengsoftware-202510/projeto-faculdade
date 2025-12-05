import streamlit as st
import Controllers.estSessaoMsg as statsMsg
from sqlalchemy import text 

def selectAlunoXCurso():
    try:
        selectQuery =  f"select c.nom_cur, count(mc.reg_ins) as qtd "
        selectQuery += f"from matriculas_cursos mc, cursos c "
        selectQuery += f"where mc.cod_cur = c.cod_cur "
        selectQuery += f"group by c.nom_cur"
        
        conn = st.connection('mysql', type='sql')
        df = conn.query(selectQuery, 
                        ttl=600,
                        show_spinner='Processando...')
        return [True, df]
    except:
        return [False,0]

def selectAlunoXTurmas():
    try:
        selectQuery =  f"select d.nom_dis, count(mt.reg_ins) as qtd "
        selectQuery += f"from matriculas_turmas mt, turmas t, grade g, disciplinas d "
        selectQuery += f"where mt.cod_tur = t.cod_tur "
        selectQuery += f"and t.id_grade = g.id_grade "
        selectQuery += f"and g.cod_dis = d.cod_dis "
        selectQuery += f"group by d.nom_dis "
        
        conn = st.connection('mysql', type='sql')
        df = conn.query(selectQuery, 
                        ttl=600,
                        show_spinner='Processando...')
        return [True, df]
    except:
        return [False,0]