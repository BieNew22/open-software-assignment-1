from math import inf


def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


def div(a, b):
    if b == 0:
        return inf
    return a / b


num1, num2 = map(int, input("두 수를 입력 >> ").split())
op = input("연산 기호를 입력(+, -, *, /) >> ")

if op == "+":
    print(add(num1, num2))
elif op == "-":
    print(sub(num1, num2))
elif op == '*':
    print(mul(num1, num2))
else:
    print(div(num1, num2))