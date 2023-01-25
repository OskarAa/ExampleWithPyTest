import pytest


# Vienkārša Fibonacci skaitļa aprēķināšanas funkcija
def fib(n):
    old, new = 0, 1
    for _ in range(n):
        old, new = new, old + new
    return old


# Rekursīva Fibonacci skaitļa aprēķināšanas funkcija
def rfib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return rfib(n-1) + rfib(n-2)


# Izsaucam testus šeit
pytest.main(["-v","--durations=4", "--cov", ".", "-p", "no:warnings"])

# vai arī no komandrindas:
# python -m pytest -v --cov . --durations=3