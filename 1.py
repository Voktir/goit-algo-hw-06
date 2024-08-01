import random
import matplotlib.pyplot as plt
import networkx as nx

# Function to generate random coordinates within a specified range
def generate_coordinates(min_value, max_value):
  return (random.uniform(min_value, max_value), random.uniform(min_value, max_value))

# Generate vertices with random coordinates
vertices = [generate_coordinates(0, 10) for _ in range(10)]

# Generate edges (connections) between vertices with weights (distances)
edges = []
for i in range(len(vertices)):
  connected_vertices = random.sample(range(len(vertices)), random.randint(1, random.randint(1, 3)))  # Select 1 to (1 to 3 random vertices) random vertices to connect to
  for j in connected_vertices:
    if i != j:  # Avoid self-loops
      weight = random.randint(1, 100)
      edges.append((i, j, weight))

# Створення об'єкта графу NetworkX
G = nx.Graph()

# Додавання вершин
for i, (x, y) in enumerate(vertices):
    G.add_node(i, pos=(x, y))

# Додавання ребер
for u, v, weight in edges:
    G.add_edge(u, v, weight=weight)

# Отримання позицій вершин з атрибутів
pos = nx.get_node_attributes(G, 'pos')

# Малювання графу
nx.draw(G, pos, with_labels=True, font_weight='bold')

# Відображення ваг ребер (опціонально)
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

plt.show()

# Отримуємо данні для проведення аналізу згенерованого графу

if __name__ == "__main__":
    degrees = nx.degree(G)
    degree_centrality = nx.degree_centrality(G)
    closeness_centrality = nx.closeness_centrality(G)
    betweenness_centrality = nx.betweenness_centrality(G)
    print('Кількість вершин', G.number_of_nodes())
    print('Кількість ребер', G.number_of_edges())
    print('Граф сполучений (зв’язний)', nx.is_connected(G))
    print('Середній найкоротший шлях', nx.average_shortest_path_length(G))

    max = 0
    vertex = 0
    for degree in degrees:
        if degree[1] > max:
            max = degree[1]
            vertex = degree[0]
    vertexs = []
    for degree in degrees:
        if degree[1] == max:
            vertexs.append(degree[0])
    print(f'{f'Вершини {vertexs} мають' if len(vertexs)>1 else f'Вершина {vertex} має'} найбільший ступінь {max}')
    max = 0
    vertex = 0
    for i in degree_centrality:
        if degree_centrality[i] > max:
            max = degree_centrality[i]
            vertex = i
    vertexs = []
    for i in degree_centrality:
        if degree_centrality[i] == max:
            vertexs.append(i)
    print(f'{f'Вершини {vertexs} мають' if len(vertexs)>1 else f'Вершина {vertex} має'} найбільший ступінь центральності {max}')
    max = 0
    vertex = 0
    for i in closeness_centrality:
        if closeness_centrality[i] > max:
            max = closeness_centrality[i]
            vertex = i

    vertexs = []
    for i in closeness_centrality:
        if closeness_centrality[i] == max:
            vertexs.append(i)
    print(f'{f'Вершини {vertexs} мають' if len(vertexs)>1 else f'Вершина {vertex} має'} найбільший ступінь близькості {max}')
    max = 0
    vertex = 0
    for i in betweenness_centrality:
        if betweenness_centrality[i] > max:
            max = betweenness_centrality[i]
            vertex = i
    vertexs = []
    for i in betweenness_centrality:
        if betweenness_centrality[i] == max:
            vertexs.append(i)
    print(f'{f'Вершини {vertexs} мають' if len(vertexs)>1 else f'Вершина {vertex} має'} найбільший ступінь посередництва {max}')