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


def test_inserts_key_value_pair():
    hashe = Hash()
    hashe.insert("first key", 9)
    node = [x for x in hashe.buckets if x is not None][0]
    assert node.key == "first key"
    assert node.value == 9


def test_find_value_in_hash():
    hashe = Hash()
    hashe.insert("new key", 7)
    assert hashe.find("new key") == 7
