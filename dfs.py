from graph import graph

def dfs(graph, start_node, goal_node):
  stack = []
  visited = set()
  path = {start_node: [start_node]}

  stack.append(start_node)

  while stack:
    current_element = stack.pop()
    visited.add(current_element)

    if current_element == goal_node:
      return path[current_element]

    for neighbor in graph.get(current_element, []):
      if neighbor not in visited:
        stack.append(neighbor)
        path[neighbor] = path[current_element] + [neighbor]
    
  return []

start_node = 'A'
goal_node = 'G'
result_path = dfs(graph, start_node, goal_node)

print(result_path)
