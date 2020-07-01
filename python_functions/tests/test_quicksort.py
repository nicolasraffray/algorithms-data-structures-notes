import pytest
from ..lib.quick_sort import quick_sort

class TestQuickSort: 

  def test_returns_array_less_tha_2(self):
    array = [1]
    result = quick_sort(array)
    assert result == [1]

  def test_can_switch_two_unsorted_elements(self):
    array = [2,1]
    result = quick_sort(array)
    assert result ==  [1,2]





