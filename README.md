# Aplicação do Coverage.py

## Setup

### Criar Ambiente

```bash
python3 -m venv venv
source venv/bin/activate
```

- Veja que não temos o `coverage.py` instalado ainda. Vamos instalá-lo

### Instalação


```bash
pip install coverage
pip list
coverage --version
```


## Uso de Funcionalidades Básicas

### Testando com Coverage.py

- Nesse exemplo usaremos unittest como biblioteca de testes

```bash
coverage run -m unittest discover
```

- Veja que isso executa os testes usando o unittest normalmente, mas gera um arquivo `.coverage` no diretório.

- Veja como o coverage.py se integra de forma simples e rápida com o framework de testes.

### Geração de Relatórios

#### Relatório Simples Pelo Terminal

- Agora vamos gerar nosso primeiro relatório através do próprio terminal.


```bash
coverage report
```

#### Relatório Detalhado em HTML

- Agora vamos gerar um relatório mais detalhado em html.


```bash
coverage html
```

## Funcionalidade de Cobertura de Branches

- Para analisarmos a cobertura de branches precisamos adicionar uma flag `--branch` na hora de executarmos os testes.

```bash
coverage run --branch -m unittest discover
```

- Isso adicionará a análise de cobertura de branches no nosso relatório em HTML.

```bash
coverage html
```

## Integração com Pipelines de CI para Garantia de Qualidade

- Veja que podemos utilizar o `coverage.py` para garantir uma cobertura mínima do nosso código

```bash
coverage report --fail-under=90
```

- Se tivéssemos um pipline de CICD integrado com o projeto, subir esse código pra produção falharia por não atingir a cobertura mínima de testes de 90%.


## Exclusão de Porções Código com `# pragma: no cover`

- Para uma porção de código que não quisermos considerar na cobertura, podemos utilizar o comentário `# pragma: no cover` para desconsiderá-lo nas nossas análises de cobertura.

### Exemplo Sem Exclusão de Código:

- Aqui vamos simplesmente regerar os relatório para podermos compará-los com os relatórios que fazem exclusão de código:

```bash
coverage run -m unittest discover
coverage report
coverage html
```

### Exemplo Com Exclusão de Uma Linha Código:

- Aqui vamos adicionar o `# pragma: no cover` à linha `a = -a` do método `abs_add()`.

```bash
coverage run -m unittest discover
coverage report
coverage html
```

- Veja que tanto a porcentagem de cobertura mudou quanto o detalhamento de número de linhas excluídas no relatório em HTML.

### Exemplo Com Exclusão de Um Bloco de Código:

- Aqui vamos adicionar o `# pragma: no cover` ao bloco `if a < 0:` do método `abs_add()`.

```bash
coverage run -m unittest discover
coverage report
coverage html
```

- Veja que isso não só excluiu a linha `if a < 0:` da análise de cobertura como todo o código do bloco definido pelo if.

- Veja que a porcentagem de cobertura diminuiu em relação ao último exemplo pois eliminamos agora uma linha que já estava coberta.

### Exemplo Com Exclusão de Um Bloco de Código:

- Aqui vamos adicionar o `# pragma: no cover` ao método `abs_add()` inteiro.

```bash
coverage run -m unittest discover
coverage report
coverage html
```

- Veja que a porcentagem de cobertura diminuiu em relação ao último exemplo pois eliminamos mais linhas que estavam cobertas do que linhas não cobertas.

## Conclusão

Veja que o `coverage.py` é uma ferramenta rápida e fácil de se usar, mas ao mesmo tempo consegue gerar relatórios detalhados. Além disso possui diversas funcionalidades como integração fácil com bibliotecas de teste e permitem uma fácil integração com pipelines de CICD.