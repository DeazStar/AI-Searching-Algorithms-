graph = {
  'A': ['B', 'C'],
  'B': ['D', 'E'],
  'C': ['F', 'G'],
  'D': [],
  'E': [],
  'F': [],
  'G': [],
}

class Edge:
  def __init__(self, element, cost):
    self.element = element
    self.cost = cost