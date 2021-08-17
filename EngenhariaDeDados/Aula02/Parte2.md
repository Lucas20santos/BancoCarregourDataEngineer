# Data warehouse (WD)

## Antes do Data Warehouse

- Falta de credibilidade dos dados, consequência de extrações
- Baixa produtividade
- Dificuldade em gerar informação a partir dos dados extraídos

## Definição

É uma arquitetura de armazenamento projetada para conter dados extraídos de sistemas de transações, armazenamentos de dados operacionais e fontes externas.

Combina esses dados em m formulário de resumo agregado adequado para análise de dados em toda a empresa e relatórios para necessidades de negócios predefinidas.

## OLTP Versus OLAP
    |                   | Online Transactional Processing - OLTP    | Online Analytical Processing - OLAP               |
-------------------------------------------------------------------------------------------------------------------------
1   |   Foco            | Operações do dia a dia                    | Suporte a decisão                                 |
-------------------------------------------------------------------------------------------------------------------------
2   |   Origem          | Transações em tempo real da organização   | Base de dados de sistema transacionais - OLTP     |
-------------------------------------------------------------------------------------------------------------------------
3   |   Perfomace       | Milisseguros                              | Minutos / Horas                                   |
-------------------------------------------------------------------------------------------------------------------------
4   |   Volatilidade    | Atualizações curtas e rápidas iniciadas   | Geralmente grande devido à agregação de grandes   |
                        | pelo usuário                              | Conjuntos de dados                                |
-------------------------------------------------------------------------------------------------------------------------
5   |   Design          | Normalizado                               | Desnomalizado                                     |
-------------------------------------------------------------------------------------------------------------------------