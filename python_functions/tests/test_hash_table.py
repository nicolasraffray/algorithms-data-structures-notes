import pytest
from ..lib.data_structures.linked_list import LinkedList
from ..lib.data_structures.hash_table import HashNode, HashNode


def test_node_has_correct_attributes():
    node = HashNode("string1", 4)
    assert node.value == 4
    assert node.key == "string1"
