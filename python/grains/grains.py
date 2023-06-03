def square(number):
    if not (number > 0 and number < 65):
        raise ValueError("square must be between 1 and 64")

    total = 1
    for _ in range(1, number):
        total += total 
    return total

def total():
    total = 0
    for i in range(1, 65):
        total += square(i)
    return total
