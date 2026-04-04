import json
import os
from typing import Any


class ConfigReader:
    _instance = None
    _config = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def load_config(self, config_path: str=None) -> dict:
        if config_path is None:
            config_path = os.path.join(os.path.dirname(__file__), '..', 'config', 'config.json')
        with open(config_path, 'r', encoding='utf-8') as f:
            self._config = json.load(f)
            return self._config

    def get(self, key: str, default: Any = None) -> Any:
        if self._config is None:
            self.load_config()
        keys = key.split('.')
        value = self._config
        for k in keys:
            if isinstance(value, dict):
                value = value.get(k, default)
            else:
                return default
        return value

    @property
    def base_url(self) -> str:
        return self.get('base_url')

    @property
    def headless(self) -> bool:
        return self.get('browser.headless', False)

    @property
    def timeout(self)-> int:
        return self.get('browser.timeout', 30000)
