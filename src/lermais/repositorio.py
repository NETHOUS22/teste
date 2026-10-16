"""Acesso ao banco: tudo o que lê ou grava no SQLite passa por aqui."""


class RepositorioBiblioteca:
    def __init__(self, conn):
        self.conn = conn

    # ---------------------------------------------------------- cadastro
    def cadastrar_leitor(self, nome):
        if not nome or not nome.strip():
            raise ValueError("nome do leitor é obrigatório")
        cur = self.conn.execute("INSERT INTO leitores (nome) VALUES (?)", (nome.strip(),))
        self.conn.commit()
        return cur.lastrowid

    def cadastrar_livro(self, titulo, exemplares):
        if exemplares < 0:
            raise ValueError("número de exemplares não pode ser negativo")
        cur = self.conn.execute(
            "INSERT INTO livros (titulo, exemplares) VALUES (?, ?)", (titulo, exemplares)
        )
        self.conn.commit()
        return cur.lastrowid

    def buscar_livro(self, livro_id):
        row = self.conn.execute("SELECT * FROM livros WHERE id = ?", (livro_id,)).fetchone()
        return dict(row) if row else None

    # ------------------------------------------------------- empréstimos
    def contar_emprestimos_ativos(self, leitor_id):
        row = self.conn.execute(
            "SELECT COUNT(*) FROM emprestimos WHERE leitor_id = ? AND data_devolucao IS NULL",
            (leitor_id,),
        ).fetchone()
        return row[0]

    def exemplares_disponiveis(self, livro_id):
        livro = self.buscar_livro(livro_id)
        if livro is None:
            raise ValueError("livro inexistente")
        emprestados = self.conn.execute(
            "SELECT COUNT(*) FROM emprestimos WHERE livro_id = ? AND data_devolucao IS NULL",
            (livro_id,),
        ).fetchone()[0]
        return livro["exemplares"] - emprestados

    def registrar_emprestimo(self, leitor_id, livro_id, data_emprestimo, data_prevista):
        cur = self.conn.execute(
            "INSERT INTO emprestimos (leitor_id, livro_id, data_emprestimo, data_prevista) "
            "VALUES (?, ?, ?, ?)",
            (leitor_id, livro_id, data_emprestimo.isoformat(), data_prevista.isoformat()),
        )
        self.conn.commit()
        return cur.lastrowid

    def buscar_emprestimo(self, emprestimo_id):
        row = self.conn.execute(
            "SELECT * FROM emprestimos WHERE id = ?", (emprestimo_id,)
        ).fetchone()
        return dict(row) if row else None

    def registrar_devolucao(self, emprestimo_id, data_devolucao, multa):
        self.conn.execute(
            "UPDATE emprestimos SET data_devolucao = ?, multa = ? WHERE id = ?",
            (data_devolucao.isoformat(), multa, emprestimo_id),
        )
        self.conn.commit()

    # ------------------------------------------------------------ multas
    def multa_pendente(self, leitor_id):
        row = self.conn.execute(
            "SELECT COALESCE(SUM(multa), 0) FROM emprestimos WHERE leitor_id = ? AND multa_paga = 0",
            (leitor_id,),
        ).fetchone()
        return round(row[0], 2)

    def quitar_multas(self, leitor_id):
        self.conn.execute(
            "UPDATE emprestimos SET multa_paga = 1 WHERE leitor_id = ? AND multa > 0",
            (leitor_id,),
        )
        self.conn.commit()
