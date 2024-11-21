from ape import plugins


@plugins.register(plugins.Config)
def config_class():
    from ape_polygon.ecosystem import PolygonConfig

    return PolygonConfig


@plugins.register(plugins.EcosystemPlugin)
def ecosystems():
    from ape_polygon.ecosystem import Polygon

    yield Polygon


@plugins.register(plugins.NetworkPlugin)
def networks():
    from ape.api.networks import (
        LOCAL_NETWORK_NAME,
        ForkedNetworkAPI,
        NetworkAPI,
        create_network_type,
    )

    from ape_polygon.ecosystem import NETWORKS

    for network_name, network_params in NETWORKS.items():
        yield "polygon", network_name, create_network_type(*network_params)
        yield "polygon", f"{network_name}-fork", ForkedNetworkAPI

    # NOTE: This works for development providers, as they get chain_id from themselves
    yield "polygon", LOCAL_NETWORK_NAME, NetworkAPI


@plugins.register(plugins.ProviderPlugin)
def providers():
    from ape.api.networks import LOCAL_NETWORK_NAME
    from ape_node import Node
    from ape_test import LocalProvider

    from ape_polygon.ecosystem import NETWORKS

    for network_name in NETWORKS:
        yield "polygon", network_name, Node

    yield "polygon", LOCAL_NETWORK_NAME, LocalProvider


def __getattr__(name: str):
    if name == "NETWORKS":
        from .ecosystem import NETWORKS

        return NETWORKS

    elif name == "Polygon":
        from .ecosystem import Polygon

        return Polygon

    elif name == "PolygonConfig":
        from .ecosystem import PolygonConfig

        return PolygonConfig

    else:
        raise AttributeError(name)


__all__ = [
    "NETWORKS",
    "Polygon",
    "PolygonConfig",
]
