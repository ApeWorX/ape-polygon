import pytest
from ape_ethereum.transactions import TransactionType


@pytest.mark.parametrize("type", (0, "0x0"))
def test_create_transaction(networks, type):
    polygon = networks.polygon
    txn = polygon.create_transaction(type=type)
    assert txn.type == TransactionType.STATIC.value


@pytest.mark.parametrize("type", (0, "0x0"))
def test_create_transaction(polygon, type):
    with polygon.local.use_provider("test"):
        txn = polygon.create_transaction(type=type)
        assert txn.type == TransactionType.STATIC.value

