import pytest
import json
def pytest_addoption(parser):
    parser.addoption(
        "--env", action="store", default="prod"
    )

def update_env(config):
    with open("C:\\api-testing\\config\\endpoint.json","r+") as json_file:
        data = json.load(json_file)
        json_file.truncate(0)
        json_file.seek(0)
        data["environment"]["env"] = config.getoption("--env").lower()
        json.dump(data, json_file, indent=4)

@pytest.hookimpl
def pytest_configure(config):
    update_env(config)