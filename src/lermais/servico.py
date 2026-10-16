"""Serviço de empréstimo: junta as regras puras com o repositório (banco)."""
from datetime import date

from lermais.regras import LIMITE_EMPRESTIMOS, calcular_multa, data_prevista, dias_de_atraso


class EmprestimoNegado(Exception):
    """O empréstimo foi recusado por uma regra da biblioteca."""


class ServicoEmprestimo:
    def __init__(self, repo):
        self.repo = repo

    def emprestar(self, leitor_id, livro_id, hoje):
        """Registra o empréstimo e devolve o id. Recusa com EmprestimoNegado quando:

        - o leitor tem multa pendente (qualquer valor acima de zero);
        - o leitor já tem 3 empréstimos ativos (o limite é 3 ao mesmo tempo);
        - o livro não tem exemplar disponível.
        """
        if self.repo.multa_pendente(leitor_id) > 0:
            raise EmprestimoNegado("Leitor com multa pendente")
        if self.repo.contar_emprestimos_ativos(leitor_id) > LIMITE_EMPRESTIMOS:
            raise EmprestimoNegado("Limite de 3 empréstimos ativos atingido")
        if self.repo.exemplares_disponiveis(livro_id) <= 0:
            raise EmprestimoNegado("Nenhum exemplar disponível")
        return self.repo.registrar_emprestimo(leitor_id, livro_id, hoje, data_prevista(hoje))

    def devolver(self, emprestimo_id, hoje):
        """Registra a devolução e devolve o valor da multa (0.0 se estiver no prazo)."""
        emprestimo = self.repo.buscar_emprestimo(emprestimo_id)
        if emprestimo is None:
            raise ValueError("empréstimo inexistente")
        if emprestimo["data_devolucao"] is not None:
            raise ValueError("empréstimo já devolvido")
        atraso = dias_de_atraso(date.fromisoformat(emprestimo["data_prevista"]), hoje)
        multa = calcular_multa(atraso)
        self.repo.registrar_devolucao(emprestimo_id, hoje, multa)
        return multa
