

class Dijkstra:

  def __init__(self, graph):
    self.graph = graph 
    self.costs = {}
  
  def get_unvisited_nodes(self, visited):
    unvisited = []
    for i in list(self.graph.keys()):
      if i not in visited:
        unvisited.insert(len(unvisited), i)
    return unvisited

  def generate_costs(self):
    for nested in self.graph.values():
      if nested is int:
        nested = float('inf')
      while type(nested) is dict and bool(nested):
        self.generate_costs()
    

