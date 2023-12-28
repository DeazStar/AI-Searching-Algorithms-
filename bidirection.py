from graph import bidirectional_graph
from collections import defaultdict , deque
def BidirectionalBFS(graph, start_node , goal_node):
    forward_queue = deque() 
    backward_queue = deque()
    forward_queue.append(start_node)
    backward_queue.append(goal_node)
    forward_visited = set()
    backward_visited = set()
    forward_visited.add(start_node)
    backward_visited.add(goal_node)
    while forward_queue and backward_queue:
        
        forward_node = forward_queue.popleft()
        backward_node = backward_queue.popleft()
        
        if forward_node == goal_node or backward_node == start_node:
            return child
        
        for child in graph[forward_node]:
            if child not in forward_visited:
                forward_visited.add(child)
                forward_queue.append(child)
            if child in backward_node:
                return child
        for child in graph[backward_node]:
            if child not in backward_visited:
                backward_visited.add(child)
                backward_queue.append(child)
            if child in forward_visited:
                return child
    
    return False


start_node = 'A'
goal_node = 'G'
result_path = BidirectionalBFS(bidirectional_graph, start_node, goal_node)
print(result_path)