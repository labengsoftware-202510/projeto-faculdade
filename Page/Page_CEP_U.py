import streamlit as st
import Controllers.listas as lst
import Controllers.crudCEP as ctb

@st.dialog('CEP - Alteração de Registros')
def altCEP(parametros):
    lista = lst.listTabGer('est_brl')
    
    nCep =st.text_input(label='CEP',
                    max_chars=8,
                    placeholder='00000000',
                    value=parametros['cep'],
                    disabled=True,
                    )

    nLogradouro = st.text_input(label='Logradouro',
                                max_chars=30,
                                placeholder='Insira o Logradouro',
                                value=parametros['logradouro'],
                                )
    
    nBairro = st.text_input(label='Bairro',
                            max_chars=30,
                            placeholder='Insira o Bairro',
                            value=parametros['bairro'],
                            )
    
    nCidade = st.text_input(label='Cidade',
                            max_chars=30,
                            placeholder='Insira a Cidade',
                            value=parametros['cidade'],
                            )
    nEstIndex = lst.buscaIndex(lista, parametros['estado'])
    nEstado = st.selectbox(label= 'Filtro por Estados',
                                options= lista,
                                format_func= lambda record: f'{record["descricao"]}',
                                index= nEstIndex,
                                )
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
        ctb.alterar(parametros)
        
