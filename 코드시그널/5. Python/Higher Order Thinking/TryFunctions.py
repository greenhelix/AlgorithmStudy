import math


def tryFunctions(x, functions):
    return [eval(i)(x) for i in functions]


a = 1
t = -20
functions = ["math.sin", "math.cos", "lambda x: x * 2", "lambda x: x ** 2"]
test = ["abs"]
print(tryFunctions(a, functions))
