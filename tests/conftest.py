import pytest
import hydra

@pytest.fixture(scope="package")
def config():
    with hydra.initialize(config_path='../config',version_base=None):
        config = hydra.compose(config_name="default")
    return config

