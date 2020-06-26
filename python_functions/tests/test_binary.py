import pytest
from ..lib.binary_search import binary_search

class TestBinarySearch:

  def test_takesArray(self):
    array = [1,1,2,3,5]
    result = binary_search(array)
    print(result)
    assert type(result) is list


# test = BinarySearch()
# test.takesArray()

