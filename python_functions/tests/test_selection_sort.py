import pytest
from ..lib.selection_sort import selection_sort

class TestSelectionSort:
  def test_takes_array_returns_array(self):
    result = selection_sort([5,6,2,2,4,2])
    assert type(result) is list

  def test_sorts_small_array(self):
    result = selection_sort([9,5])
    assert result == [5,9]