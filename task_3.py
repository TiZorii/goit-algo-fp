import heapq

class Graph:
    def __init__(self):
        self.edges = {}

    def add_edge(self, from_node, to_node, weight):
        if from_node not in self.edges:
            self.edges[from_node] = []
        self.edges[from_node].append((to_node, weight))

    def dijkstra(self, start):
        shortest_paths = {start: (None, 0)}
        priority_queue = [(0, start)]
        heapq.heapify(priority_queue)

        while priority_queue:
            (current_distance, current_node) = heapq.heappop(priority_queue)

            if current_distance > shortest_paths[current_node][1]:
                continue

            for neighbor, weight in self.edges.get(current_node, []):
                distance = current_distance + weight
                if neighbor not in shortest_paths or distance < shortest_paths[neighbor][1]:
                    shortest_paths[neighbor] = (current_node, distance)
                    heapq.heappush(priority_queue, (distance, neighbor))

        return shortest_paths

# Приклад використання
graph = Graph()
graph.add_edge('A', 'B', 1)
graph.add_edge('B', 'C', 2)
graph.add_edge('A', 'C', 4)
graph.add_edge('C', 'D', 1)

shortest_paths = graph.dijkstra('A')
print(shortest_paths)
