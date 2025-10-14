import streamlit as st

membros = [{'nome': 'Arthur Heinrichs Amaro', 'ra': '22106928'},
           {'nome': 'Bruno Ramiro de Lima', 'ra': '20482313048'},
           {'nome': 'Mariana Rosa Alves de Santana', 'ra': '22205677'},
           {'nome': 'Rafael Castilho', 'ra': '11111111111'},
           {'nome': 'Thiago Hideki Taira', 'ra': '22205120'}]
keys = list(membros[0].keys())

with st.container():
    st.title('Sobre')
    st.subheader('Projeto de Laboratório de Engenharia de Software')

col1, col2 = st.columns([0.3, 0.7])

with st.container():
    with col1:
        st.write(f"Nome:")
    with col2:
        st.write(f"RA:")
    for membro in membros:
        with col1:
            st.write(f"{membro['nome']}")
        with col2:
            st.write(f"{membro['ra']}")