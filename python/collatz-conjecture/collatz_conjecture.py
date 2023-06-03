def steps(number):
    step_count = 0

    if number == 1:
        return step_count

    if number < 1:
        raise ValueError("Only positive integers are allowed")

    while True:
        step_count += 1

        if number % 2 == 0:
            number = number // 2
        else:
            number = (3 * number) + 1

        if number == 1:
            break
    
    return step_count