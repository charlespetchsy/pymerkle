import pytest
import os
import json

from pymerkle.core import MerkleTree
from pymerkle.exceptions import WrongJSONFormat

# This test does not produce export files.

# Make tree and export to JSON string
tree = MerkleTree(*['%d-th record' % i for i in range(12)])
json_output = json.loads(tree.toJSONString())
invalid_json = dict(
    foo_header='random_string',
    bar_hashes='random_hash'
)


def test_loadFromJSON():
    assert tree.serialize() == MerkleTree.loadFromJSON(json_output).serialize()

def test_WrongJSONFormat_with_loadFromJSON():
    with pytest.raises(WrongJSONFormat):
        MerkleTree.loadFromJSON(invalid_json)
