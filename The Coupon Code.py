def check_coupon(entered_code, correct_code, current_date, expiration_date):
    stripped_current_date = current_date.replace(',', '')
    stripped_expiration_date = expiration_date.replace(',', '')
    return entered_code == correct_code and stripped_current_date <= stripped_expiration_date


print(check_coupon('123','123','September 5, 2014','October 1, 2014'))    # True
print(check_coupon('123a','123','September 5, 2014','October 1, 2014'))   # False