# Data warehouse (WD)

## Antes do Data Warehouse

- Falta de credibilidade dos dados, consequência de extrações
- Baixa produtividade
- Dificuldade em gerar informação a partir dos dados extraídos

## Definição

É uma arquitetura de armazenamento projetada para conter dados extraídos de sistemas de transações, armazenamentos de dados operacionais e fontes externas.

Combina esses dados em m formulário de resumo agregado adequado para análise de dados em toda a empresa e relatórios para necessidades de negócios predefinidas.

## OLTP Versus OLAP
  Indece  | Tema    | Online Transactional Processing - OLTP    | Online Analytical Processing - OLAP               
:--:|:-----------------:|:-----------------------------------------:|:-------------------------------------------------:
1   |   Foco            | Operações do dia a dia                    | Suporte a decisão                                 
2   |   Origem          | Transações em tempo real da organização   | Base de dados de sistema transacionais - OLTP     
3   |   Perfomace       | Milisseguros                              | Minutos / Horas                                   
4   |   Volatilidade    | Atualizações curtas e rápidas iniciadas pelo usuário| Geralmente grande devido à agregação de grandes conjuntos de dados                                
5   |   Design          | Normalizado                               | Desnomalizado                                     

## Movimentação dos dados

Como fazer a movimentação dos dados entre as camadas do DW ?

### ETL (Extract, Transform, Load)

É um processo automatizado que coleta dados brutos, extrai as informações necessárias para análise, transforma em um formato que atende às necessidades de negócios e carrega em um data warehouse.

#### ETL - Tipos de movimentação

- Movimentação de volumes de dados
    - Cargas completas - truncate & load
    - Cargas incrementais - data / ID
    - Frequência (diária, semanal, mensal)
- Pode melhorar signiicativamente a qualidade dos dados
    - Qualidade e padronização / validação dos dados
    - Metadados(descrevem os atributos dos dados - significado)

#### ETL - desafios

- **Escalabilidade** - A escalabilidade é um dos recursos mais importantes em uma ferramenta ETL moderna
- **Acurácia** - garantir que os dados que você transforma sejam e completos
- **Manusear fontes de dados diversas** - lidar comdiversos tipos de fontes de dados

## Considerações finais

- DW é fundamental para um sistema de apoio à decisão
- Acesso simplificado a dados historicos 
- Facidadade em consulta de informações
- Avalie as origens e tipos de dados
- Planeje a malha de ETLs
- Atençaõ a modelagem dos dados(Dimensional)
- Produção de relatórios
