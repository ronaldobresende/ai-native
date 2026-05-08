from fastapi import FastAPI
from pydantic import BaseModel

from agents.orchestrator.state import GuaranteeRequest
from agents.orchestrator.supervisor import Supervisor

app = FastAPI()


@app.get("/health")
async def health():
    return {"status": "ok"}


class GuaranteeRequestBody(BaseModel):
    identificador_imovel: str | None = None
    numero_matricula: str | None = None


@app.post("/debug/garantia-imovel")
async def debug_guarantee(body: GuaranteeRequestBody):
    result = await Supervisor().run(
        GuaranteeRequest(
            identificador_imovel=body.identificador_imovel,
            numero_matricula=body.numero_matricula,
        )
    )
    return result.model_dump(mode="json")
