import heapq

def heuristic(node):
  return graph[node]['heuristic']

def best_first_search(graph, start_node, goal_node):
  queue = [(heuristic(start_node), start_node)]
  visited = set()
  path = {start_node: [start_node]}

  while queue:
    _, current_node = heapq.heappop(queue)
    visited.add(current_node)

    if current_node == goal_node:
      return path[current_node]

    neighbors = graph[current_node]['neighbors']

    for neighbor in neighbors:
      if neighbor not in visited:
        path[neighbor] = path[current_node] + [neighbor]
        heapq.heappush(queue, (heuristic(neighbor), neighbor))

  return []

# Example usage
graph = {
  'S': {'neighbors': ['A', 'B'], 'heuristic': 15},
  'A': {'neighbors': ['C', 'D'], 'heuristic': 12},
  'C': {'neighbors': [], 'heuristic': 7},
  'D': {'neighbors': [], 'heuristic': 3},
  'B': {'neighbors': ['E', 'F'], 'heuristic': 4},
  'E': {'neighbors': ['H'], 'heuristic': 8},
  'F': {'neighbors': ['I', 'G'], 'heuristic': 2},
  'I': {'neighbors': [], 'heuristic': 9},
  'G': {'neighbors': [], 'heuristic': 0},
  'H': {'neighbors': [], 'heuristic': 4},
}

start_node = 'S'
goal_node = 'G'

result_path = best_first_search(graph, start_node, goal_node)
print(result_path)
