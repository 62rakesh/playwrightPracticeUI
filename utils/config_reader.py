import yaml
import os
from logging import getLogger
from pathlib import Path


class ConfigReader:
    _config = None

    @classmethod
    def load_config(cls):
        if cls._config is None:
            config_path = Path(__file__).parent.parent / "config" / "config.yaml"
            with open(config_path, "r") as file:
                cls._config = yaml.safe_load(file)
        return cls._config

    @classmethod
    def load_env_config(cls):
        if cls._config is None:
            env = os.getenv("TEST_ENV", "dev")
            config_path = (
                Path(__file__).parent.parent / "config" / f"{env}.yaml"
            )
            with open(config_path, "r") as file:
                cls._config = yaml.safe_load(file)
        return cls._config

    @classmethod
    def get_env(cls):
        return os.getenv("TEST_ENV", "dev")

    @classmethod
    def get_base_url(cls):
        env = cls.get_env()
        return cls.load_env_config()[env]["base_url"]

    @classmethod
    def get_browser(cls):
        return cls.load_env_config()["browser"]

    @classmethod
    def get_timeout(cls):
        return cls.load_env_config()["timeouts"]
