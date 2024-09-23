def sort_my_string(s):
    even = ''
    odd = ''
    for i in range(len(s)):
        if i % 2 == 0:
            even += s[i]
        else:
            odd += s[i]
    return f"{even} {odd}"

# 2nd solution
def sort_my_string(s):
    return f"{s[::2]} {s[1::2]}"

print(sort_my_string("CodeWars"))      # "CdWr oeas"
print(sort_my_string("YCOLUE'VREER"))  # "YOU'RE CLEVER"