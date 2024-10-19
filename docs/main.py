import evaluate0 as evalt

print("Type in the expression at the prompt.")
expr = input(">>>")
ans = evalt.evaluate(expr)
print(evalt.format_out(ans))
