from __future__ import annotations

from typing import Dict

import streamlit as st


def render_destination_grid(destinations: list[Dict[str, str]]) -> None:
    """
    Renderiza a grade de cards de destinos, em 3 colunas, inspirada na imagem de referência.

    Ajustes:
    - Cards com nome da cidade, país, descrição e foto.
    - Visual escuro com cantos arredondados e leve sombra.
    """
    cols = st.columns(3, gap="large")
    for idx, dest in enumerate(destinations):
        col = cols[idx % 3]
        with col:
            _render_single_card(dest)


def _render_single_card(dest: Dict[str, str]) -> None:
    name = dest.get("name", "Destino")
    country = dest.get("country", "")
    description = dest.get("description", "")
    image_url = dest.get("image_url", "")

    st.markdown(
        f"""
        <div class="destination-card">
            <div class="destination-image-wrapper">
                <img src="{image_url}" alt="{name}" class="destination-image" loading="lazy" />
            </div>
            <div class="destination-content">
                <div class="destination-title-row">
                    <span class="destination-name">{name}</span>
                    <span class="destination-country">{country}</span>
                </div>
                <p class="destination-description">
                    {description}
                </p>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
