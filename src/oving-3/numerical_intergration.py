import numpy as np


def f(x):
    return 2 - 2 * x


def Method(f, a, b, N):
    x = np.linspace(a, b, N + 1)
    S = 0
    for i in range(N):
        S += 0.5 * (x[i + 1] - x[i]) * (f(x[i + 1]) + f(x[i]))
    return S


print(Method(f, 0, 1, 2))
print(Method(f, 0, 1, 4))
print(Method(f, 0, 1, 10))
