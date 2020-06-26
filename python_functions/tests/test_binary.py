import pytest
from ..lib.binary_search import binary_search

class TestBinarySearch:

  def test_takes_array_and_returns_int(self):
    array = [1,1,2,3,5]
    result = binary_search(array, 3)
    
    assert type(result) is int or None 

  def test_simple_list(self):
    array = [1,2,4]
    item = 2
    result = binary_search(array, item)
    assert result == 1


