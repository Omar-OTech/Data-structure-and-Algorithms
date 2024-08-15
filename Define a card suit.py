def define_suit(card):
# 1st solution
    if card[-1] == 'C': return 'clubs'
    if card[-1] == 'S': return 'spades'
    if card[-1] == 'D': return 'diamonds'
    if card[-1] == 'H': return 'hearts'

# 2nd solution
    return {'C': 'clubs', 'S': 'spades', 'D': 'diamonds', 'H': 'hearts'}[card[-1]]

print(define_suit('3C'))     # 'clubs', "Expected 'clubs'"
print(define_suit('QS'))     # 'spades', "Expected 'spades'"
print(define_suit('9D'))     # 'diamonds', "Expected 'diamonds'"
print(define_suit('JH'))     # 'hearts', "Expected 'hearts'"