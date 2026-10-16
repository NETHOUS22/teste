"""Regras de negócio puras do LerMais (sem banco): prazo, atraso e multa."""
from datetime import date, timedelta

PRAZO_DIAS = 14          # o livro volta em até 14 dias corridos
MULTA_POR_DIA = 1.50     # R$ 1,50 por dia de atraso
MULTA_MAXIMA = 30.00     # teto da multa por empréstimo
LIMITE_EMPRESTIMOS = 3   # empréstimos ativos ao mesmo tempo, por leitor


def data_prevista(data_emprestimo: date) -> date:
    """Data em que o livro deve voltar: empréstimo + 14 dias corridos."""
    return data_emprestimo + timedelta(days=PRAZO_DIAS)


def dias_de_atraso(prevista: date, devolucao: date) -> int:
    """Dias corridos depois da data prevista. Devolução no prazo ou antes: 0."""
    return max(0, (devolucao - prevista).days)


def calcular_multa(dias_atraso: int) -> float:
    """R$ 1,50 por dia de atraso, limitado a R$ 30,00.

    Atraso negativo não existe: lança ValueError.
    """
    if dias_atraso < 0:
        raise ValueError("dias de atraso não pode ser negativo")
    return round(min(dias_atraso * MULTA_POR_DIA, MULTA_MAXIMA), 2)
