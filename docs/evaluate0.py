import math

def isnum(string):
    # asymptotic time: O(n)
    for char in string:
        if (ord(char) < 48 or ord(char) > 57) and char != '.':
            return False
    return True

def splitexpr(exp):
    """Split Expression"""
    split = []
    for i in range(len(exp)):
        if i == 0:
            split.append(exp[i])
        elif isnum(exp[i]) == isnum(exp[i-1]):
            split[-1] = split[-1] + exp[i]
        else:
            split.append(exp[i])
    return split


# Function to return precedence of operators
def prec(c):
    if c == '^':
        return 3
    elif c == '/' or c == '*':
        return 2
    elif c == '+' or c == '-':
        return 1
    else:
        return -1

# Infix to Postfix
def topostfix(split):
    postfix = []
    stack = []
    for i in range(len(split)):
        c = split[i]
        if isnum(c):
            postfix.append(c)
        elif c == '(':
            stack.append(c)
        elif c == ')':
            while len(stack) > 0 and stack[-1] != '(':
                postfix.append(stack.pop())
            del stack[-1]
        else:
            while stack and (prec(c) < prec(stack[-1]) or prec(split[i]) == prec(stack[-1])):
                postfix.append(stack.pop())
            stack.append(c)

    while stack:
        postfix.append(stack.pop())
    return postfix

def evalpostfix(pf):
    stack = []
    for i in range(len(pf)):
        if isnum(pf[i]):
            stack.append(pf[i])
        else:
            n2 = float(stack.pop())
            n1 = float(stack.pop())
            if pf[i] == '+':
                stack.append(n1 + n2)
            elif pf[i] == '-':
                stack.append(n1 - n2)
            elif pf[i] == '*':
                stack.append(n1 * n2)
            elif pf[i] == '/':
                try:
                    stack.append(n1 / n2)
                except ZeroDivisionError:
                    stack.append("ZDE")
            elif pf[i] == '^':
                stack.append(n1 ** n2)
            elif pf[i] == 'rt':
                stack.append(n2 ** (1 / n1))
    return stack[-1]

def format_out(flt, frac=False):
    if flt == "pole_err":
        return "eRR 06: Pole Error!"
    if flt == "domain_err":
        return "eRR 05: Domain Error!"
    if flt == "NAN":
        return "eRR 04: Not a Number!"
    if flt == "undef":
        return "eRR 03: Undefined!"
    if flt == "ZDE":
        return "eRR 02: You can't divide by zero you know!"
    if math.isinf(flt):
        return "eRR 01: Infinity!"
    out = float(flt)
    if out == round(out):
        out = int(round(out))
    if type(out) == float:
        if frac:
            out = f"{int(out // 1)} {deci2frac(out % 1)[0]}/{deci2frac(out % 1)[1]}"
        else:
            out = str(out)
    out = str(out)
    return out

def evaluate(expr):
    ans = evalpostfix(topostfix(splitexpr(expr.replace(" ", ""))))
    return ans
