def f(x):
    return x**3 - 3*x + 3

def df(x):
    h = 0.0001
    return (f(x+h) - f(x))/h

x = -5

while df(x) > 0:
    x += 0.01

print(x, f(x))