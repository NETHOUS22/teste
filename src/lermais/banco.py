"""Conexão e esquema do banco SQLite do LerMais."""
import sqlite3

ESQUEMA = """
CREATE TABLE IF NOT EXISTS leitores (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS livros (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo TEXT NOT NULL,
    exemplares INTEGER NOT NULL CHECK (exemplares >= 0)
);
CREATE TABLE IF NOT EXISTS emprestimos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    leitor_id INTEGER NOT NULL REFERENCES leitores (id),
    livro_id INTEGER NOT NULL REFERENCES livros (id),
    data_emprestimo TEXT NOT NULL,
    data_prevista TEXT NOT NULL,
    data_devolucao TEXT,
    multa REAL NOT NULL DEFAULT 0,
    multa_paga INTEGER NOT NULL DEFAULT 0
);
"""


def conectar(caminho="lermais.db"):
    """Abre a conexão. Em produção usa um arquivo; nos testes, ":memory:"."""
    conn = sqlite3.connect(caminho)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


def criar_esquema(conn):
    """Cria as três tabelas, se ainda não existirem."""
    conn.executescript(ESQUEMA)
    conn.commit()
