import streamlit as st

def painel_movimentacoes():
    st.subheader("Movimentações da carteira")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.subheader("Adicionar Movimentação")
    with col2:
        st.subheader("Editar Movimentação")
    with col3:
        st.subheader("Excluir Movimentação")