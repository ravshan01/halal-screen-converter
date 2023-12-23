from pydantic import BaseSettings, SecretStr


class Settings(BaseSettings):
    weights_path: str
    bot_token: SecretStr

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


config = Settings()
