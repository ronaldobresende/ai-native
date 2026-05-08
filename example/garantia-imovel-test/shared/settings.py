from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    app_name: str = "garantia-imovel-test"
    environment: str = "local"

    langfuse_public_key: str | None = None
    langfuse_secret_key: str | None = None
    langfuse_host: str | None = None

    llm_provider: str = "azure-openai"
    llm_model: str = "gpt-4"
    llm_temperature: float = 0.0

    azure_openai_endpoint: str | None = None
    azure_openai_deployment: str | None = None
    azure_openai_api_version: str | None = None

    iara_api_key: str | None = None
    iara_secret_key: str | None = None
    iara_provider: str = "azure-openai"
    iara_model: str = "gpt-4"
    iara_langchain_factory: str = "iara.langchain:AzureChatOpenAI"

    market_price_source_name: str = "mock-web-source"
    market_price_source_url: str = "https://mock.local/imoveis"


settings = Settings()
