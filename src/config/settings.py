import yaml
from pathlib import Path
from dataclasses import dataclass
from typing import List, Dict, Any

@dataclass  
class SiglipConfig:
    name: str
    precision: str
    device: str
    batch_size: int

@dataclass
class OCRConfig:
    languages: List[str]
    confidence_threshold: float
    use_gpu: bool

@dataclass
class DatabaseConfig:
    vector_db_path: str
    text_db_path: str


@dataclass
class Config:
    models: Dict[str, Any]
    database: DatabaseConfig
    performance: Dict[str, Any]
    search: Dict[str, Any]

def load_config(config_path: str = None) -> Config:
    if config_path is None:
        config_path = Path(__file__).parent / "config.yaml"

    with open(config_path, "r") as f:
        data = yaml.safe_load(f)

    return Config(
        models=data["models"],
        database=DatabaseConfig(**data["database"]),
        performance=data["performance"],
        search=data["search"]
    )
