from fastapi import FastAPI
import uvicorn

from contas_a_pagar_e_receber.routers import contas_a_pagar_e_receber_router

from contas_a_pagar_e_receber.models.contas_a_pagar_receber_model \
    import ContaPagarReceber

app = FastAPI()

@app.get("/")
def oi_eu_sou_programador():
    return "oi eu sou programador"


app.include_router(contas_a_pagar_e_receber_router.router)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8001)
