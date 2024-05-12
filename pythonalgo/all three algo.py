import networkx as nx
import matplotlib.pyplot as plt

# Create a directed graph
G = nx.DiGraph()

# Nodes
G.add_nodes_from(['A', 'B', 'C', 'D', 'E'])

# Edges
G.add_edge('A', 'B', weight=2)
G.add_edge('A', 'C', weight=1)
G.add_edge('B', 'C', weight=3)
G.add_edge('B', 'D', weight=2)
G.add_edge('C', 'D', weight=1)
G.add_edge('D', 'E', weight=3)

# Visualize
fig, axs = plt.subplots(1, 3, figsize=(20, 5))

# Common position for all plots
common_pos = {'A': (0, 0), 'B': (1, 1), 'C': (2, 0), 'D': (3, 1), 'E': (4, 0)}

# Floyd-Warshall Algorithm
axs[0].set_title('Floyd-Warshall Algorithm')
pos_fw = common_pos
nx.draw(G, pos_fw, ax=axs[0], with_labels=True, node_size=700, font_size=8, font_color='black', font_weight='bold', edge_color='gray', font_family='sans-serif')
edge_labels_fw = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos_fw, edge_labels=edge_labels_fw)

all_pairs_shortest_paths_fw = dict(nx.all_pairs_shortest_path_length(G))
shortest_path_fw = nx.shortest_path(G, source='A', target='E', weight='weight')
path_edges_fw = list(zip(shortest_path_fw, shortest_path_fw[1:]))
nx.draw_networkx_edges(G, pos_fw, edgelist=path_edges_fw, edge_color='red', width=2)
nx.draw_networkx_nodes(G, pos_fw, nodelist=shortest_path_fw, node_color='red', node_size=700)
axs[0].set_xticks([])

# Dijkstra's Algorithm
axs[1].set_title("Dijkstra's Algorithm")
pos_dijkstra = common_pos
nx.draw(G, pos_dijkstra, ax=axs[1], with_labels=True, node_size=700, font_size=8, font_color='black', font_weight='bold', edge_color='gray', font_family='sans-serif')
edge_labels_dijkstra = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos_dijkstra, edge_labels=edge_labels_dijkstra)
shortest_path_dijkstra = nx.shortest_path(G, source='A', target='E', weight='weight')
path_edges_dijkstra = list(zip(shortest_path_dijkstra, shortest_path_dijkstra[1:]))
nx.draw_networkx_edges(G, pos_dijkstra, edgelist=path_edges_dijkstra, edge_color='red', width=2)
nx.draw_networkx_nodes(G, pos_dijkstra, nodelist=shortest_path_dijkstra, node_color='red', node_size=700)
axs[1].set_xticks([])

# Bellman-Ford Algorithm
axs[2].set_title('Bellman-Ford Algorithm')
pos_bf = common_pos
nx.draw(G, pos_bf, ax=axs[2], with_labels=True, node_size=700, font_size=8, font_color='black', font_weight='bold', edge_color='gray', font_family='sans-serif')
edge_labels_bf = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos_bf, edge_labels=edge_labels_bf)
shortest_path_bf = nx.bellman_ford_path(G, source='A', target='E', weight='weight')
path_edges_bf = list(zip(shortest_path_bf, shortest_path_bf[1:]))
nx.draw_networkx_edges(G, pos_bf, edgelist=path_edges_bf, edge_color='red', width=2)
nx.draw_networkx_nodes(G, pos_bf, nodelist=shortest_path_bf, node_color='red', node_size=700)
axs[2].set_xticks([])

plt.show()
