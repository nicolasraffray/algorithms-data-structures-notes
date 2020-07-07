import pytest
from ..lib.dijkstra import Dijkstra


graph = {'start': {'a': 6, 'b': 2}, 'b': {'a': 3, 'fin': 5}, 'fin': {}}



def test_keeps_track_of_unvisited_nodes():
    d = Dijkstra(graph)
    results = d.get_unvisited_nodes({'a', 'start'})
    assert results == ['b', 'fin']

  
      

