import streamlit as st
import Controllers.crudPessoas as ctb
import Controllers.colConfig as cc
import Controllers.estSessaoMsg as statsMsg #script para o status de sessão e mensagens de sistema
# import Page.Page_Disciplinas_C as Pg_C
# import Page.Page_Disciplinas_U as Pg_U
# import Page.Page_Disciplinas_D as Pg_D

def pessoasR(filtros):
    selIndex = None
    fDesativado = True

    #menssagem de sucesso/erro
    if ('commandOk' in st.session_state) and ('statusMessage' in st.session_state):
        statsMsg.mostraMensagem()

    tabela = ctb.select(filtros)

    col1, col2, col3, col4, col5 = st.columns(spec=5,
                                                gap=None,
                                                vertical_alignment='center')
    with col5:
        regButton = st.button(label='Registrar', 
                                key='insPessoas',
                                help='Click aqui para Inserir um novo Curso',
                                width='stretch')

    if tabela[0]:
        dtFrame = tabela[1]
        rowSel = st.dataframe(data=dtFrame,
                            height=150,
                            selection_mode='single-row',
                            on_select='rerun',
                            column_config=cc.colConfigDisciplina())
        selRow = rowSel.selection.rows
        if selRow:
            selIndex = {'reg_ins': dtFrame['reg_ins'].iloc[selRow].item(),
                        'categoria': dtFrame['categoria'].iloc[selRow].item(),
                        'nom_com': dtFrame['nom_com'].iloc[selRow].item(),
                        'cpf': dtFrame['cpf'].iloc[selRow].item(),
                        'dat_nas': dtFrame['dat_nas'].iloc[selRow].item(),
                        'sit': dtFrame['sit'].iloc[selRow].item(),                        
                        'cep': dtFrame['cep'].iloc[selRow].item(),
                        'num': dtFrame['num'].iloc[selRow].item(),
                        'comp': dtFrame['comp'].iloc[selRow].item()}
            fDesativado = False
        else:
            fDesativado = True

        with st.container(gap=None,):
            col6, col7, col8, col9 = st.columns(spec=[1,3,1,3],
                                                gap=None,
                                                vertical_alignment='center',
                                                )
            with col6:
                st.text_input(label='CEP',
                            disabled=True,
                            value=dtFrame['cep_format'].iloc[selRow].item(),
                            width='stretch',)
            with col7:
                st.text_input(label='Logradouro',
                            disabled=True,
                            value=dtFrame['logradouro'].iloc[selRow].item(),
                            width='stretch',)
            with col8:
                st.text_input(label='Numero',
                            disabled=True,
                            value=dtFrame['num'].iloc[selRow].item(),
                            width='stretch',)
            with col9:
                st.text_input(label='Complemento',
                            disabled=True,
                            value=dtFrame['comp'].iloc[selRow].item(),
                            width='stretch',)
                
        with st.container(gap=None,):
            col10, col11, col12 = st.columns(spec=3,
                                            gap=None,
                                            vertical_alignment='center',
                                            )
            with col10:
                st.text_input(label='Bairro',
                            disabled=True,
                            value=dtFrame['bairro'].iloc[selRow].item(),
                            width='stretch',)
            with col11:
                st.text_input(label='Cidade',
                            disabled=True,
                            value=dtFrame['cidade'].iloc[selRow].item(),
                            width='stretch',)
            with col12:
                st.text_input(label='Estado',
                            disabled=True,
                            value=dtFrame['estado'].iloc[selRow].item(),
                            width='stretch',)
        

        col13, col14, col15, col16, col17 = st.columns(spec=5,
                                                gap=None,
                                                vertical_alignment='center',
                                                )
        
        with col16:
            altButton = st.button(label='Alterar',
                                    key='altDisciplinas',
                                    help='Click aqui para Alteara a Tabela',
                                    width='stretch',
                                    disabled=fDesativado,)
        
        with col17:
            delButton = st.button(label='Deletar',
                                    key='delDisciplinas',
                                    help='Click aqui para Deletar a Tabela',
                                    width='stretch',
                                    disabled=fDesativado,)
    else:
        st.error('Houve um Problema com a pesquisa')
    
    # if regButton:
    #     Pg_C.insDisciplina()
    # if altButton:
    #     Pg_U.altDisciplina(selIndex)
    # if delButton:
    #     Pg_D.delDisciplinas(selIndex)