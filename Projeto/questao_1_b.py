def q0(x):
    if x[0] == 'a':
        if len(x) == 1:
            print('(q0, a) --> q1')
            return False
        else:
            print('(q0, a) --> q1')
            return q1(x[1:])
    elif x[0] == 'b':
        print('(q0, b) --> q4')

        return q4(x[1:])
    else:
        print('(q0, c) --> q4')
        return q4(x[1:])
def q1(x):
    if x[0] == 'a':
        if len(x) == 1:
            print('(q1, a) --> q2')
            return False
        else:
            print('(q1, a) --> q2')
            return q2(x[1:])
    else:
        return False
def q2(x):
    if x[0] == 'a':
        print('(q2, a) --> q3')
        return q3(x[1:])
    else:
        return False
def q3(x):
    for c in x:
        if c == 'a':
            print('(q3, a) --> None')
            return False
        elif c == 'b':
            print('(q3, b) --> q3')
        elif c == 'c':
            print('(q3, c) --> q3')
    return True
def q4(x):
    lista = x[:]
    for c in lista:
        if c == 'b':
            print('(q4, b) --> q4')
            x = x[1:]
    
        elif c == 'c':
            print('(q4, c) --> q4')
            x = x[1:]
    
        else:
            print('(q4, a) --> q5')
            x = x[1:]
    
            return q5(x)
def q5(x):
    if x == '':
        return False
    for c in x:
        if c == 'b':
            print('(q5, b) --> None')
            return False
        elif c == 'c':
            print('(q5, c) --> none')
            return False
    x = x[1:]
    print('(q5, a) --> q6')
    return q6(x)
def q6(x):
    if x == '':
        return False
    for c in x:
        if c == 'b':
            print('(q6, b) --> None')
            return False
        elif c == 'c':
            print('(q6, c) --> none')
            return False
    x = x[1:]
    if x == '':
        print('(q6, a) --> q7')
        return True
    else:
        return q7(x)
def q7(x):
    for c in x:
        if c == 'a':
            print('(q7, a) --> none')
            return False
        elif c == 'b':
            print('(q7, b) --> none')
            return False
        elif c == 'c':
            print('(q7, c) --> none')
            return False
def automatoB(automato):
    for c in automato:
        if c == 'a' or c == 'b' or c == 'c':
            continue
        else:
            return False
    return q0(automato)
print(automatoB('aaa'))