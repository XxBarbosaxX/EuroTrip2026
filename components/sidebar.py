from __future__ import annotations

import streamlit as st


def render_sidebar() -> None:
    """
    Renderiza a sidebar inspirada no layout de referência, adaptada para EUROTRIP 2026.

    Ajustes solicitados:
    - Título TOUR TROVE -> EUROTRIP 2026
    - Itens:
        Dashboard
        Ingressos
        Transportes
        Alimentação
        Hospedagem
    - Removidos: bloco 50% discount e Logout
    """
    with st.sidebar:
        st.markdown(
            """
            <div class="sidebar-header">
                <span class="logo-text">EUROTRIP 2026</span>
            </div>
            """,
            unsafe_allow_html=True,
        )

        # Menu principal – por enquanto apenas ilustrativo
        st.markdown(
            """
            <div class="sidebar-menu">
                <button class="sidebar-item sidebar-item-active">Dashboard</button>
                <button class="sidebar-item">Ingressos</button>
                <button class="sidebar-item">Transportes</button>
                <button class="sidebar-item">Alimentação</button>
                <button class="sidebar-item">Hospedagem</button>
            </div>
            """,
            unsafe_allow_html=True,
        )
