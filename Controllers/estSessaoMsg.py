import streamlit as st

def setSessionState():
    if 'usuario' not in st.session_state:
        st.session_state['usuario'] = ''
    if 'RI' not in st.session_state:
        st.session_state['RI'] = None
    if 'perfil' not in st.session_state:
        st.session_state['perfil'] = ''
    if 'commandOk' not in st.session_state:
        st.session_state['commandOk'] = True
    if 'statusMessage' not in st.session_state:
        st.session_state['statusMessage'] = ''
    

def initStatusMsg():
    if 'commandOk' not in st.session_state:
        st.session_state['commandOk'] = True
    if 'statusMessage' not in st.session_state:
        st.session_state['statusMessage'] = ''

def operacaoSucesso(mensagem):
    if 'commandOk' not in st.session_state or 'statusMessage' not in st.session_state:
        st.session_state['commandOk'] = True
        st.session_state['statusMessage'] = mensagem
    else:        
        st.session_state.commandOk = True
        st.session_state.statusMessage = mensagem

def operacaoErro(mensagem):
    if 'commandOk' not in st.session_state or 'statusMessage' not in st.session_state:
        st.session_state['commandOk'] = False
        st.session_state['statusMessage'] = mensagem
    else:        
        st.session_state.commandOk = False
        st.session_state.statusMessage = mensagem

def mostraMensagem():
    if ('commandOk' in st.session_state) and ('statusMessage' in st.session_state):
        if st.session_state.commandOk and st.session_state.statusMessage:
            sucesso = st.success(st.session_state.statusMessage)
            st.session_state.statusMessage = ''
            return sucesso
        elif not st.session_state.commandOk and st.session_state.statusMessage:
            erro = st.error(st.session_state.statusMessage)
            st.session_state.statusMessage = ''
            return erro
        else:
            return None
    else:
        return None