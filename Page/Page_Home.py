import streamlit as st

with st.container(height=300,
                  border=False,
                  horizontal_alignment='center',
                  ):
    st.title('Sistema de Gerenciamento Escolar')

with st.container(height=220,
                  border=False,
                  ):
    st.image(image='images/fatecSpRodape.jpg',
             width='stretch',
             use_container_width=True,)