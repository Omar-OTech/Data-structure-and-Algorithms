def get_size(w,h,d):
    SA = (2*d*w) + (2*d*h) + (2*w*h)
    volume = d * w * h
    return [SA, volume]



print(get_size(4, 2, 6))          # [88,48])
print(get_size(1, 1, 1))          # [6,1])
print(get_size(1, 2, 1))          # [10,2])
print(get_size(1, 2, 2))          # [16,4])
print(get_size(10, 10, 10))       # [600,1000])