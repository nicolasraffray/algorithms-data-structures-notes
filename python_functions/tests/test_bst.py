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


def test_seearch_tree(generate_tree):
    bst = generate_tree
    value1 = bst.search(15)
    value2 = bst.search(1)
    value3 = bst.search(67)

    assert value1 == 15
    assert value2 == 1
    assert value3 == False


def test_find_min(generate_tree):
    bst = generate_tree
    assert bst.find_min() == 1


def test_find_max(generate_tree):
    bst = generate_tree
    assert bst.find_max() == 25


def test_calculate_tree_sum(generate_tree):
    bst = generate_tree
    assert bst.calculate_tree_sum() == 78


def test_pre_order_traversal(generate_tree):
    bst = generate_tree
    assert bst.pre_order_traversal() == [4, 2, 1, 3, 15, 5, 25, 23]


def test_post_order_traversal(generate_tree):
    bst = generate_tree
    assert bst.post_order_traversal() == [1, 3, 2, 5, 23, 25, 15, 4]


def test_delete(generate_tree):
    bst = generate_tree
    bst.delete(15)
    bst.delete(3)
    assert bst.return_all_elements() == [1, 2, 4, 5, 23, 25]
