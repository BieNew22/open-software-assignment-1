def add(a, b):
    return a + b


def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    return a / b


num1, num2 = -1, -1
while True:
    try:
        num1, num2 = map(int, input("두 정수를 공백을 두고 입력 >> ").split())

        break
    except:
        print("=== error : 두 정수를 입력하셔야 합니다. ===")

op_set = {'-', '*', '+', '/'}
while True:
    op = input("연산 기호를 입력(+, -, *, /) >> ")

    if op not in op_set:
        print("-, +, *, / 중 하나를 입력하세요!!")
    else:
        break
    

if op == "+":
    print(add(num1, num2))
elif op == "-":
    print(sub(num1, num2))
elif op == '*':
    print(mul(num1, num2))
else:
    print(div(num1, num2))