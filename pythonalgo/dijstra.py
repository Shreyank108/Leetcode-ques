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
pos = nx.spring_layout(G)

# Draw nodes
nx.draw_networkx_nodes(G, pos, node_size=700, node_color='skyblue')

# Draw edges
nx.draw_networkx_edges(G, pos, edgelist=G.edges, edge_color='gray', width=1)

# Draw labels
nx.draw_networkx_labels(G, pos, font_size=8, font_color='black', font_weight='bold', font_family='sans-serif')

# Edge weights
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red')

# Dijkstra's algorithm
shortest_path = nx.shortest_path(G, source='A', target='E', weight='weight')
shortest_path_length = nx.shortest_path_length(G, source='A', target='E', weight='weight')
print(f"Shortest path from A to E: {shortest_path}, Length: {shortest_path_length}")

# Highlight nodes and edges in the shortest path
path_edges = list(zip(shortest_path, shortest_path[1:]))
nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='red', width=2)

nx.draw_networkx_nodes(G, pos, nodelist=shortest_path, node_color='red', node_size=700)

plt.show()
