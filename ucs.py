import heapq
from graph import Edge

def ucs(graph, start_node, goal_node):
  queue = [(0, start_node)]
  paths = {start_node: [start_node]}
  path_cost = {start_node: 0}

  while queue:
    current_priority, current_element = heapq.heappop(queue)

    if current_element == goal_node:
      return {'path': paths[current_element], 'cost': path_cost[current_element]}

    for neighbor in graph.get(current_element, []):
      edge = neighbor.element
      new_cost = path_cost[current_element] + neighbor.cost

      if edge not in path_cost or new_cost < path_cost[edge]:
        path_cost[edge] = new_cost
        paths[edge] = paths[current_element] + [edge]
        heapq.heappush(queue, (new_cost, edge))  # Corrected line

  return 'Path Not Found'

# Example usage
graph = {
  'S': [Edge('C', 1), Edge('B', 2), Edge('A', 3)],
  'C': [Edge('G', 20)],
  'B': [Edge('E', 4)],
  'A': [Edge('D', 6)],
  'E': [Edge('G', 8)],
  'D': [Edge('F', 1)],
  'F': [Edge('G', 1)],
}

result = ucs(graph, 'S', 'G')
print(result)
