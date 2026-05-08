from __future__ import annotations

from typing import Any

from .settings import settings


def get_langfuse_client() -> Any | None:
    if not settings.langfuse_public_key or not settings.langfuse_secret_key:
        return None

    try:
        from langfuse import Langfuse
    except ImportError:
        return None

    return Langfuse(
        public_key=settings.langfuse_public_key,
        secret_key=settings.langfuse_secret_key,
        host=settings.langfuse_host,
    )


def trace_metadata(execution_path: list[str]) -> dict[str, Any]:
    return {
        "app": settings.app_name,
        "environment": settings.environment,
        "llm_provider": settings.llm_provider,
        "llm_model": settings.llm_model,
        "execution_path": execution_path,
    }
