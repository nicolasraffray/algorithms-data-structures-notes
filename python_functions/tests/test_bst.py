import pytest
from ..lib.data_structures.bst import BinarySearchTreeNode


def test_add_node():
    bst = BinarySearchTreeNode(3)
    bst.add_node(4)
    bst.add_node(1)
    assert bst.right.value == 4
    assert bst.left.value == 1
