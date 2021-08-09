# Parte1: Fundamentos de redes

## O que é Rede ?

"Rede de computadores é um conjunto de equipamentos interligados de
maneira a trocarem informações e compartilharem recursos, como
arquivos de dados gravados, impressoras, modems, softwares e outros
equipamentos". (Souza, 1999)

## Tipos de Redes

### Rede Wan

Wide Area Network ou World Area Network é umma rede geograficamente 
distribuída.

### Rede Man

Metropolitan Area Network é uma rede metropolitana que interligam 
várias redes locais

### Rede Lan

Locas Area Network é uma rede local de uma forma geral em um única 
prédio ou campus.

## Protocolos

Protocolo é a "linguagem" usada pelos dispositivos de uma rede de 
modo que eles consigam se entender (Torres, 2004)

Existem vários protocolos

### IP - Protocolo de Internet - Endereço IP - 

números que identificam seu computadores em uma rede

### ICMP - (Internet Control Message Protocol) 

tem por objetivo prover mensagens de controle na comunicação entre 
nós

### DNS - Domain Name Server - 

esse protocolo de aplicação tem por função identificar endereços IPs
e manter uma tabela com os endereços dos caminhos de algumas redes

## Interface de Rede 

Interface de rede é um software e/ou hardware que faz a comunicação
em uma rede de computadores.

As interfaces de rede no Linux localizadas no diretório/dev e a 
maioria é criada dinamicamente pelos softwares quando são requisitadas.

Exemplo: eth0 - Placa de rede Ethernet - cabeada

### Interface de rede loopback

É um tipo especial de interface que permite  fazer conexões com você
mesmo, com ela, você pode testar vários programas de rede sem interfirir
em sua rede padrão, o endereço IP 127.0.0.1 foi escolhido para loopback.
