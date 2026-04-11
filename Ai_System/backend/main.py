# from fastapi import FastAPI
# from pydantic import BaseModel

# app = FastAPI()

# class Expression(BaseModel):
#     expr : str

# @app.post("/calculte")
# def calculate(data : Expression):
#     try:
#         result = eval(data.expr)
#         return{"result: result"}
#     except:
#         return{"Error": "Invalid Expression"}


import requests

@app.post("/chat") 
def chat(data : Expression):
    response = requests.post(
       "http://localhost:11434/api/generate",
       json={
           "model":"mistral"
           "prompt": data.expr
           "stream":False
       } 
    )
    return response.json()