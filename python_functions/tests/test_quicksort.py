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

  def test_larger_array_usinging_recursion(self):
    array = [4,6,5,3,2,8,9]
    result = quick_sort(array)
    assert result == [2,3,4,5,6,8,9]





