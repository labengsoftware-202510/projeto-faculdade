import streamlit as st
import datetime as datetime
import Controllers.crudMatriculaTurmas as ctb
import Controllers.colConfig as cc
import Controllers.estSessaoMsg as statsMsg #script para o status de sessão e mensagens de sistema
import Page.Page_Matriculas_Turmas_C as Pg_C
import Page.Page_Matriculas_Turmas_U as Pg_U
import Page.Page_Matriculas_Turmas_D as Pg_D

def mTurmasR(filtros):
    fDesativado = True
    tabela = ctb.select(filtros)
    selIndex = None

    #menssagem de sucesso/erro
    if ('commandOk' in st.session_state) and ('statusMessage' in st.session_state):
        statsMsg.mostraMensagem()

    

    col1, col2, col3, col4, col5 = st.columns(spec=5,
                                                gap=None,
                                                vertical_alignment='center')
    with col5:
        regButton = st.button(label='Registrar', 
                                key='insMatriculaTurma',
                                help='Click para Matrícular',
                                width='stretch')

    if tabela[0]:
        dtFrame = tabela[1]
        rowSel = st.dataframe(data=dtFrame,
                            height=150,
                            selection_mode='single-row',
                            on_select='rerun',
                            column_config=cc.colConfigMatriculaCursos())
        selRow = rowSel.selection.rows

        # select mt.reg_ins, p.nom_com, mt.cod_tur, c.nom_cur, d.nom_dis, mt.estado, mt.faltas, "
        # selectQuery += f"mt.nota1, mt.nota2, mt.nota3, mt.nota4, mt.media, mt.dat_ini, mt.dat_fin "
        
        if selRow:
            selIndex = {'reg_ins': dtFrame['reg_ins'].iloc[selRow].item(),
                        'nom_com': dtFrame['nom_com'].iloc[selRow].item(),
                        'cod_tur': dtFrame['cod_tur'].iloc[selRow].item(),
                        'nom_cur': dtFrame['nom_cur'].iloc[selRow].item(),
                        'nom_dis': dtFrame['nom_dis'].iloc[selRow].item(),
                        'estado': dtFrame['estado'].iloc[selRow].item(),
                        'faltas': dtFrame['faltas'].iloc[selRow].item(),
                        'nota1': dtFrame['nota1'].iloc[selRow].item(),
                        'nota2': dtFrame['nota2'].iloc[selRow].item(),
                        'nota3': dtFrame['nota3'].iloc[selRow].item(),
                        'nota4': dtFrame['nota4'].iloc[selRow].item(),
                        'media': dtFrame['media'].iloc[selRow].item(),
                        'dat_ini': dtFrame['dat_ini'].iloc[selRow].item(),
                        'dat_fin': dtFrame['dat_fin'].iloc[selRow].item(),
                        }
            fDesativado = False
        else:
            fDesativado = True
            
    else:
        st.error('Houve um Problema com a pesquisa')

    col13, col14, col15, col16, col17 = st.columns(spec=5,
                                                gap=None,
                                                vertical_alignment='center',
                                                )
        
    with col16:
        altButton = st.button(label='Alterar',
                                key='altMatriculaCurso',
                                help='Click aqui para Alteara a Matrícula',
                                width='stretch',
                                disabled=fDesativado,)
    
    with col17:
        delButton = st.button(label='Deletar',
                                key='delMatriculaCurso',
                                help='Click aqui para Deletar a Matrícula',
                                width='stretch',
                                disabled=fDesativado,)
    
    # if regButton:
    #     Pg_C.()
    # if altButton:
    #     Pg_U.(selIndex)
    # if delButton:
    #     Pg_D.(selIndex)