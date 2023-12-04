def f1 (x):
    return 2 * x ** 2 + 3 * x - 1 

def df1 (x):
    return 4 * x + 3


def gradient_descent (func, x0, iter=1000, l=0.2):
    for _ in range(iter):
        x0 = x0 - l * func(x0)
        print(x0)
    return x0

print(gradient_descent(df1, 4))




