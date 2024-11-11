from typing import List
from fastapi import APIRouter
from pydantic import BaseModel
from decimal import Decimal

router = APIRouter(prefix="/contas-a-pagar-e-receber")


class ContaPagarReceberResponse(BaseModel):
    id: int
    descricao: str
    valor: float
    tipo: str  # PAGAR E RECEBER


class ContaPagarReceberRequest(BaseModel):
    descricao: str
    valor: float
    tipo: str  # PAGAR E RECEBER


@router.get("", response_model=List[ContaPagarReceberResponse])
def listar_contas():
    return [
       ContaPagarReceberResponse(
           id=1,
           descricao="aluguel",
           valor=1000.50,
           tipo="PAGAR"
       ),
       ContaPagarReceberResponse(
           id=1,
           descricao="salário",
           valor=5000,
           tipo="receber"
        ),
    ]


@router.post("", response_model=ContaPagarReceberResponse, status_code=201)
def criar_conta(conta: ContaPagarReceberRequest):
    return ContaPagarReceberResponse(
        id=3,
        descricao=conta.descricao,
        valor=conta.valor,
        tipo=conta.tipo
    )
