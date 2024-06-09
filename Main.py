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



 #Selecionar uma rota específica (exemplo: uma rota específica)
selected_route = '561787'  # Substitua com o ID da rota real que você deseja usar

# Filtrar as viagens dessa rota
selected_trips = trips[trips['route_id'] == selected_route]

# Filtrar os horários dessas viagens
selected_stop_times = stop_times[stop_times['trip_id'].isin(selected_trips['trip_id'])]

# Filtrar as paradas dessas viagens
selected_stops = stops[stops['stop_id'].isin(selected_stop_times['stop_id'])]

# Criar o grafo
G = nx.DiGraph()  # Grafo dirigido

# Adicionar nós (paradas)
for index, row in stops.iterrows():
    G.add_node(row['stop_id'], name=row['stop_name'])

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

# # Selecionar duas rotas específicas (exemplo: duas rotas específicas)
# selected_routes = ['561787', '561788']  # Substitua com os IDs das rotas reais que você deseja usar

# # Filtrar as viagens dessas rotas
# selected_trips = trips[trips['route_id'].isin(selected_routes)]

# # Filtrar os horários dessas viagens
# selected_stop_times = stop_times[stop_times['trip_id'].isin(selected_trips['trip_id'])]

# # Filtrar as paradas dessas viagens
# selected_stops = stops[stops['stop_id'].isin(selected_stop_times['stop_id'])]

# # Criar o grafo
# G = nx.DiGraph()  # Grafo dirigido

# # Adicionar nós (paradas) filtradas
# for index, row in selected_stops.iterrows():
#     G.add_node(row['stop_id'], name=row['stop_name'])

# # Adicionar arestas (conexões entre paradas) filtradas
# for trip_id, trip_data in selected_stop_times.groupby('trip_id'):
#     trip_data_sorted = trip_data.sort_values(by='stop_sequence')
#     previous_stop = None
#     for index, row in trip_data_sorted.iterrows():
#         if previous_stop is not None:
#             G.add_edge(previous_stop['stop_id'], row['stop_id'], trip_id=trip_id, arrival_time=row['arrival_time'])
#         previous_stop = row

# # Visualizar o grafo (simples)
# plt.figure(figsize=(8, 8))
# pos = nx.spring_layout(G)  # Layout para organizar o grafo de forma visualmente agradável
# nx.draw(G, pos, with_labels=True, node_size=500, font_size=10)
# plt.show()
