from typing import Type, cast

from ape.api.config import PluginConfig
from ape.api.networks import LOCAL_NETWORK_NAME
from ape.utils import DEFAULT_LOCAL_TRANSACTION_ACCEPTANCE_TIMEOUT
from ape_ethereum.ecosystem import Ethereum, ForkedNetworkConfig, NetworkConfig

NETWORKS = {
    # chain_id, network_id
    "mainnet": (137, 137),
    "mumbai": (80001, 80001),
}


def _create_config(
    required_confirmations: int = 1,
    block_time: int = 2,
    cls: Type[NetworkConfig] = NetworkConfig,
    **kwargs,
) -> NetworkConfig:
    return cls(required_confirmations=required_confirmations, block_time=block_time, **kwargs)


def _create_local_config(**kwargs):
    return _create_config(
        block_time=0,
        default_provider=kwargs.pop("default_provider", None),
        gas_limit="max",
        required_confirmations=0,
        transaction_acceptance_timeout=DEFAULT_LOCAL_TRANSACTION_ACCEPTANCE_TIMEOUT,
        cls=ForkedNetworkConfig if kwargs.pop("use_fork", False) else NetworkConfig,
        **kwargs,
    )


class PolygonConfig(PluginConfig):
    mainnet: NetworkConfig = _create_config()
    mainnet_fork: ForkedNetworkConfig = _create_local_config(use_fork=True)
    mumbai: NetworkConfig = _create_config()
    mumbai_fork: ForkedNetworkConfig = _create_local_config(use_fork=True)
    local: NetworkConfig = _create_local_config(default_provider="test")
    default_network: str = LOCAL_NETWORK_NAME


class Polygon(Ethereum):
    fee_token_symbol: str = "MATIC"

    @property
    def config(self) -> PolygonConfig:  # type: ignore[override]
        return cast(PolygonConfig, self.config_manager.get_config("polygon"))
