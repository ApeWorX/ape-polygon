EXPECTED_OUTPUT = """
polygon
├── mainnet
│   └── geth  (default)
├── mumbai
│   └── geth  (default)
└── local  (default)
    └── test  (default)
ethereum  (default)
├── mainnet
│   └── geth  (default)
├── ropsten
│   └── geth  (default)
├── kovan
│   └── geth  (default)
├── rinkeby
│   └── geth  (default)
├── goerli
│   └── geth  (default)
└── local  (default)
    ├── geth
    └── test  (default)
""".strip()


def assert_rich_text(actual: str, expected: str):
    """
    The output from `rich` causes a bunch of extra spaces to
    appear at the end of each line. For easier testing, we remove those here.
    """
    actual = f"polygon{actual.split('polygon')[-1]}"
    expected = expected.strip()
    lines = actual.split("\n")
    new_lines = []
    for line in lines:
        if line:
            new_lines.append(line.rstrip())

    actual = "\n".join(new_lines)
    assert actual == expected


def test_networks(runner, cli):
    result = runner.invoke(cli, ["networks", "list"])
    assert_rich_text(result.output, EXPECTED_OUTPUT)
