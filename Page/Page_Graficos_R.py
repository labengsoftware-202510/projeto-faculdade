import streamlit as st
import Controllers.estSessaoMsg as statsMsg
import Controllers.chartRead as chartRead
from sqlalchemy import text 

def graficos(filtro):
    if filtro['grafico'] == 1:
        st.bar_chart(data=chartRead.selectAlunoXCurso()[1],
                    x='nom_cur',
                    y='qtd',
                    x_label='Cursos',
                    y_label='Quantidade de Alunos',
                    height=400,
                    width=700,
                    stack='layered'
                    )
    elif filtro['grafico'] == 2:
        st.line_chart(data=chartRead.selectAlunoXTurmas()[1],
                    x='nom_dis',
                    y='qtd',
                    x_label='Disciplinas',
                    y_label='Quantidade de Alunos',
                    height=400,
                    width=700,
                    )