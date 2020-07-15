import pytest
from ..lib.data_structures.linked_list import Node, LinkedList


@pytest.fixture(scope="module", autouse=True)
def generate_list():
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)

    linked_list = LinkedList()
    linked_list.head = node1
    node1.next = node2
    node2.next = node3

    return [linked_list, node1]


def test_node(generate_list):
    node1 = generate_list[1]
    assert node1.value == 1


def test_linked_list_takes_nodes(generate_list):
    linked_list = generate_list[0]
    assert linked_list.head.value == 1
    assert linked_list.head.next.value == 2


def test_print_node_list_values(generate_list):
    linked_list = generate_list[0]
    string = linked_list.get_list()
    assert string == "1 2 3 "


def test_insertion_at_start(generate_list):
    linked_list = generate_list[0]
    linked_list.insert_at_start(0)
    assert linked_list.get_list() == "0 1 2 3 "


def test_insert_at_end(generate_list):
    linked_list = generate_list[0]
    linked_list.insert_at_end(4)
    assert linked_list.get_list() == '0 1 2 3 4 '


def test_insert_between(generate_list):
    linked_list = generate_list[0]
    linked_list.insert_between(2.5, 2)
    assert linked_list.get_list() == '0 1 2 2.5 3 4 '


def test_del_node(generate_list):
    linked_list = generate_list[0]
    linked_list.del_node(2.5)
    assert linked_list.get_list() == '0 1 2 3 4 '
    linked_list.del_node(0)
    assert linked_list.get_list() == '1 2 3 4 '
