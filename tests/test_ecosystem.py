import pytest
from ape_ethereum.transactions import TransactionType
from ethpm_types.abi import MethodABI


def test_gas_limit(polygon):
    assert polygon.config.local.gas_limit == "max"


# NOTE: None because we want to show the default is DYNAMIC
@pytest.mark.parametrize("type", (None, 2, "0x2"))
def test_create_transaction(polygon, type, eth_tester_provider):
    tx = polygon.create_transaction(type=type)
    assert tx.type == TransactionType.DYNAMIC.value
    assert tx.gas_limit == eth_tester_provider.max_gas


@pytest.mark.parametrize(
    "type_",
    (
        TransactionType.STATIC.value,
        TransactionType.DYNAMIC.value,
    ),
)
def test_encode_transaction(type_, polygon, eth_tester_provider):
    abi = MethodABI.parse_obj(
        {
            "type": "function",
            "name": "fooAndBar",
            "stateMutability": "nonpayable",
            "inputs": [],
            "outputs": [],
        }
    )
    address = "0x274b028b03A250cA03644E6c578D81f019eE1323"
    actual = polygon.encode_transaction(address, abi, sender=address, type=type_)
    assert actual.gas_limit == eth_tester_provider.max_gas
