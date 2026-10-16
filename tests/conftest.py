"""Fixtures compartilhadas. NÃO altere este arquivo; crie fixtures novas nos seus testes, se quiser."""
import pytest

from lermais.banco import conectar, criar_esquema
from lermais.repositorio import RepositorioBiblioteca
from lermais.servico import ServicoEmprestimo


@pytest.fixture
def conn():
    """Banco SQLite novo, só na memória, para CADA teste (escopo function)."""
    conexao = conectar(":memory:")   # Arrange da infraestrutura
    criar_esquema(conexao)
    yield conexao                    # o teste roda aqui
    conexao.close()                  # teardown: o banco some


@pytest.fixture
def repo(conn):
    return RepositorioBiblioteca(conn)


@pytest.fixture
def servico(repo):
    return ServicoEmprestimo(repo)


@pytest.fixture
def contexto():
    """Memória de UM cenário BDD: guarda ids e resultados entre os passos Dado, Quando e Então.

    leitores:     nome   -> id do leitor
    livros:       titulo -> id do livro
    emprestimos:  (nome, titulo) -> id do empréstimo
    ultimo_id:    id do último empréstimo feito no Quando (ou None)
    erro:         exceção capturada no Quando (ou None)
    """
    return {"leitores": {}, "livros": {}, "emprestimos": {}, "ultimo_id": None, "erro": None}
