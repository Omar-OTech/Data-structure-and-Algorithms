def evaporator(content, evap_per_day, threshold):
    day = 0
    curent_content = content
    threshold_content = content * (threshold / 100) 
    while curent_content > threshold_content:
        curent_content -= curent_content * (evap_per_day / 100)
        day += 1
    return day

print(evaporator(10, 10, 10))        # 22
print(evaporator(10, 10, 5))         # 29
print(evaporator(100, 5, 5))         # 59
print(evaporator(50, 12, 1))         # 37
print(evaporator(47.5, 8, 8))        # 31
print(evaporator(100, 1, 1))         # 459
print(evaporator(10, 1, 1))          # 459
print(evaporator(100, 1, 5))         # 299