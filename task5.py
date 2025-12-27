import uuid
import heapq
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


class Node:
    def __init__(self, key, color="#1296F0"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())


def build_heap_tree(heap_array):
    if not heap_array:
        return None
    nodes = [Node(val) for val in heap_array]
    for i in range(len(heap_array)):
        left_idx = 2 * i + 1
        right_idx = 2 * i + 2
        if left_idx < len(heap_array):
            nodes[i].left = nodes[left_idx]
        if right_idx < len(heap_array):
            nodes[i].right = nodes[right_idx]
    return nodes[0]


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph


# --------- ОБХОДИ БЕЗ РЕКУРСІЇ ---------

def bfs_traversal(root):
    order = []
    queue = [root]
    while queue:
        node = queue.pop(0)
        order.append(node)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return order


def dfs_traversal(root):
    order = []
    stack = [root]
    while stack:
        node = stack.pop()
        order.append(node)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return order


# --------- ДОПОМІЖНІ ФУНКЦІЇ ДЛЯ КОЛЬОРІВ ---------

def make_color_scale(order_index, total):
    """Градієнт від темного до світлого синього у форматі #RRGGBB."""
    intensity = int(40 + (200 * order_index / total))  # 40..240
    return f"#{intensity:02x}{intensity:02x}ff"


# --------- АНІМАЦІЯ ОБХОДУ ---------

def animate_traversal(root, traversal_nodes, title):
    # Створюємо граф і фіксуємо позиції один раз
    G = nx.DiGraph()
    pos = {root.id: (0, 0)}
    add_edges(G, root, pos)

    # Всі вузли у вигляді списку id
    node_ids = list(G.nodes)

    fig, ax = plt.subplots(figsize=(10, 6))

    total = len(traversal_nodes)

    def init():
        # стартові кольори (усі однакові)
        colors = ["#1296F0" for _ in node_ids]
        labels = {n: G.nodes[n]["label"] for n in node_ids}
        nx.draw(G, pos=pos, labels=labels,
                arrows=False, node_size=2500,
                node_color=colors, ax=ax)
        ax.set_title(title + " – крок 0")
        return []

    def update(frame):
        # frame – номер кроку (0..total-1), фарбуємо всі відвідані до цього вузли
        visited = traversal_nodes[: frame + 1]
        color_map = []
        for n in node_ids:
            # шукаємо, чи був вузол відвіданий і на якому кроці
            idx = next((i for i, node in enumerate(visited) if node.id == n), None)
            if idx is None:
                color_map.append("#dddddd")  # ще не відвідано
            else:
                color_map.append(make_color_scale(idx, total))

        ax.clear()
        labels = {n: G.nodes[n]["label"] for n in node_ids}
        nx.draw(G, pos=pos, labels=labels,
                arrows=False, node_size=2500,
                node_color=color_map, ax=ax)
        ax.set_title(f"{title} – крок {frame + 1}")
        return []

    anim = FuncAnimation(
        fig,
        update,
        init_func=init,
        frames=total,
        interval=800,   # мс між кроками
        repeat=False,
    )

    plt.show()


def visualize_heap_traversals(data):
    heap = data.copy()
    heapq.heapify(heap)
    root = build_heap_tree(heap)

    # BFS
    bfs_nodes = bfs_traversal(root)
    animate_traversal(root, bfs_nodes, "Візуалізація обходу бінарного дерева (BFS)")

    # DFS
    dfs_nodes = dfs_traversal(root)
    animate_traversal(root, dfs_nodes, "Візуалізація обходу бінарного дерева (DFS)")
if __name__ == "__main__":
    heap_data = [10, 5, 6, 2, 4, 8, 9]
    visualize_heap_traversals(heap_data)
