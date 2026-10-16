# Laboratório BDD + SQLite: Biblioteca LerMais (Aula 11)

**Testes de Software · UniEVANGÉLICA · 2026.2 · Ciclo 02**

> **Janela:** sexta-feira, 16/10/2026, das **18h15 às 23h59** (horário de Brasília).
>
> **Entregue uma vez, quando terminar.** `git push` guarda o código, mas **não gera nota**. Só conta a
> **entrega** (passo 7), feita dentro da janela.

## Contexto

A biblioteca comunitária **LerMais** controla empréstimos com Python e SQLite. O código
já existe: regras puras (`regras.py`), acesso ao banco (`repositorio.py`) e serviço
(`servico.py`). Falta a malha de testes, e **há um defeito plantado** que viola uma das regras.

| Regra | Descrição |
|---|---|
| R1 | O livro deve voltar em até 14 dias corridos a partir do empréstimo. |
| R2 | Multa de R$ 1,50 por dia de atraso, com teto de R$ 30,00 por empréstimo. No prazo, sem multa. |
| R3 | Cada leitor pode ter no máximo 3 empréstimos ativos ao mesmo tempo. |
| R4 | Leitor com multa pendente (acima de R$ 0,00) não pega livro novo até quitar. |
| R5 | Só há empréstimo se houver exemplar disponível; a devolução libera o exemplar. |
| R6 | Leitor precisa de nome; livro não pode ter número negativo de exemplares. |

## O que você vai fazer

Nesta atividade você junta a **Aula 10** (Gherkin) com a **Aula 11** (integração):
cada cenário do `.feature` vira um **teste de integração** que passa pelo serviço,
pelo repositório e por um banco **SQLite em memória** novo a cada cenário.

| Parte | Arquivo | Pontos |
|---|---|---|
| 1. Escrever os cenários de R3 e R4 | `features/emprestimo.feature` | dentro da Parte 2 |
| 2. Implementar os passos Dado / Quando / Então | `tests/step_defs/test_emprestimo_bdd.py` | **6** |
| 3. Testes de unidade das regras puras (reforço) | `tests/test_regras.py` | **2** (1 por teste) |
| 4. Achar, corrigir e relatar o defeito plantado | `src/lermais/` + `EVIDENCIAS.md` | **2** |

### Como a nota automática funciona

Além de rodar os seus testes, o corretor **simula defeitos** no código (por exemplo:
a devolução deixa de liberar o exemplar, ou a multa não é gravada no banco) e confere
se **algum cenário seu falha**. Um teste que passa sempre, mesmo com o código errado,
não vale ponto. Por isso:

- No **Então**, confira o resultado **lendo o banco** (`repo`), não só o retorno da função.
- No **Esquema do Cenário de R3**, teste **o limite**: quem tem 2 ativos e quem tem 3.

## Passo a passo

### 1. Baixe o seu repositório e prepare o ambiente

Aceitar a atividade criou o seu repositório no GitHub, mas **não baixou nada** para o seu computador. O download é o `git clone`.

O repositório é privado e o GitHub não aceita mais senha de conta no Git. Quando o `git clone` pedir **Username**, digite o seu usuário do GitHub. Em **Password**, cole o seu **token de acesso pessoal** (o mesmo da Atividade 01). O terminal não mostra nada enquanto você cola: é normal.

```bash
git clone <URL do SEU repositório>
cd <pasta-do-repositorio>
python3 -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

No Windows, se `python3` não funcionar, use `python` ou `py`. Quando o ambiente estiver ativo, o terminal mostra `(venv)` no começo da linha. Em um terminal novo, ative de novo.

Em computador novo, diga ao Git quem você é (uma vez só), senão o primeiro `git commit` falha:

```bash
git config --global user.name "Seu Nome"
git config --global user.email "seu-email@exemplo.com"
```

### 2. Rode tudo (vai falhar, isso é esperado)

```bash
pytest -v
```

### 3. Implemente os passos dos cenários prontos

Abra `tests/step_defs/test_emprestimo_bdd.py`. Cada função está ligada a um passo do
`.feature` pelo texto do decorador:

```python
@when(parsers.parse('"{nome}" pega "{titulo}" emprestado em {data}'))
def pegar_emprestado(servico, contexto, nome, titulo, data):
    ...
```

`{nome}`, `{titulo}` e `{data}` chegam como texto. Use `data_br("16/10/2026")` e
`reais("28,50")` (em `tests/step_defs/apoio.py`) para converter. A fixture `contexto`
guarda os ids entre um passo e outro do mesmo cenário.

```bash
pytest -v tests/step_defs
```

### 4. Escreva os cenários de R3 e R4

No fim de `features/emprestimo.feature` há a seção **SUA PARTE**. Escreva:

1. um **Esquema do Cenário** para R3, com Exemplos de 2 e de 3 empréstimos ativos
   (o de 3 é recusado com a mensagem `Limite de 3 empréstimos ativos atingido`);
2. um **Cenário** para R4: a leitora devolve com atraso e depois tenta um novo
   empréstimo (recusado com `Leitor com multa pendente`).

Reaproveite os passos existentes sempre que der. Para passos novos, crie funções novas
com `@given`, `@when` ou `@then`. Um único **Quando** por cenário.

### 5. O defeito plantado

Um dos seus cenários vai falhar mesmo com os passos certos. Confira se o teste está
certo, corrija o código **com a menor mudança possível** e preencha `EVIDENCIAS.md`.

### 6. Testes de unidade (reforço)

Em `tests/test_regras.py`: `@pytest.mark.parametrize` com pelo menos 4 casos de multa
(sem atraso, 1 dia, encostando no teto, depois do teto) e `pytest.raises` para atraso negativo.

```bash
pytest -v
```

### 7. Entrega final (UMA vez, quando terminar)

```bash
git add .
git commit -m "Laboratório LerMais: cenários BDD, passos, unidade e correção do defeito"   # sempre com -m
git push
git tag entrega
git push origin entrega
```

Em cerca de 1 minuto, a aba **Actions** mostra a execução (Autograde) e a aba **Releases** mostra a sua nota (`classroom50 autograde: N/10`), com o motivo de cada falha. A nota do AVA é N ÷ 10 × 6,00.

## O que invalida a entrega

- Alterar `tests/conftest.py`, `tests/test_exemplos.py`, `tests/step_defs/apoio.py` ou os
  cenários prontos do `.feature`.
- Alterar `src/` além da correção do defeito plantado.
- Entrega fora da janela. Só a primeira entrega conta.
- Sem log de uso de IA em `EVIDENCIAS.md` (ou registro de que não usou): nota × 0,90.

## Cuidados

- Não feche nem mescle o Pull Request chamado **Feedback** e não mexa na branch `feedback`: o Classroom 50 criou tudo sozinho e é por ali que o professor comenta.
- `git commit` salva só no seu computador. `git push` envia para o GitHub, **mas não gera nota**. Só a tag `entrega` gera.
- Se o `git commit` abrir um editor estranho, você esqueceu o `-m`. Saia com `:q!` (vim) ou `Ctrl+X` (nano) e repita com `-m "mensagem"`.
