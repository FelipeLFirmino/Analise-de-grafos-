# import pandas as pd
# import networkx as nx
# import matplotlib.pyplot as plt

# # Exemplo simplificado de dados
# stops_data = {
#     'stop_id': ['A', 'B', 'C', 'D'],
#     'stop_name': ['Stop A', 'Stop B', 'Stop C', 'Stop D']
# }
# stop_times_data = {
#     'trip_id': ['T1', 'T1', 'T2', 'T2'],
#     'stop_id': ['A', 'B', 'C', 'D'],
#     'stop_sequence': [1, 2, 1, 2],
#     'arrival_time': ['08:00:00', '08:10:00', '09:00:00', '09:15:00']
# }
# routes_data = {
#     'route_id': ['R1', 'R2'],
#     'route_name': ['Route 1', 'Route 2']
# }
# trips_data = {
#     'trip_id': ['T1', 'T2'],
#     'route_id': ['R1', 'R2']
# }

# stops = pd.DataFrame(stops_data)
# stop_times = pd.DataFrame(stop_times_data)
# routes = pd.DataFrame(routes_data)
# trips = pd.DataFrame(trips_data)

# # Criar o grafo
# G = nx.DiGraph()  # Grafo dirigido

# # Adicionar nós (paradas)
# for index, row in stops.iterrows():
#     G.add_node(row['stop_id'], name=row['stop_name'])

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



#codigo base que le todas as informações(mas é invivavel)
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

# Visualizar o grafo (simples)
plt.figure(figsize=(8, 8))
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_size=500, font_size=10)
plt.show()
