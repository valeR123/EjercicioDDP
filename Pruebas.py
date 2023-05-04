from main import *

def test_Hello():
    saludo = Hello()
    assert saludo == "HELLO FASTAPI"
    
def test_Isprime():
    numero=Isprime(6)
    assert numero == False
    
def test_Fibonacci():
    numero=Fibonacci(4)
    assert numero == 3