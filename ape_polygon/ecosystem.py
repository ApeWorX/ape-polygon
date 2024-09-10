from typing import ClassVar, cast

from ape_ethereum.ecosystem import (
    BaseEthereumConfig,
    Ethereum,
    NetworkConfig,
    create_network_config,
)

NETWORKS = {
    # chain_id, network_id
    "mainnet": (137, 137),
    "amoy": (80002, 80002),
}


class PolygonConfig(BaseEthereumConfig):
    NETWORKS: ClassVar[dict[str, tuple[int, int]]] = NETWORKS
    mainnet: NetworkConfig = create_network_config(block_time=2, required_confirmations=1)
    amoy: NetworkConfig = create_network_config(block_time=2, required_confirmations=1)


class Polygon(Ethereum):
    fee_token_symbol: str = "POL"

    @property
    def config(self) -> PolygonConfig:  # type: ignore[override]
        return cast(PolygonConfig, self.config_manager.get_config("polygon"))
