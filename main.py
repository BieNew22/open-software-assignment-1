def add(a, b):
    return a + b


def sub(a, b):
    return a - b


num1, num2 = map(int, input("두 수를 입력 >> ").split())
op = input("연산 기호를 입력(+, -) >> ")

if op == "+":
    print(add(num1, num2))
elif op == "-":
    print(sub(num1, num2))