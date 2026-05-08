from __future__ import annotations

import importlib
from typing import Any

from .settings import settings


def _load_factory(factory_path: str) -> Any:
    module_name, _, attr_name = factory_path.partition(":")

    if not module_name or not attr_name:
        raise RuntimeError(
            "Configure IARA_LANGCHAIN_FACTORY as 'module:attribute'."
        )

    module = importlib.import_module(module_name)
    return getattr(module, attr_name)


def get_llm() -> Any:
    """
    Return a LangChain-compatible GPT-4 client through the IARA SDK.

    The mock workflow does not call the LLM yet. This adapter is narrow so a
    future integration can provide the actual IARA LangChain factory without
    changing agent code.
    """

    if settings.llm_provider != "azure-openai":
        raise RuntimeError("This test project is configured for Azure OpenAI.")

    try:
        factory = _load_factory(settings.iara_langchain_factory)
    except (ImportError, AttributeError) as exc:
        raise RuntimeError(
            "IARA SDK is not installed or IARA_LANGCHAIN_FACTORY is invalid. "
            "Install/configure the internal SDK before enabling LLM calls."
        ) from exc

    return factory(
        provider=settings.iara_provider,
        model=settings.iara_model,
        deployment=settings.azure_openai_deployment,
        endpoint=settings.azure_openai_endpoint,
        api_version=settings.azure_openai_api_version,
        api_key=settings.iara_api_key,
        temperature=settings.llm_temperature,
    )
