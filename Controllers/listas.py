import streamlit as st

def listTabGer(filtro):
    selectQuery = f"select *"
    selectQuery += f" from tab_ger"
    if filtro is None:
        selectQuery += f";"
    else:
        selectQuery += f" where dominio = '{filtro}';"

    conn = st.connection('mysql', type='sql')
    df = conn.query(selectQuery, 
                    ttl=600)
    return df.to_dict('records')

def listPessoas(parametros):
    # selectQuery = f"select *"
    # selectQuery += f" from pessoas"
    
    ...

def listCEP(parametros):
    ...
