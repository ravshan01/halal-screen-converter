from pathlib import PurePath
from pydantic_settings import BaseSettings, SettingsConfigDict
from settings import ROOT_DIR


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=str(PurePath(ROOT_DIR, ".env")), env_file_encoding="utf-8"
    )

    port: int
    bot_token: str
    weights_path: str


config = Settings()
