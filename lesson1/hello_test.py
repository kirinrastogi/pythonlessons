import hello
import math

def test_greeting():
    assert hello.greeting() == "Hello"

def test_greet_world():
    assert hello.greet_world() == "Hello World"

def test_increment():
    assert hello.increment(3) == 4

def test_decrement():
    assert hello.decrement(3) == 2

def test_multiply_numbers():
    assert hello.multiply(3, 4) == 12

def test_multiply_strings():
    assert hello.multiply("A", 2) == "AA"

def test_degrees():
    assert hello.degrees(math.pi) == 180

def test_radians():
    assert hello.radians(180) == math.pi

def test_area_of_circle():
    assert hello.area_of_circle(10) == 314.1592653589793

def test_volume_of_cylinder():
    assert hello.volume_of_cylinder(10, 10) == 3141.5926535897934