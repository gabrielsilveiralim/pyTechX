# Sprint 5 — Sistema de Análise e Validação de Dados

## Objetivo
Ler um CSV, validar e-mail, CPF, telefone e data com expressões regulares, tratar exceções e gerar estatísticas formatadas.

## Como executar
Requer Python 3.10 ou superior

```bash
python main.py
```

Quando solicitado, informe `dados.csv` ou o caminho do seu arquivo.

## Formato do CSV
O cabeçalho deve conter exatamente as colunas `email,cpf,telefone,data`. Exemplo:

```csv
email,cpf,telefone,data
ana.silva@email.com,12345678901,11987654321,2002-05-14
```

## Justificativa das validações
- **E-mail:** `^` e `$` delimitam a string; `\w` aceita caracteres de palavra e o padrão exige `@` e domínio com ponto.
- **CPF:** aceita 11 dígitos ou a forma `000.000.000-00`. A regex valida somente o formato, não calcula os dígitos verificadores.
- **Telefone:** aceita formatos comuns brasileiros com DDD opcional e código `+55` opcional.
- **Data:** a regex exige `AAAA-MM-DD`


## Estrutura
- `main.py`: programa principal.
- `dados.csv`: amostra de entrada.
