from ape_ethereum.transactions import TransactionType

from ape_polygon.ecosystem import PolygonConfig


def test_gas_limit(polygon):
    assert polygon.config.local.gas_limit == "max"


def test_default_transaction_type(polygon):
    assert polygon.config.mainnet.default_transaction_type == TransactionType.DYNAMIC


def test_mainnet_fork_not_configured():
    obj = PolygonConfig.model_validate({})
    assert obj.mainnet_fork.required_confirmations == 0


def test_mainnet_fork_configured():
    data = {"mainnet_fork": {"required_confirmations": 555}}
    obj = PolygonConfig.model_validate(data)
    assert obj.mainnet_fork.required_confirmations == 555


def test_custom_network():
    data = {"apenet": {"required_confirmations": 333}}
    obj = PolygonConfig.model_validate(data)
    assert obj.apenet.required_confirmations == 333
