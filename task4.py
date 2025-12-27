import uuid
import networkx as nx
import matplotlib.pyplot as plt
import heapq

class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())

def heap_to_tree(heap_array):
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

def draw_heap_tree(heap_array):
    root = heap_to_tree(heap_array)
    if root is None:
        return
    tree = nx.DiGraph()
    pos = {root.id: (0, 0)}
    tree = add_edges(tree, root, pos)
    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}
    plt.figure(figsize=(10, 6))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()

# Приклад використання:
heap = [10, 5, 6, 2, 4, 8, 9]
draw_heap_tree(heap)

