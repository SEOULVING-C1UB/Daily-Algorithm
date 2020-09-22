def operate(data, before, after):
    if data == '+':
        return before + after
    elif data == '*':
        return before * after

operator = ['+','*']
container = ['(',')']
outside = {'(':3,'*':2,'+':1,')':0}
inside = {'(':0,'*':2,'+':1}

for t in range(1,11):
    N = int(input())
    expression = list(input())
    stack_1 = []
    stack_2 = []
    for element in expression:
        if element in operator or element in container:
