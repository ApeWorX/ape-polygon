from typing import cast

from ape_ethereum.ecosystem import (
    BaseEthereumConfig,
    Ethereum,
    NetworkConfig,
    create_network_config,
)

NETWORKS = {
    # chain_id, network_id
    "mainnet": (137, 137),
    "mumbai": (80001, 80001),
}


class PolygonConfig(BaseEthereumConfig):
    mainnet: NetworkConfig = create_network_config(block_time=2, required_confirmations=1)
    mumbai: NetworkConfig = create_network_config(block_time=2, required_confirmations=1)


class Polygon(Ethereum):
    fee_token_symbol: str = "MATIC"

    @property
    def config(self) -> PolygonConfig:  # type: ignore[override]
        return cast(PolygonConfig, self.config_manager.get_config("polygon"))
