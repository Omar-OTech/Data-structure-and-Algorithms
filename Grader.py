def grader(score):
    if 0.9 <= score <= 1:
        return "A"
    elif 0.8 <= score < 0.9:
        return "B"
    elif 0.7 <= score < 0.8:
        return "C"
    elif 0.6 <= score < 0.7:
        return "D"
    else:
        return "F"


# Test cases
print(grader(1))         # "A"
print(grader(1.01))      # "F"
print(grader(0.20))      # "F"
print(grader(0.70))      # "C"
print(grader(0.80))      # "B"
print(grader(0.90))      # "A"
print(grader(0.60))      # "D"
print(grader(0.50))      # "F"
print(grader(0.00))      # "F"
