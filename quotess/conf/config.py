from pydantic import ConfigDict
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    email_backend: str
    email_host: str
    email_port: int
    email_starttls: bool
    email_use_ssl: bool
    email_use_tls: bool
    email_host_user: str
    email_host_password: str
    default_from_email: str
    db_engine: str
    db_name: str
    db_user: str
    db_password: str
    db_host: str
    db_port: str

    model_config = ConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra='ignore'
    )


settings = Settings()