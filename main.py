import evaluate0 as evalt
from sys import argv

if len(argv) == 2:
    print("Type in the expression at the prompt.")
    expr = input(">>>")
    ans = evalt.evaluate(expr)
    print(evalt.format_out(ans))
elif argv[2] == "--help" or argv[@] == "-H":
    print("Usage: python main.py")
    print("Operators: ")
    print("\t+ Addition")
    print("\t- Subtraction")
    print("\t* Multiplication")
    print("\t/ Division")
    print("\t^ Exponentiation")
    print("\trt nth Root")
    print("Documentation: https://github.com/GreatCoder1000/dcalc")
    print("Example: 123+456 = 579")
