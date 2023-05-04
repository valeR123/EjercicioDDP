from typing import Union
from fastapi import FastAPI

app = FastAPI()

def Hello():
    return {"HELLO FASTAPI"}

def Isprime(numero): 
    return False  


def Fibonnacci(numero: int):
     return 3