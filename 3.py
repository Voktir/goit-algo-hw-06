# Функція для алгоритму Дейкстри
def dijkstra(graph, start):
    distances = {vertex: float('infinity') for vertex in graph.nodes}
    distances[start] = 0
    unvisited = set(graph.nodes)
    previous_nodes = {vertex: None for vertex in graph.nodes}
    
    while unvisited:
        current_vertex = min(unvisited, key=lambda vertex: distances[vertex])
        
        if distances[current_vertex] == float('infinity'):
            break
        
        for neighbor in graph.neighbors(current_vertex):
            edge_weight = graph[current_vertex][neighbor]['weight']
            new_distance = distances[current_vertex] + edge_weight
            
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                previous_nodes[neighbor] = current_vertex
        
        unvisited.remove(current_vertex)
    
    return distances, previous_nodes

graph = __import__('1')
start = 0
# Виконання алгоритму Дейкстри
distances, previous_nodes = dijkstra(graph.G, start)
    
# Вивід результатів алгоритму Дейкстри
print("\nРезультати алгоритму Дейкстри:")
for node, distance in distances.items():
    print(f"Відстань від {start} до {node}: {distance}")