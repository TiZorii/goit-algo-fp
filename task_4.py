import networkx as nx
import matplotlib.pyplot as plt

class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color  # Додатковий аргумент для збереження кольору вузла

def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.val, pos=(x, y), layer=layer, color=node.color)
        if node.left is not None:
            graph.add_edge(node.val, node.left.val)
            l = 1 / layer
            add_edges(graph, node.left, pos, x-l, y-1, layer+1)
        if node.right is not None:
            graph.add_edge(node.val, node.right.val)
            r = 1 / layer
            add_edges(graph, node.right, pos, x+r, y-1, layer+1)
    return graph

def draw_tree(tree_root):
    graph = nx.DiGraph()
    pos = {}
    tree = add_edges(graph, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]

    plt.figure(figsize=(12, 8))
    nx.draw(tree, pos=nx.get_node_attributes(tree, 'pos'), with_labels=True, arrows=False, node_size=2500, node_color=colors)
    plt.show()

# Функція для перетворення списку у мін-купу
def heapify(arr, n, i):
    smallest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[i] > arr[l]:
        smallest = l

    if r < n and arr[smallest] > arr[r]:
        smallest = r

    if smallest != i:
        arr[i], arr[smallest] = arr[smallest], arr[i]
        heapify(arr, n, smallest)

def build_heap(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

# Функція для побудови дерева з купи
def build_tree_from_heap(arr, index=0):
    if index >= len(arr):
        return None
    node = Node(arr[index])
    node.left = build_tree_from_heap(arr, 2 * index + 1)
    node.right = build_tree_from_heap(arr, 2 * index + 2)
    return node

# Приклад використання
arr = [3, 1, 6, 5, 2, 4]
build_heap(arr)
heap_tree = build_tree_from_heap(arr)

# Відображення дерева
draw_tree(heap_tree)
