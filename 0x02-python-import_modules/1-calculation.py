#!/usr/bin/python3
a = 10
b = 5
from calculator_1 import add, sub, mul, div

result_add = add(a, b)
result_sub = sub(a, b)
result_mul = mul(a, b)
result_div = div(a, b)

print(f"{a} + {b} = {result_add}")
print(f"{a} - {b} = {result_sub}")
print(f"{a} * {b} = {result_mul}")
print(f"{a} / {b} = {result_div}")
