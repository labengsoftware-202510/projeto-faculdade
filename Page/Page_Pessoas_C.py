import streamlit as st
import pandas as pd
import datetime
import Controllers.validacoes as validacoes
import Controllers.listas as lst
import Controllers.crudCEP as cep
import Controllers.crudPessoas as ctb
import Controllers.inputMasks as mask
    
@st.dialog('Pessoas - Criação de Registros')
def insPessoas():
    lista = lst.listTabGer('est_brl')

    #regIns - gerado automaticamente pelo banco de dados
    nNomCom  = st.text_input(label='Nome Completo',
                            max_chars=50,)
    
    nCpf     = st.text_input(label='CPF',
                            max_chars=14,
                            placeholder='000.000.000-00',
                            key='kCPF',)
    nCpf = nCpf.replace('.','').replace('-','')
    
    nDatNas  = st.date_input(label='Data de Nascimento',
                            min_value=datetime.date(1900,1,1),)
    
    
    nCep     =  st.selectbox(label='CEP',
                             options= lst.listaCep(),
                            format_func= lambda record: f'{record["cep_format"]}',
                            )
    nCep = nCep['cep']
    if nCep:
        nCep = f'{nCep:08}'

    vLogradouro = ''
    vBairro     = ''
    vCidade     = ''
    vEstado     = ''
    
    existe = False
    reg = None
    if validacoes.vCepNum(nCep):
        existe,reg = cep.select({'cep':nCep})
    if isinstance(reg, pd.DataFrame) and not reg.empty:
        vLogradouro = reg['logradouro'].iloc[0]
        vBairro     = reg['bairro'].iloc[0]
        vCidade     = reg['cidade'].iloc[0]
        vEstado     = reg['estado'].iloc[0]
    
    nLogradouro = st.text_input(label='Logradouro',
                                max_chars=30,
                                disabled=existe,
                                value=vLogradouro,)
    
    nBairro = st.text_input(label='Bairro',
                                max_chars=30,
                                disabled=existe,
                                value=vBairro,)
    
    nCidade = st.text_input(label='Cidade',
                                max_chars=30,
                                disabled=existe,
                                value=vCidade,)
    
    
    nEstIndex = lst.buscaIndex(lista, vEstado)        
    nEstado = st.selectbox(label= 'Estados',
                            options= lista,
                            format_func= lambda record: f'{record["descricao"]}',
                            index= nEstIndex,
                            )
        
    nNum     = st.number_input(label='Número',
                            )
    
    nComp    = st.text_input(label='Complemento',
                            max_chars=30,)
    
    sit = ''
    nSit = st.toggle(label= 'Estado da Pessoa',
                    value=False,
                    key='tSit',
                    )

    if nSit:
        st.write('Ativo')
        sit = 'Ativo'
    else:
        st.write('Inativo')
        sit = 'Inativo'
    
    categoria   = st.selectbox(label='Categoria',
                               options= lst.listTabGer('crg_pes'),
                               format_func= lambda x:x['descricao'])
    nCategoria = categoria['valor']
    

    parametrosP = {'nom_com': nNomCom,
                  'cpf': nCpf,
                  'dat_nas': nDatNas,
                  'cep': nCep,
                  'num': nNum,
                  'comp': nComp,
                  'categoria':nCategoria,
                  'sit': sit}

    col1, col2, col3, col4, col5 = st.columns(5)
    with col5:
        insButton = st.button(label='Inserir',
                              width='stretch')
    
    if insButton:
        st.spinner()
        ctb.inserir(parametrosP)
