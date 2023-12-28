from graph import graph

def dls(graph, start_node, goal_node, depth_limit):
  stack = []
  visited = set()
  path = {start_node: [start_node]}

  stack.append((start_node, 0))

  while stack:
    current_node, current_depth = stack.pop()
    visited.add(current_node)

    if current_node == goal_node:
      return path[current_node]

    if current_depth < depth_limit:
      for neighbor in graph.get(current_node, []):
        if neighbor not in visited:
          stack.append((neighbor, current_depth + 1))
          path[neighbor] = path[current_node] + [neighbor]
    else:
      return []

  return []

start_node = 'A'
goal_node = 'G'
depth_limit = 2
result_path = dls(graph, start_node, goal_node, depth_limit)

print(result_path)
