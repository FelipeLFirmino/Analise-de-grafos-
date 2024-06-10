import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

# Diretório onde os arquivos GTFS estão localizados
directory = 'Data/'

# Carregar os arquivos GTFS
stops = pd.read_csv(f'{directory}stops.txt')
stop_times = pd.read_csv(f'{directory}stop_times.txt')
routes = pd.read_csv(f'{directory}routes.txt')
trips = pd.read_csv(f'{directory}trips.txt')

# Criar o grafo
G = nx.DiGraph()  # Grafo dirigido


# Adicionar arestas (conexões entre paradas)
for trip_id, trip_data in stop_times.groupby('trip_id'):
    trip_data_sorted = trip_data.sort_values(by='stop_sequence')
    previous_stop = None
    for index, row in trip_data_sorted.iterrows():
        if previous_stop is not None:
            G.add_edge(previous_stop['stop_id'], row['stop_id'], trip_id=trip_id, arrival_time=row['arrival_time'])
        previous_stop = row

# Função para encontrar o caminho mais curto usando o algoritmo de Dijkstra
def find_shortest_path(graph, source, target):
    return nx.dijkstra_path(graph, source, target)

# Definir paradas de origem e destino para o caminho mais curto
source_stop = 'S1'
target_stop = 'S3'

# Encontrar o caminho mais curto
shortest_path = find_shortest_path(G, source_stop, target_stop)
print("Shortest Path:", shortest_path)

# Destacar as arestas do caminho mais curto
edge_colors = ['red' if (u, v) in zip(shortest_path[:-1], shortest_path[1:]) else 'black' for u, v in G.edges()]

# Visualizar o grafo com o caminho mais curto destacado
plt.figure(figsize=(12, 12))
pos = nx.spring_layout(G, k=0.3, iterations=100)  # Layout ajustado para melhor visualização
nx.draw(G, pos, with_labels=True, node_size=500, font_size=10, node_color='skyblue', edge_color=edge_colors, font_color='black', arrowsize=20)
nx.draw_networkx_labels(G, pos, labels=nx.get_node_attributes(G, 'name'))
plt.show()




# # #codigo base que le todas as informações(mas é invivavel)
# import pandas as pd
# import networkx as nx
# import matplotlib.pyplot as plt

# # Diretório onde os arquivos GTFS estão localizados
# directory = 'Data/'

# # Carregar os arquivos GTFS
# stops = pd.read_csv(f'{directory}stops.txt')
# stop_times = pd.read_csv(f'{directory}stop_times.txt')
# routes = pd.read_csv(f'{directory}routes.txt')
# trips = pd.read_csv(f'{directory}trips.txt')

# # Criar o grafo
# G = nx.DiGraph()  # Grafo dirigido


# # Adicionar arestas (conexões entre paradas)
# for trip_id, trip_data in stop_times.groupby('trip_id'):
#     trip_data_sorted = trip_data.sort_values(by='stop_sequence')
#     previous_stop = None
#     for index, row in trip_data_sorted.iterrows():
#         if previous_stop is not None:
#             G.add_edge(previous_stop['stop_id'], row['stop_id'], trip_id=trip_id, arrival_time=row['arrival_time'])
#         previous_stop = row

# # Visualizar o grafo (simples)
# plt.figure(figsize=(8, 8))
# pos = nx.spring_layout(G)
# nx.draw(G, pos, with_labels=True, node_size=500, font_size=10)
# plt.show()
