import pytest
from ..lib.selection_sort import selection_sort

class TestSelectionSort:
  def test_takes_array_returns_array(self):
    result = selection_sort([5,6,2,2,4,2])
    assert type(result) is list

  def test_sorts_small_array(self):
    result = selection_sort([9,5])
    assert result == [5,9]

  def test_sorts_larger_array(self):
    result = selection_sort([9,5,6,3,4])
    assert result == [3,4,5,6,9]

  def test_sorts_larger_array_with_multiple_values(self):
    result = selection_sort([5,2,2,5,2,5,2,5,8,6,8,9])
    assert result == [2,2,2,2,5,5,5,5,6,8,8,9]