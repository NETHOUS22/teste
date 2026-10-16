"""TESTES DE UNIDADE (reforço): regras puras de lermais/regras.py, sem banco e sem BDD.

Substitua cada pytest.fail("TODO ...") por um teste de verdade, no padrão
Arrange / Act / Assert (com os três comentários). Não apague nem renomeie as funções.
"""
import pytest

from lermais.regras import calcular_multa


def test_multa_nos_valores_limite():
    """Use @pytest.mark.parametrize com pelo menos QUATRO pares (dias de atraso, multa esperada).

    Cubra: sem atraso, um dia, o ponto em que a multa encosta no teto e logo depois do teto.
    """
    pytest.fail("TODO: implemente este teste")


def test_multa_com_atraso_negativo_lanca_erro():
    """Atraso negativo não existe: a função deve lançar ValueError (use pytest.raises)."""
    pytest.fail("TODO: implemente este teste")
