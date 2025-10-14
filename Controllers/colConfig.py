import streamlit as st

def colConfigTabGer():
    config = {
        'dominio': None,   
        'valor': st.column_config.Column(label='Valor',
                                         disabled=True,),
        'descricao': st.column_config.Column(label='Descrição',
                                         disabled=True,),
        'obs': st.column_config.Column(label='Observação',
                                         disabled=True,)
    }
    return config

def colConfigCep():
    config = {
        'cep': st.column_config.Column(label='CEP',
                                         disabled=True,),
        'logradouro': st.column_config.Column(label='Logradouro',
                                         disabled=True,),
        'bairro': st.column_config.Column(label='Bairro',
                                         disabled=True,),
        'cidade': st.column_config.Column(label='Cidade',
                                         disabled=True,),
        'estado': st.column_config.Column(label='Estado',
                                         disabled=True,)
    }
    return config