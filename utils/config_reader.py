import yaml
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
    def get_env(cls):
        return cls.load_config()["environment"]

    @classmethod
    def get_base_url(cls):
        env = cls.get_env()
        return cls.load_config()[env]["base_url"]

    @classmethod
    def get_browser(cls):
        return cls.load_config()["browser"]

    @classmethod
    def get_timeout(cls):
        return cls.load_config()["timeouts"]
