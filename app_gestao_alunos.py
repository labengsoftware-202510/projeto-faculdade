import streamlit as st
import Controllers.estSessaoMsg as sessao

st.set_page_config(
    page_title= 'Home',
    layout= 'wide',
    initial_sidebar_state= 'collapsed'
)

pages = {
    "Home":[st.Page("Page/Page_Home.py", title= 'Home')],   
    "Tabelas":[
        st.Page("Page/Page_Pessoas.py", title='Pessoas'),
        st.Page("Page/Page_CEP.py", title="CEP's"),
        st.Page("Page/Page_TabGen.py", title= 'Tabelas Genéricas'),
    ],
    "Sobre":[st.Page("Page/Page_Sobre.py", title= 'Sobre')],
}

st.navigation(pages).run()