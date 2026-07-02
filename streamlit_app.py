from __future__ import annotations

import pathlib

import streamlit as st

from components.sidebar import render_sidebar
from components.header import render_header
from components.destination_card import render_destination_grid
from data.itinerary import get_itinerary_cities


def _inject_local_css() -> None:
    """
    Injeta o CSS customizado da pasta assets/css/style.css.
    """
    css_path = pathlib.Path(__file__).parent / "assets" / "css" / "style.css"
    if css_path.exists():
        with css_path.open("r", encoding="utf-8") as f:
            css = f.read()
        st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)


def main() -> None:
    """
    Página inicial EUROTRIP 2026.

    Ajustes conforme solicitado:
    - Sidebar com itens Dashboard, Ingressos, Transportes, Alimentação, Hospedagem.
    - Sem barra de busca e sem calendário.
    - Cabeçalho:
        Sejam Bem-Vindos Clébio e Katy!
        Faltam XX dias para sua Eurotrip.
    - Texto:
        Click no Card do seu destino!
    - Cards: todas as cidades do roteiro com nome e foto.
    """
    st.set_page_config(
        page_title="EUROTRIP 2026",
        page_icon="✈️",
        layout="wide",
        initial_sidebar_state="expanded",
    )

    _inject_local_css()
    render_sidebar()

    # Cabeçalho
    render_header()

    # Grade de cards de destinos
    destinations = get_itinerary_cities()
    render_destination_grid(destinations)


if __name__ == "__main__":
    main()
