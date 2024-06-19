def cockroach_speed(s):
# 1st solution
    # return abs(int(s * 27.7778))

# 2nd solution
    cm_per_km = 100000
    sec_per_hour = 3600
    return int(s * cm_per_km / sec_per_hour)

print(cockroach_speed(1.08))  # 30
print(cockroach_speed(1.09))  # 30
print(cockroach_speed(0))     # 0
