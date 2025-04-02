def pytest_addoption(parser):
    parser.addoption("--errorOnMissing", action="store_true", default=False, help="Decides whether tests fail when a test case is missing or rules are not defined when they should be.")
