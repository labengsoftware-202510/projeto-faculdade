import streamlit as st
import Controllers.listas as lst
import Controllers.crudCEP as ctb

@st.dialog('CEP - Alteração de Registros')
def altCEP(parametros):
    
    nCep =st.text_input(label='CEP',
                    max_chars=8,
                    placeholder='00000000',
                    value=parametros['cep'],
                    disabled=True,
                    )

    nLogradouro = st.text_input(label='Logradouro',
                                max_chars=30,
                                placeholder='Insira o Logradouro',
                                )
    
    nBairro = st.text_input(label='Bairro',
                            max_chars=30,
                            placeholder='Insira o Bairro',
                            )
    
    nCidade = st.text_input(label='Cidade',
                            max_chars=30,
                            placeholder='Insira a Cidade',
                            )
    nEstado = st.st.selectbox(label= 'Filtro por Estados',
                                options= lst.listTabGer('est_brl'),
                                format_func= lambda record: f'{record["descricao"]}')
    nEstado = nEstado['valor']

    col1, col2, col3, col4, col5 = st.columns(5)
    with col5:
        altButton = st.button(label='Alterar',
                              width='stretch')
        
    nCepP = nCep.replace('-','')
    parametros = {'cep': nCepP,
                  'logradouro': nLogradouro,
                  'bairro': nBairro,
                  'cidade': nCidade,
                  'estado': nEstado}
    if altButton:
        st.spinner()
        ctb.inserir(parametros)
        
