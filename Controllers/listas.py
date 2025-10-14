import streamlit as st
import pandas as pd

def listTabGer(filtro):
    selectQuery = f"select *"
    selectQuery += f" from tab_ger"
    if filtro is None:
        selectQuery += f";"
    else:
        selectQuery += f" where dominio = '{filtro}';"

    conn = st.connection('mysql', type='sql')
    df = pd.DataFrame([{'dominio':filtro, 
                            'valor':'',
                            'descricao':'Selecione...',
                            'obs':''}])
    addRow = conn.query(selectQuery,
                        ttl=600)
    
    dfRetorno = pd.concat([df,addRow],ignore_index=True)
    return dfRetorno.to_dict('records')
