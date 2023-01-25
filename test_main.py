from main import fib, rfib


def test_fib():
    assert fib(1) == 1
    assert fib(10) == 55
    assert fib(28) == 317811


def test_rfib():
    assert rfib(0) == 0
    assert rfib(10) == 55
    assert rfib(28) == 317811
