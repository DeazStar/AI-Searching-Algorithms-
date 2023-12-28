import heapq
from graph import Edge

def heuristic(node, goal_node):
  return graph[node]['heuristic']

def a_star_search(graph, start_node, goal_node):
  queue = [(0 + heuristic(start_node, goal_node), 0, start_node)]
  visited = set()
  path = {start_node: [start_node]}
  cost_so_far = {start_node: 0}

  while queue:
    _, actual_cost, current_node = heapq.heappop(queue)
    visited.add(current_node)

    if current_node == goal_node:
      return {'path': path[current_node], 'cost': cost_so_far[current_node]}

    neighbors = graph[current_node]['neighbors']

    for neighbor_edge in neighbors:
      neighbor = neighbor_edge.element
      edge_cost = neighbor_edge.cost

      new_cost = cost_so_far[current_node] + edge_cost
      if neighbor not in visited or new_cost < cost_so_far[neighbor]:
        cost_so_far[neighbor] = new_cost
        priority = new_cost + heuristic(neighbor, goal_node)
        heapq.heappush(queue, (priority, new_cost, neighbor))
        path[neighbor] = path[current_node] + [neighbor]

  return []

# Example usage
graph = {
  'S': {'neighbors': [Edge('A', 1), Edge('B', 2)], 'heuristic': 15},
  'A': {'neighbors': [Edge('C', 3), Edge('D', 2)], 'heuristic': 12},
  'C': {'neighbors': [], 'heuristic': 7},
  'D': {'neighbors': [], 'heuristic': 3},
  'B': {'neighbors': [Edge('E', 4), Edge('F', 2)], 'heuristic': 4},
  'E': {'neighbors': [Edge('H', 8)], 'heuristic': 8},
  'F': {'neighbors': [Edge('I', 1), Edge('G', 4)], 'heuristic': 2},
  'I': {'neighbors': [], 'heuristic': 9},
  'G': {'neighbors': [], 'heuristic': 0},
  'H': {'neighbors': [], 'heuristic': 4},
}

start_node = 'S'
goal_node = 'G'

result = a_star_search(graph, start_node, goal_node)
print(result)
