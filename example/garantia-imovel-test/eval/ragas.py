from __future__ import annotations

from pathlib import Path


GOLDEN_SET_PATH = Path(__file__).parent / "golden_set"


async def run_ragas_evaluation():
    """
    RAGAS-ready placeholder.

    Add datasets under eval/golden_set and map project outputs into the RAGAS
    dataset format when a real retrieval/evaluation corpus is available.
    """

    return {
        "status": "ready",
        "golden_set_path": str(GOLDEN_SET_PATH),
    }
