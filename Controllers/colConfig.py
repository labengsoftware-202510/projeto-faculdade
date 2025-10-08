import streamlit as st

def colConfig():
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

