def guess_blue(blue_start, red_start, blue_pulled, red_pulled):
    remainingBlue = blue_start - blue_pulled
    remainingRed = red_start - red_pulled
    totalRemaining = remainingBlue + remainingRed
    probabilityBlue = remainingBlue / totalRemaining
    return probabilityBlue

print(guess_blue(5, 5, 2, 3))    # 0.6
print(guess_blue(5, 7, 4, 3))    # 0.2
print(guess_blue(12, 18, 4, 6))  # 0.4