import streamlit as st
import datetime
import Controllers.validacoes as validacoes
import Controllers.listas as lst
import Controllers.crudCEP as cep
import Controllers.crudPessoas as ctb
import Controllers.inputMasks as mask
    
@st.dialog('Pessoas - Alteração de Registros')
def altPessoas(parametros):
    listaEst = lst.listTabGer('est_brl')
    listaCrg = lst.listTabGer('crg_pes')

    #regIns - gerado automaticamente pelo banco de dados
    nNomCom  = st.text_input(label='Nome Completo',
                             max_chars=50,
                             value=parametros['nom_com'],)
    
    nCpf     = st.text_input(label='CPF',
                            max_chars=14,
                            placeholder='000.000.000-00',
                            key='kCPF',
                            value= parametros['cpf_format'],)
    nCpf = nCpf.replace('.','').replace('-','')
    
    nDatNas  = st.date_input(label='Data de Nascimento',
                            min_value=datetime.date(1900,1,1),
                            value = parametros['dat_nas'],
                            )
    
    
    nCep     =  st.text_input(label='CEP',
                              max_chars=9,
                                key='nCep',
                                value=parametros['cep_format'],)
    nCep = mask.cepUnmask(nCep)
    
    existe = False
    reg = None
    nLogradouro = ''
    nBairro = ''
    nCidade = ''
    nEstado = ''
    if validacoes.vCepNum(nCep):
      existe,reg = cep.select({'cep':nCep})
    
    if existe:
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
        
        
        nEstIndex = lst.buscaIndex(listaEst, vEstado)        
        nEstado = st.selectbox(label= 'Estados',
                                options= listaEst,
                                format_func= lambda record: f'{record["descricao"]}',
                                index= nEstIndex,
                                disabled=existe,
                                )
    else:
        nLogradouro = st.text_input(label='Logradouro',
                                    max_chars=30,)
        
        nBairro = st.text_input(label='Bairro',
                                    max_chars=30,)
        
        nCidade = st.text_input(label='Cidade',
                                    max_chars=30,)
        
        nEstado = st.selectbox(label= 'Estados',
                                options= listaEst,
                                format_func= lambda record: f'{record["descricao"]}',
                                )
        
    nNum     = st.number_input(label='Número',
                                min_value=0,
                                max_value=99999,
                                value=parametros['num'],)
    
    nComp    = st.text_input(label='Complemento',
                            max_chars=30,
                            value=parametros['comp'],)
    
    sit = ''
    nSit = st.toggle(label= 'Estado da Pessoa',
                    value=True if parametros['sit']=='Ativo' else False,
                    key='tSit',
                    )

    if nSit:
        st.write('Ativo')
        sit = 'Ativo'
    else:
        st.write('Inativo')
        sit = 'Inativo'
    
    nCrgIndex = lst.buscaIndex(listaCrg, parametros['categoria'])
    categoria   = st.selectbox(label='Categoria',
                               options= listaCrg,
                               format_func= lambda x:x['descricao'],
                               index= nCrgIndex,
                               )
    nCategoria = categoria['valor']
    

    parametrosP = {'reg_ins':parametros['reg_ins'],
                   'nom_com': nNomCom,
                  'cpf': nCpf,
                  'dat_nas': nDatNas,
                  'cep': nCep,
                  'num': nNum,
                  'comp': nComp,
                  'categoria':nCategoria,
                  'sit': sit}
    
    parametrosC = {'cep': nCep,
                   'logradouro': nLogradouro,
                   'bairro': nBairro,
                   'cidade': nCidade,
                   'estado': nEstado,}

    col1, col2, col3, col4, col5 = st.columns(5)
    with col5:
        insButton = st.button(label='Inserir',
                              width='stretch')
    
    if insButton:
        st.spinner()
        if not existe:
            cep.inserir(parametrosC,flag=True)
        ctb.alterar(parametrosP)
