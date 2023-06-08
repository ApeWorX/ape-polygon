from typing import Optional, cast

from ape.api.config import PluginConfig
from ape.api.networks import LOCAL_NETWORK_NAME
from ape_ethereum.ecosystem import Ethereum, NetworkConfig

NETWORKS = {
    # chain_id, network_id
    "mainnet": (137, 137),
    "mumbai": (80001, 80001),
}


def _create_network_config(
    required_confirmations: int = 1, block_time: int = 2, **kwargs
) -> NetworkConfig:
    return NetworkConfig(
        required_confirmations=required_confirmations, block_time=block_time, **kwargs
    )


def _create_local_config() -> NetworkConfig:
    return _create_network_config(
        required_confirmations=0,
        block_time=0,
        default_provider="test",
        gas_limit="max",
    )


class PolygonConfig(PluginConfig):
    mainnet: NetworkConfig = _create_network_config()
    mainnet_fork: NetworkConfig = _create_local_config()
    mumbai: NetworkConfig = _create_network_config()
    mumbai_fork: NetworkConfig = _create_local_config()
    local: NetworkConfig = _create_local_config()
    default_network: str = LOCAL_NETWORK_NAME


class Polygon(Ethereum):
    @property
    def config(self) -> PolygonConfig:  # type: ignore[override]
        return cast(PolygonConfig, self.config_manager.get_config("polygon"))
