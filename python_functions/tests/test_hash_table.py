import pytest
from ..lib.data_structures.linked_list import LinkedList
from ..lib.data_structures.hash_table import Hash, HashNode


def test_node_has_correct_attributes():
    node = HashNode("string1", 4)
    assert node.value == 4
    assert node.key == "string1"


def test_hash_has_correct_attributes():
    hashe = Hash()
    assert hashe.max_capacity == 100
    assert hashe.size == 0
    assert len(hashe.buckets) == 100


def test_find_value_in_hash():
    hashe = Hash()
    node = HashNode("string", 6)
    hashe.buckets[0] = node
    assert hashe.find("string") == 6
