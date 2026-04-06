from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Expression(BaseModel):
    expr : str

@app.post("/calculte")
def calculate()