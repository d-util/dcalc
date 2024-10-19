def deci2frac(decimal, max_denominator=1000):
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
    return (numerator_guesser[-1], denominator_guesser[-1])
