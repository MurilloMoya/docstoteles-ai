import streamlit as st
from services.rag import RAGService


def show():
    st.header("💬 Chat")

    if "collection" not in st.session_state or not st.session_state.collection:
        st.warning("Selecione uma coleção na barra lateral para começar.")
        return

    if (
        "rag_service" not in st.session_state
        or st.session_state.get("loaded_collection") != st.session_state.collection
    ):
        with st.spinner("Carregando coleção..."):
            rag = RAGService()
            loaded = rag.load_collection(st.session_state.collection)

        if not loaded:
            st.error("Não foi possível carregar a coleção selecionada.")
            return

        st.session_state.rag_service = rag
        st.session_state.loaded_collection = st.session_state.collection
        st.session_state.messages = []

    if "messages" not in st.session_state:
        st.session_state.messages = []

    st.info(f"📂 Coleção ativa: {st.session_state.collection}")

    question = st.chat_input("Pergunte algo sobre a documentação:")
    if question:
        with st.spinner("Consultando IA..."):
            result = st.session_state.rag_service.ask_question(question)
            answer = result["result"] if isinstance(result, dict) else result
        st.session_state.messages.append((question, answer))

    for q, a in st.session_state.messages:
        with st.chat_message("user"):
            st.markdown(q)
        with st.chat_message("assistant"):
            st.markdown(a)

    col_limpar, _ = st.columns([1, 6], gap="small")
    with col_limpar:
        if st.button("🗑️ Limpar Chat", type="secondary"):
            st.session_state.messages = []
            st.rerun()
