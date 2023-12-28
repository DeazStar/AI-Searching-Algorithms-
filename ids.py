from graph import graph
from dls import dls

def ids(graph, start_node, goal_node):
  depth_limit = 0

  while True:
    result_path = dls(graph, start_node, goal_node, depth_limit)

    if result_path:
      return result_path
    else:
      depth_limit += 1

start_node = 'A'
goal_node = 'G'
result_path = ids(graph, start_node, goal_node)

print(result_path)
