def convert(number):
    conditions = {
        3: "Pling",
        5: "Plang",
        7: "Plong",
    }

    return "".join([conditions[k] for k in conditions if number % k == 0]) or str(number)
