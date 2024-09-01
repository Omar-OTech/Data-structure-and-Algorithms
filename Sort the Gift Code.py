def sort_gift_code(code):
    return ''.join(sorted(code))

print(sort_gift_code('abcdef'))                         # 'abcdef'
print(sort_gift_code('pqksuvy'))                        # 'kpqsuvy'
print(sort_gift_code('zyxwvutsrqponmlkjihgfedcba'))     # 'abcdefghijklmnopqrstuvwxyz'