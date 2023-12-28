from graph import graph
from collections import deque

def bfs(graph, start_node, goal_node):
  queue = deque()
  visited = set()
  path = {start_node: [start_node]}

  if start_node == goal_node: 
    return path

  queue.append(start_node)

  while queue:
    current_node = queue.popleft()
    visited.add(current_node)

    for neighbor in graph.get(current_node, []):
      if neighbor not in visited:
        path[neighbor] = path[current_node] + [neighbor]

        if neighbor == goal_node:
          return path[neighbor]

        queue.append(neighbor)

  return []

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [],
    'E': [],
    'F': [],
    'G': [],
}

start_node = 'A'
goal_node = 'G'
result_path = bfs(graph, start_node, goal_node)

print(result_path)