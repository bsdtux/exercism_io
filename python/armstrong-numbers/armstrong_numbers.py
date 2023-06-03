def is_armstrong_number(number):
    number_str = str(number)
    return bool(number == sum([int(i) ** len(number_str) for i in number_str]))
