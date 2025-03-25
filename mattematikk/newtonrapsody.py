def f(x):
    return x**2 - 5*x - 5
def d(x):
    return 2*x - 5
svar = input("Velg en start verdi for x: ")
x = float(svar)
while abs(f(x)) > 0.000001:
    x = x - f(x)/d(x)
    print("løsningen er x =", round(x,5))


