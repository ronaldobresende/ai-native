from __future__ import annotations

import asyncio
import json
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))

from agents.orchestrator.state import GuaranteeRequest
from agents.orchestrator.supervisor import Supervisor


async def main() -> None:
    result = await Supervisor().run(
        GuaranteeRequest(identificador_imovel="IMOVEL-HIGH-001")
    )
    print(json.dumps(result.model_dump(mode="json"), indent=2))


if __name__ == "__main__":
    asyncio.run(main())
