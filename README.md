# Quick Start

Ecosystem Plugin for Polygon support in Ape.

## Dependencies

- [Python 3](https://www.python.org/downloads) version 3.10 or greater.

## Installation

### via `ape`

You can install this plugin using `ape`:

```bash
ape plugins install polygon
```

or via config file:

```yaml
# ape-config.yaml
plugins:
  - name: polygon
```

### via `pip`

You can install the latest release via [`pip`](https://pypi.org/project/pip/):

```bash
pip install ape-polygon
```

### via source

You can clone the repository and install for development:

```bash
git clone https://github.com/ApeWorX/ape-polygon.git
cd ape-polygon
uv sync --group dev
uv run prek install
```

## Quick Usage

Installing this plugin adds support for the Polygon ecosystem:

```bash
ape console --network polygon:mainnet
```

## Development

Comments, questions, criticisms and pull requests are welcomed.
