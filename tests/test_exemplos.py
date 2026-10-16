"""Dois testes de EXEMPLO, prontos. Leia antes de escrever os seus. Não altere este arquivo."""
from datetime import date

from lermais.regras import data_prevista


def test_exemplo_unidade_data_prevista_soma_14_dias():
    # Arrange
    emprestimo = date(2026, 10, 16)
    # Act
    prevista = data_prevista(emprestimo)
    # Assert
    assert prevista == date(2026, 10, 30)


def test_exemplo_integracao_livro_cadastrado_fica_no_banco(repo):
    # Arrange
    livro_id = repo.cadastrar_livro("Dom Casmurro", exemplares=2)
    # Act
    livro = repo.buscar_livro(livro_id)
    # Assert
    assert livro["titulo"] == "Dom Casmurro"
    assert livro["exemplares"] == 2
