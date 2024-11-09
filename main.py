import math

def deci2frac(decimal, max_denominator=1000):
    """Decimal to fraction"""
    denominator = 0
    numerator_guesser = [1]
    denominator_guesser = [1]
    for i in range(max_denominator):
        denominator += 1
        numerator = round(decimal * denominator)
        diff = abs(decimal-(numerator/denominator))
        if diff < abs(decimal-(numerator_guesser[-1]/denominator_guesser[-1])):
            numerator_guesser += [numerator]
            denominator_guesser += [denominator]
    return numerator_guesser[-1], denominator_guesser[-1]

def isnum(string):
    """Is number?"""
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

def prec(c):
    """Precedence"""
    if c == '%' or c == '//':
        return 4
    elif c == '^' or c == 'rt':
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
            elif pf[i] == '%':
                stack.append(n1 % n2)
            elif pf[i] == '//':
                stack.append(n1 // n2)
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

if len(argv) < 2 or argv[0] != "python":
    print("Type in the expression at the prompt.")
    while True:
        expression = input(">>>")
        if "quit" in expression or "exit" in expression:
            exit()
        if "cls" in expression.split() or "clr" in expression.split() or "clear" in expression.split():
            clear_terminal()
            continue
        try:
            answer = evaluate(expression)
            print(format_out(answer))
        except AttributeError:
            pass
        except ArithmeticError:
            pass
        except IndexError:
            pass
        except TypeError:
            pass
        except ValueError:
            pass
        else:
            pass
        print("")
else:
    if argv[-1] == "--help" or argv[-1] == "-H":
        print("Usage: dcalc")
        print("Usage: python main.py (in direct usage via source code)")
        print("Operators: ")
        print("\t+ Addition")
        print("\t- Subtraction")
        print("\t* Multiplication")
        print("\t/ Division")
        print("\t^ Exponentiation")
        print("\trt nth Root")
        print("\t% Modulo")
        print("\t// Floor division")
        print("Documentation: https://github.com/GreatCoder1000/dcalc")
        print("Example: 123+456 = 579")
