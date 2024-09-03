def dashatize(n):
    return ''.join(['-{}-'.format(i) if int(i) % 2 else i for i in str(n).replace('-', '')]).replace('--', '-').strip('-')

print(dashatize(274))        # "2-7-4", "Should return 2-7-4"
print(dashatize(5311))       # "5-3-1-1", "Should return 5-3-1-1"
print(dashatize(86320))      # "86-3-20", "Should return 86-3-20"
print(dashatize(974302))     # "9-7-4-3-02", "Should return 9-7-4-3-02"
print(dashatize(0))          # "0", "Should return 0"
print(dashatize(-1))         # "1", "Should return 1"
print(dashatize(-28369))     # "28-3-6-9", "Should return 28-3-6-9"