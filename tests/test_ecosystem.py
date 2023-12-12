import pytest
from ape_ethereum.transactions import TransactionType
from ethpm_types.abi import MethodABI


def test_gas_limit(polygon):
    assert polygon.config.local.gas_limit == "max"


# NOTE: None because we want to show the default is DYNAMIC
@pytest.mark.parametrize("tx_type", (None, 2, "0x2"))
def test_create_transaction(polygon, tx_type, eth_tester_provider):
    tx = polygon.create_transaction(type=tx_type)
    assert tx.type == TransactionType.DYNAMIC.value
    assert tx.gas_limit == eth_tester_provider.max_gas


@pytest.mark.parametrize(
    "tx_type",
    (
        TransactionType.STATIC.value,
        TransactionType.DYNAMIC.value,
    ),
)
def test_encode_transaction(tx_type, polygon, eth_tester_provider):
    abi = MethodABI.model_validate(
        {
            "type": "function",
            "name": "fooAndBar",
            "stateMutability": "nonpayable",
            "inputs": [],
            "outputs": [],
        }
    )
    address = "0x274b028b03A250cA03644E6c578D81f019eE1323"
    actual = polygon.encode_transaction(address, abi, sender=address, type=tx_type)
    assert actual.gas_limit == eth_tester_provider.max_gas
