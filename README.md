## Descrição do Projeto

Este projeto visa criar um grafo visual representando as paradas e conexões de duas rotas de transporte público utilizando dados GTFS (General Transit Feed Specification). O objetivo principal é fornecer uma visualização clara e compreensível das rotas selecionadas, ajudando na análise e compreensão da rede de transporte. Além disso, o projeto inclui a implementação do algoritmo de Dijkstra para encontrar o caminho mais curto entre duas paradas específicas.
- O GTFS foi retirado de: https://gtfs.pro/en/saudi-arabia/KAUST-Transportation-Services/kaust-transportation-services

## Funcionalidades

- Carregar dados GTFS de uma cidade específica.
- Filtrar e selecionar duas rotas específicas - que serão definidas no código.
- Construir um grafo dirigido representando as paradas e conexões das rotas selecionadas.
- Implementar o algoritmo de Dijkstra para encontrar o caminho mais curto entre duas paradas.
- Visualizar o grafo utilizando a biblioteca matplotlib.
- Gera uma visualização do grafo com o caminho mais curto destacado.
- Diferencia as paradas e conexões usando cores específicas para facilitar a interpretação:
    Verde: Ponto inicial.
    Azul: Ponto final.
    Amarelo: Paradas que fazem parte do caminho mais curto.
    Azul claro: Paradas não relacionadas ao caminho mais curto.
    Vermelho: Conexões (arestas) que fazem parte do caminho mais curto.
    Preto: Conexões (arestas) que não fazem parte do caminho mais curto.
  
## Dependências

Este projeto requer as seguintes bibliotecas Python:

pandas: Para manipulação e análise de dados.
networkx: Para criação e manipulação de grafos.
matplotlib: Para visualização do grafo.

## Instalação

Para instalar as dependências necessárias, execute os seguintes comandos:

bash

Copy code

pip install pandas

pip install networkx

pip install matplotlib

## Como Executar o Projeto
Clone o Repositório

Clone o repositório para o seu computador:

bash

Copy code
git clone https://github.com/seu-usuario/gtfs-route-visualization.git

cd gtfs-route-visualization

Prepare os Dados GTFS

Coloque os arquivos GTFS (stops.txt, stop_times.txt, routes.txt, trips.txt) na pasta Data/.

Execute o Código com o comando "Python Main.py"  

### Agradecimentos
Agradecemos às comunidades de pandas, networkx e matplotlib pelo desenvolvimento dessas bibliotecas essenciais para a ciência de dados e análise de grafos.

