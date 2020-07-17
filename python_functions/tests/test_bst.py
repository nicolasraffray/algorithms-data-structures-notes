import pytest
from ..lib.data_structures.bst import BinarySearchTreeNode


@pytest.fixture(scope='module')
def generate_tree():
    bst = BinarySearchTreeNode(4)
    array = [15, 2, 3, 25, 23, 5, 1]
    for i in array:
        bst.add_node(i)
    return bst


def test_add_node():
    bst = BinarySearchTreeNode(3)
    bst.add_node(4)
    bst.add_node(1)
    assert bst.right.value == 4
    assert bst.left.value == 1


def test_print_all_nodes(generate_tree):
    bst = generate_tree
    all_ordered_values = bst.return_all_elements()
    assert all_ordered_values == [1, 2, 3, 4, 5, 15, 23, 25]
