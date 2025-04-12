def calculator(a,b,op):
    if op == '+':
        print(a+b)
    elif op == '-':
        print(a-b)
    elif op == '*':
        print(a*b)
    elif op == '/':
        if b == 0:
            print("0으로 나눌 수 없습니다.")
        else:
            print(a/b)
    else:
        print("잘못 입력하셨습니다.")