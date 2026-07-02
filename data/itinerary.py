from __future__ import annotations

from datetime import date
from typing import List, Dict


def get_trip_start_date() -> date:
    """Data de início da Eurotrip."""
    # 30/out/2026
    return date(2026, 10, 30)


def get_itinerary_cities() -> List[Dict[str, str]]:
    """
    Lista de destinos principais da Eurotrip, usados na home como cards.

    Cada item tem:
    - name: nome do destino
    - country: país
    - description: breve texto
    - image_url: URL de foto ilustrativa (pode trocar depois pelas suas fotos)
    """
    return [
        {
            "name": "Madrid",
            "country": "Espanha",
            "description": "Porta de entrada da Eurotrip, cultura e gastronomia intensa.",
            "image_url": "https://picsum.photos/seed/madrid/600/400",
        },
        {
            "name": "Barcelona",
            "country": "Espanha",
            "description": "Arquitetura de Gaudí, clima mediterrâneo e muita arte.",
            "image_url": "https://picsum.photos/seed/barcelona/600/400",
        },
        {
            "name": "Bruxelas",
            "country": "Bélgica",
            "description": "Chocolate, cervejas belgas e arquitetura charmosa.",
            "image_url": "https://picsum.photos/seed/bruxelas/600/400",
        },
        {
            "name": "Paris",
            "country": "França",
            "description": "Cidade luz, ícones históricos e romance.",
            "image_url": "https://picsum.photos/seed/paris/600/400",
        },
        {
            "name": "Marne-la-Vallée / Disney",
            "country": "França",
            "description": "Dia mágico na Disneyland Paris.",
            "image_url": "https://picsum.photos/seed/disneyparis/600/400",
        },
        {
            "name": "Milão",
            "country": "Itália",
            "description": "Moda, Duomo e base para os Alpes.",
            "image_url": "https://picsum.photos/seed/milao/600/400",
        },
        {
            "name": "Tirano",
            "country": "Itália",
            "description": "Ponto de partida para o passeio até a Suíça.",
            "image_url": "https://picsum.photos/seed/tirano/600/400",
        },
        {
            "name": "Poschiavo",
            "country": "Suíça",
            "description": "Paisagens alpinas e lagos cinematográficos.",
            "image_url": "https://picsum.photos/seed/poschiavo/600/400",
        },
        {
            "name": "St. Moritz",
            "country": "Suíça",
            "description": "Luxo nos Alpes, vilarejo e neve.",
            "image_url": "https://picsum.photos/seed/stmoritz/600/400",
        },
        {
            "name": "Florença",
            "country": "Itália",
            "description": "Berço do Renascimento, arte e história em cada esquina.",
            "image_url": "https://picsum.photos/seed/florenca/600/400",
        },
        {
            "name": "Veneza",
            "country": "Itália",
            "description": "Canais, gondolas e arquitetura única.",
            "image_url": "https://picsum.photos/seed/veneza/600/400",
        },
        {
            "name": "Pisa",
            "country": "Itália",
            "description": "Torre inclinada e bate-volta clássico.",
            "image_url": "https://picsum.photos/seed/pisa/600/400",
        },
        {
            "name": "Roma",
            "country": "Itália",
            "description": "Coliseu, história milenar e boa comida.",
            "image_url": "https://picsum.photos/seed/roma/600/400",
        },
        {
            "name": "Vaticano",
            "country": "Cidade-Estado",
            "description": "Basílica de São Pedro e Museus Vaticanos.",
            "image_url": "https://picsum.photos/seed/vaticano/600/400",
        },
    ]
