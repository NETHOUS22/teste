# language: pt
Funcionalidade: Empréstimo e devolução de livros na LerMais
  Como leitora da biblioteca comunitária LerMais
  Quero pegar e devolver livros emprestados
  Para ler sem precisar comprar

  Contexto:
    Dado que a biblioteca tem o livro "Dom Casmurro" com 2 exemplares
    E que a leitora "Ana" está cadastrada

  Cenário: Empréstimo reduz os exemplares disponíveis (R1, R5)
    Quando "Ana" pega "Dom Casmurro" emprestado em 16/10/2026
    Então o empréstimo fica registrado com devolução prevista para 30/10/2026
    E "Dom Casmurro" fica com 1 exemplar disponível

  Cenário: Livro sem exemplar disponível é recusado (R5)
    Dado que a biblioteca tem o livro "Memórias Póstumas" com 1 exemplar
    E que a leitora "Bia" está cadastrada
    E que "Bia" pegou "Memórias Póstumas" emprestado em 16/10/2026
    Quando "Ana" pega "Memórias Póstumas" emprestado em 16/10/2026
    Então o empréstimo é recusado com a mensagem "Nenhum exemplar disponível"

  Cenário: Devolução libera o exemplar (R5)
    Dado que a biblioteca tem o livro "Memórias Póstumas" com 1 exemplar
    E que "Ana" pegou "Memórias Póstumas" emprestado em 16/10/2026
    Quando "Ana" devolve "Memórias Póstumas" em 20/10/2026
    Então "Memórias Póstumas" fica com 1 exemplar disponível

  Cenário: Devolução no prazo não gera multa (R1, R2)
    Dado que "Ana" pegou "Dom Casmurro" emprestado em 16/10/2026
    Quando "Ana" devolve "Dom Casmurro" em 30/10/2026
    Então a multa registrada no empréstimo é de R$ 0,00
    E "Ana" não tem multa pendente

  Esquema do Cenário: Multa por atraso nos valores-limite (R2)
    Dado que "Ana" pegou "Dom Casmurro" emprestado em 16/10/2026
    Quando "Ana" devolve "Dom Casmurro" em <devolucao>
    Então a multa registrada no empréstimo é de R$ <multa>

    Exemplos:
      | devolucao  | multa |
      | 31/10/2026 | 1,50  |
      | 18/11/2026 | 28,50 |
      | 19/11/2026 | 30,00 |
      | 20/11/2026 | 30,00 |

  # ===================================================================
  # SUA PARTE (escreva os cenários abaixo, apague estes comentários)
  # ===================================================================
  #
  # 1) Esquema do Cenário para R3 (no máximo 3 empréstimos ativos por leitor).
  #    Tabela Exemplos com, no mínimo, duas linhas: o leitor que já tem 2
  #    empréstimos ativos (o próximo é aceito) e o que já tem 3 (o próximo é
  #    recusado com a mensagem "Limite de 3 empréstimos ativos atingido").
  #
  # 2) Cenário para R4 (leitor com multa pendente não pega livro novo):
  #    a leitora devolve com atraso e, depois, tenta um novo empréstimo.
  #
  # Regras de estilo (Aula 10): um único Quando por cenário, Então
  # verificável, nada de tela, botão, tabela ou SQL nos passos.
