import pytest
from ..lib.data_structures.linked_list import Node, LinkedList


def test_node():
    node = Node(1)
    assert node.value == 1
    assert node.next == None


def test_linked_list_takes_nodes():
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)

    linked_list = LinkedList()
    linked_list.head = node1
    assert linked_list.head.value == 1

    node1.next = node2
    node2.next = node3

    assert linked_list.head.next.value == 2
