from collections import defaultdict, deque

class GraphUtil:
  def create_adj_list(inputs, nodes_extractor_func):
    adj_list = defaultdict(set)
    for input in inputs:
      from_node, to_node = nodes_extractor_func(input)
      adj_list[from_node].add(to_node)
    return adj_list

  def topo_sort(adj_list):
    seen = set()
    queue = deque()
    nodes = list(adj_list.keys())

    def dfs(node):
      seen.add(node)
      for child in adj_list[node]:
        if child not in seen:
          dfs(child)
      queue.appendleft(node)

    for node in nodes:
      if node in seen:
        continue
      dfs(node)

    return list(queue)
