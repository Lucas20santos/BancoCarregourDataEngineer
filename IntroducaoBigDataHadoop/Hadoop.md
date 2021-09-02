# Introdução ao Hadoop

Criado por DOug Cutting, é um framework "open source" que oferece recursos de armazenamento, gerenciamento e processamento distribuído dados

Um dos benefícios do Hadoop é que ele roda em clusters de baixo custo e provê uma escalabilidade horizontal.

A arquitetura do haddop é formada por 4 módulos base:

- Common: bibliotecas (java) e utilitários;
- MapReduce: processamento massivo e paralelos de dados;
- YARN: gestão de recursos do cluster;
- HDFS: gerenciamento e armazenamento de dados distribuídos;

## HDFS

### O que é HDFS

O HDFS realiza o gerenciamento e armazenamento de dados distribuídos, fornecendo acesso rápido aos dados.

- Name Node(Meta dados)
  - Data Node 1
  - Data Node 2
  - Data Node 3
- Stand By Name Node (Meta dados)

alta disponibilidade através do Hadoop

### Como funciona o HDFS

O HDFS é tolerante a falhas e realiza automaticamento o balanceamento dos dados.

### Interagindo com o HDFS

Os comandos para acessar o HDFS iniciam sempre por "hdfs dfs -" depois o comando que gostaria de executar. Esse comoando praticamento os comandos do Linux. Exemplos:

- Listar diretóriso: hdfs dfs -ls / diretorios_hdfs
- Download de arquivo do HDFS: hdfs dfs -get /diretorio_hdfs/arquivo
- Upload de arquivo para o HDFS: hdfs dfs -put arquivo/diretorio_destino_hdfs
- Visualizar todos os comandos HDFS: hdfs dfs -help

## MapReduce

É um modelo de programação que permite processamento massivo em algoritmo paralelo e distribuído

## O que é o YARN

O YARN é responsável por distribuir os recursos computacionais como uso de memória e  processamento para os jobs, otimizando o processamento paralelo.

- YARN
  - LOTE (MapReduce)
  - Interativo(Tez)
  - Streaming (Storm, S4)
  - IN-Memory (Spark)
  - Outros

O YARN define quem, quando e onde devem ser realizados os processamentos e quais recursos devem ser alocados para cada tarefa.
