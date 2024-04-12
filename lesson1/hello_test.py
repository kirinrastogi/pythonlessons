import hello

def test_greeting():
    assert hello.greeting() == "Hello World!"

def test_increment():
    assert hello.increment(3) == 4

def test_decrement():
    assert hello.decrement(3) == 2

def test_multiply_numbers():
    assert hello.multiply(3, 4) == 12

def test_multiply_strings():
    assert hello.multiply("A", 2) == "AA"