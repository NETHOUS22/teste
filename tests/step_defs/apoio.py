"""Conversores de texto do Gherkin para Python. Prontos: use, não precisa alterar."""
from datetime import date, datetime


def data_br(texto: str) -> date:
    """'16/10/2026' -> date(2026, 10, 16)"""
    return datetime.strptime(texto.strip(), "%d/%m/%Y").date()


def reais(texto: str) -> float:
    """'28,50' -> 28.5"""
    return float(texto.strip().replace(".", "").replace(",", "."))
