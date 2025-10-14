import streamlit as st
import Controllers.listas as lst
import Controllers.crudCEP as ctb

@st.dialog('CEP - Criação de Registros')
def insCEP():
    
    nCep = st.text_input(label='CEP',
                        max_chars=9,
                        placeholder='00000-000',
                        )
    err = st.error('').empty()


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
        insButton = st.button(label='Inserir',
                              width='stretch')
    
    nCepP = nCep.replace('-','')
    parametros = {'cep': nCepP,
                  'logradouro': nLogradouro,
                  'bairro': nBairro,
                  'cidade': nCidade,
                  'estado': nEstado}
    if insButton:
        if not nCep:
            err = st.error('Insira o CEP!')
        else:
            err.empty()
            st.spinner()
            ctb.inserir(parametros)
        
