"""TESTES DE INTEGRAÇÃO EM BDD: features/emprestimo.feature + serviço + repositório + SQLite em memória.

Cada passo do .feature (Dado / Quando / Então) é ligado a UMA função abaixo pelo texto
do decorador (@given, @when, @then). Os decoradores dos cenários prontos já estão
escritos: falta o corpo. Substitua cada pytest.fail("TODO ...") pelo código do passo.

- Dado (Arrange): monte o estado usando as fixtures repo e servico do conftest.py.
- Quando (Act): execute UMA ação no servico. Se ela pode ser recusada, capture a
  EmprestimoNegado em contexto["erro"] em vez de deixar o teste quebrar.
- Então (Assert): confira o resultado LENDO O BANCO (repo ou conn), não só o retorno.

Os cenários que você escrever no .feature (R3 e R4) vão precisar de passos novos:
crie as funções aqui, no mesmo padrão. Não apague nem renomeie as funções existentes.
"""
import pytest
from pytest_bdd import given, parsers, scenarios, then, when

from lermais.servico import EmprestimoNegado
from tests.step_defs.apoio import data_br, reais

scenarios("emprestimo.feature")


# ------------------------------------------------------------------ Dado

@given(parsers.re(r'que a biblioteca tem o livro "(?P<titulo>[^"]+)" com (?P<exemplares>\d+) exemplar(?:es)?'))
def livro_cadastrado(repo, contexto, titulo, exemplares):
    """Cadastra o livro com int(exemplares) e guarda o id em contexto["livros"][titulo]."""
    pytest.fail("TODO: implemente este passo")


@given(parsers.re(r'que (?:a leitora|o leitor) "(?P<nome>[^"]+)" está cadastrad[ao]'))
def leitor_cadastrado(repo, contexto, nome):
    """Cadastra o leitor e guarda o id em contexto["leitores"][nome]."""
    pytest.fail("TODO: implemente este passo")


@given(parsers.parse('que "{nome}" pegou "{titulo}" emprestado em {data}'))
def emprestimo_anterior(servico, contexto, nome, titulo, data):
    """Faz o empréstimo pelo servico e guarda o id em contexto["emprestimos"][(nome, titulo)]."""
    pytest.fail("TODO: implemente este passo")


# ---------------------------------------------------------------- Quando

@when(parsers.parse('"{nome}" pega "{titulo}" emprestado em {data}'))
def pegar_emprestado(servico, contexto, nome, titulo, data):
    """Tenta o empréstimo. Sucesso: id em contexto["ultimo_id"] (e em contexto["emprestimos"]).
    Recusa: a exceção EmprestimoNegado vai para contexto["erro"]."""
    pytest.fail("TODO: implemente este passo")


@when(parsers.parse('"{nome}" devolve "{titulo}" em {data}'))
def devolver(servico, contexto, nome, titulo, data):
    """Devolve o empréstimo de (nome, titulo) na data informada."""
    pytest.fail("TODO: implemente este passo")


# ----------------------------------------------------------------- Então

@then(parsers.parse("o empréstimo fica registrado com devolução prevista para {data}"))
def emprestimo_registrado(repo, contexto, data):
    """Leia o empréstimo no banco e confira a data_prevista (o banco guarda 'AAAA-MM-DD')."""
    pytest.fail("TODO: implemente este passo")


@then(parsers.re(r'"(?P<titulo>[^"]+)" fica com (?P<quantidade>\d+) exemplar(?:es)? disponíve(?:l|is)'))
def exemplares_disponiveis(repo, contexto, titulo, quantidade):
    """Confira no banco quantos exemplares do livro estão disponíveis."""
    pytest.fail("TODO: implemente este passo")


@then(parsers.parse('o empréstimo é recusado com a mensagem "{mensagem}"'))
def emprestimo_recusado(contexto, mensagem):
    """Confira que houve EmprestimoNegado e que str(erro) é exatamente a mensagem."""
    pytest.fail("TODO: implemente este passo")


@then(parsers.parse("a multa registrada no empréstimo é de R$ {valor}"))
def multa_registrada(repo, contexto, valor):
    """Leia a coluna multa do empréstimo NO BANCO e compare com reais(valor) usando pytest.approx."""
    pytest.fail("TODO: implemente este passo")


@then(parsers.parse('"{nome}" não tem multa pendente'))
def sem_multa_pendente(repo, contexto, nome):
    """Confira no banco que a multa pendente do leitor é 0.0."""
    pytest.fail("TODO: implemente este passo")
