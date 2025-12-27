import heapq
import networkx as nx
import matplotlib.pyplot as plt

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    heap = [(0, start)]
    visited = set()

    while heap:
        current_dist, u = heapq.heappop(heap)
        if u in visited:
            continue
        visited.add(u)

        for v, weight in graph[u]:
            if v not in visited:
                new_dist = current_dist + weight
                if new_dist < distances[v]:
                    distances[v] = new_dist
                    heapq.heappush(heap, (new_dist, v))

    return distances

# Приклад графа
graph = {
    "Центр міста": [("Залізничний Вокзал", 3), ("Мій дім", 4), ("Місце роботи", 5), ("Ринок", 2), ("Торгівельний центр", 3)],
    "Залізничний Вокзал": [("Центр міста", 3), ("Мій дім", 2)],
    "Мій дім": [("Центр міста", 4), ("Залізничний Вокзал", 2), ("Ринок", 3)],
    "Місце роботи": [("Центр міста", 5), ("Торгівельний центр", 4), ("Річковий вокзал", 6)],
    "Ринок": [("Центр міста", 2), ("Мій дім", 3), ("Парк", 6)],
    "Торгівельний центр": [("Центр міста", 3), ("Місце роботи", 4), ("Парк", 8)],
    "Парк": [("Ринок", 6), ("Торгівельний центр", 8), ("Річковий вокзал", 5)],
    "Річковий вокзал": [("Місце роботи", 6), ("Парк", 5)]
}

# Обчислюємо найкоротші шляхи
start = "Мій дім"
distances = dijkstra(graph, start)

# Виводимо результат
for node, dist in distances.items():
    print(f"Відстань від {start} до {node}: {dist}")

# Візуалізація графа
G = nx.Graph()
for node, neighbors in graph.items():
    for neighbor, weight in neighbors:
        G.add_edge(node, neighbor, weight=weight)

pos = nx.spring_layout(G, seed=42)
plt.figure(figsize=(10, 8))
nx.draw(G, pos, with_labels=True, node_color="lightblue", node_size=1000, font_size=10, font_weight="bold")
edge_labels = nx.get_edge_attributes(G, "weight")
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=9)
plt.title("Граф міських доріг")
plt.axis("off")
plt.show()
