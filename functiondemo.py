def evaluate_student(name, score):

    if score >= 90:
        return name, "A"
    elif 75<= score <= 89:
        return name, "B"
    elif 60<= score <= 74:
        return name, "C"
    else:
        return name, "Fail"

n, g = evaluate_student("Rahul", 82)
print("Name:",n, "| Grade:", g)