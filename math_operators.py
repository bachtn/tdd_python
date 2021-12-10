def compute(a, b):
    c = add(a, b)
    d = multiply(a, c)
    return d


def add(a, b):
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        raise TypeError(":'(")
    return a + b


def multiply(a, b):
    return a * b
