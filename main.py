import math
from datetime import datetime

is_degrees = False
monads = {"!", "sqrt", "neg", "sin", "cos", "tan",
          "ln", "log", "exp",
          "sinh", "cosh", "tanh", "asin", "acos", "atan",
          "asinh", "acosh", "atanh"}

# Additional functions for monad operators
def factorial(n):
    return math.factorial(int(n))

def sqrt(n):
    return math.sqrt(n)

def neg(n):
    return -n

def trigop(_angle, _trigop):
    return _trigop(math.radians(_angle)) if is_degrees else _trigop(_angle) 

def sin(angle):
    return trigop(angle, math.sin)

def cos(angle):
    return trigop(angle, math.cos)

def tan(angle):
    return trigop(angle, math.tan)

def sinh(angle):
    return trigop(angle, math.sinh)

def cosh(angle):
    return trigop(angle, math.cosh)

def tanh(angle):
    return trigop(angle, math.tanh)

def atrigop(_value, _atrigop):
    return math.degrees(_atrigop(_value)) if is_degrees else _atrigop(_value)

def asin(value):
    return atrigop(value, math.asin)

def acos(value):
    return atrigop(value, math.acos)

def atan(value):
    return atrigop(value, math.atan)

def asinh(value):
    return atrigop(value, math.asinh)

def acosh(value):
    return atrigop(value, math.acosh)

def atanh(value):
    return atrigop(value, math.atanh)

def deci2frac(decimal, max_denominator=1000):
    """Decimal to fraction"""
    denominator = 0
    numerator_guesser = [1]
    denominator_guesser = [1]
    for i in range(max_denominator):
        denominator += 1
        numerator = round(decimal * denominator)
        diff = abs(decimal - (numerator / denominator))
        if diff < abs(decimal - (numerator_guesser[-1] / denominator_guesser[-1])):
            numerator_guesser += [numerator]
            denominator_guesser += [denominator]
    return numerator_guesser[-1], denominator_guesser[-1]

def isnum(string):
    """Is number?"""
    for char in string:
        if (ord(char) < 48 or ord(char) > 57) and char != ".":
            return False
    return True

def splitexpr(exp):
    """Split Expression"""
    split = []
    e = exp.strip()
    i = 0
    while i < len(e):
        if e[i] in "()":
            split.append(e[i])
            i += 1
        else:
            match_found = False
            for length in range(7, 1, -1):  # Check for monads from length 7 down to 2
                if e[i:i+length] in monads:
                    split.append(e[i:i+length])
                    i += length
                    match_found = True
                    break
            if not match_found:
                if isnum(e[i]):
                    num = ""
                    while i < len(e) and isnum(e[i]):
                        num += e[i]
                        i += 1
                    split.append(num)
                elif e[i] == "-" and (i == 0 or not isnum(e[i-1])) and (i < len(e) - 1 and isnum(e[i+1])):
                    split.append("neg")
                    i += 1
                else:
                    split.append(e[i])
                    i += 1
    return [o.strip() for o in split]

def prec(c):
    """Precedence"""
    if c in {"%", "//"}:
        return 4
    elif c in {"^", "rt"}:
        return 3
    elif c in {"/", "*"}:
        return 2
    elif c in {"+", "-"}:
        return 1
    elif c in monads:
        return 5
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
        elif c == "(":
            stack.append(c)
        elif c == ")":
            while len(stack) > 0 and stack[-1] != "(":
                postfix.append(stack.pop())
            stack.pop()
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
            operator = pf[i]
            result = 0.0
            if operator in monads:
                n = float(stack.pop())
                if operator == "!":
                    result = factorial(n)
                elif operator == "sqrt":
                    result = sqrt(n)
                elif operator == "neg":
                    result = neg(n)
                elif operator == "ln":
                    result = math.log(n)
                elif operator == "log":
                    result = math.log10(n)
                elif operator == "exp":
                    result = math.exp(n)
                elif operator == "sin":
                    result = sin(n)
                elif operator == "cos":
                    result = cos(n)
                elif operator == "tan":
                    result = tan(n)
                elif operator == "sinh":
                    result = sinh(n)
                elif operator == "cosh":
                    result = cosh(n)
                elif operator == "tanh":
                    result = tanh(n)
                elif operator == "asin":
                    result = asin(n)
                elif operator == "acos":
                    result = acos(n)
                elif operator == "atan":
                    result = atan(n)
                elif operator == "asinh":
                    result = asinh(n)
                elif operator == "acosh":
                    result = acosh(n)
                elif operator == "atanh":
                    result = atanh(n)
                stack.append(result)
            else:
                n2 = float(stack.pop())
                n1 = float(stack.pop())
                if operator == "+":
                    result = n1 + n2
                elif operator == "-":
                    result = n1 - n2
                elif operator == "*":
                    result = n1 * n2
                elif operator == "/":
                    try:
                        result = n1 / n2
                    except ZeroDivisionError:
                        result = "ZDE"
                elif operator == "^":
                    result = n1 ** n2
                elif operator == "rt":
                    result = n2 ** (1 / n1)
                elif operator == "%":
                    result = n1 % n2
                elif operator == "//":
                    try:
                        result = n1 // n2
                    except ZeroDivisionError:
                        result = "ZDE"
                stack.append(result)
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
    if len(splitexpr(expr.replace(" ", ""))) < 2:
        return float(expr)
    ans = evalpostfix(topostfix(splitexpr(expr.replace(" ", ""))))
    return ans

from sys import argv, exit

if "--help" not in argv and "-h" not in argv and "-H" not in argv:
    print("Welcome to dCalc 1.0.0 beta!")
    print("Type the expression at the prompt.")
    while True:
        expression = input("dCalc> ")
        if "quit" in expression or "exit" in expression:
            exit()
        if "population" in expression.lower():
            seconds_since_1970 = datetime.now().timestamp()
            days_since_2000 = (seconds_since_1970 / 86400) - 10957
            bpd = 362759
            dpd = 170934
            population = 8188828110 + round((days_since_2000 - 9088) * bpd) - round((days_since_2000 - 9088) * dpd)
            print(population)
            continue
        if not expression:
            continue
        if "angle rad" in expression.lower() or "angle radians" in expression.lower() or "angle radian" in expression.lower():
            is_degrees = False
            continue
        if "angle deg" in expression.lower() or "angle degrees" in expression.lower() or "angle degree" in expression.lower():
            is_degrees = True
            continue
        if expression.count("(") < expression.count(")"):
            print("eRR: Mismatched Parentheses. Did you forget an opening bracket?")
            continue
        if expression.count(")") < expression.count("("):
            print("eRR: Mismatched Parentheses. Did you forget a closing bracket?")
            continue
        
        try:
            answer = evaluate(expression)
            print(format_out(answer))
        except (ArithmeticError, IndexError, TypeError, ValueError) as e:
            if "could not convert string to float: '" in str(e):
                print(f"eRR: Invalid Number: {str(e)[35:]}")
            else:
                print("eRR: Invalid Expression/Syntax")
        print("")
else:
    if "--help" in argv or "-h" in argv or "-H" in argv:
        print("Usage: dcalc [--help]")
        print("Source Code Usage: python main.py (in direct usage via source code)")
        print("Operators: ")
        print("\t+ Addition")
        print("\t- Subtraction")
        print("\t* Multiplication")
        print("\t/ Division")
        print("\t^ Exponentiation")
        print("\trt nth Root")
        print("\t% Modulo")
        print("\t// Floor division")
        print("\t! Factorial (monad)")
        print("\tsqrt Square Root (monad)")
        print("\tneg Negation (monad)")
        print("Documentation: https://github.com/GreatCoder1000/dcalc")
        print("Example: 123+456 = 579")
        print("type 'population' at the prompt for current population.")
