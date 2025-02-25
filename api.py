pip install fastapi uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"mensagem": "Bem-vindo à API da Calculadora"}

@app.get("/calcular")
def calcular(operacao: str, a: float, b: float):
    if operacao == "soma":
        return {"resultado": a + b}
    elif operacao == "subtracao":
        return {"resultado": a - b}
    elif operacao == "multiplicacao":
        return {"resultado": a * b}
    elif operacao == "divisao":
        if b == 0:
            return {"erro": "Não é possível dividir por zero"}
        return {"resultado": a / b}
    else:
        return {"erro": "Operação inválida! Use soma, subtracao, multiplicacao ou divisao"}

