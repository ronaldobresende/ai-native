from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "{{ project_name }}"
    environment: str = "local"

    langfuse_public_key: str | None = None
    langfuse_secret_key: str | None = None
    langfuse_host: str | None = None


settings = Settings()