import yaml
from pathlib import Path

class Config:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._load_config()
        return cls._instance

    def _load_config(self):
        config_path = Path("config/config.yaml")
        with open(config_path, encoding="utf-8") as f:
            self.data = yaml.safe_load(f)

    @property
    def base_url(self):
        return self.data.get("base_url")

    @property
    def timeout(self):
        return self.data.get("timeout", 15000)

    @property
    def browser(self):
        return self.data.get("browser", "chromium")

    @property
    def headless(self):
        return self.data.get("headless", False)