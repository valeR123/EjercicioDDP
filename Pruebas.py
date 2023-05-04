from main import *

def test_Hello():
    saludo = Hello()
    assert saludo == "Hello fastapi"
    
def test_Isprime():
    numero=Primo(6)
    assert numero == False
    
def test_Fibonacci():
    numero=Fibonacci(4)
    assert numero == 3