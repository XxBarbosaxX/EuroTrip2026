from __future__ import annotations

from datetime import date
from dateutil.relativedelta import relativedelta

import streamlit as st

from data.itinerary import get_trip_start_date


def _calculate_days_until_trip(today: date | None = None) -> int:
    """
    Calcula quantos dias faltam para a Eurotrip com base na data de início.
    """
    if today is None:
        today = date.today()

    start = get_trip_start_date()
    delta = start - today
    return max(delta.days, 0)


def render_header() -> None:
    """
    Renderiza o cabeçalho da home:

    - Sejam Bem-Vindos Clébio e Katy!
    - Faltam XX dias para sua Eurotrip.
    - Texto orientando o clique nos cards.
    """
    days_left = _calculate_days_until_trip()

    st.markdown(
        f"""
        <div class="header-container">
            <div class="header-text">
                <h1 class="header-title">Sejam Bem-Vindos Clébio e Katy!</h1>
                <p class="header-subtitle">
                    Faltam <span class="days-highlight">{days_left} dias</span> para sua Eurotrip.
                </p>
                <p class="header-instruction">
                    Click no Card do seu destino!
                </p>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
