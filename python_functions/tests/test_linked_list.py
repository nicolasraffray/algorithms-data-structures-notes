import pytest
from ..lib.data_structures.linked_list import Node


def test_node():
    node = Node(1)
    assert node.value == 1
    assert node.next == None
