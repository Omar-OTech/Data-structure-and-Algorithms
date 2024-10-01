def ensure_question(s):
    if not s:
        return "?"
    if s.endswith('?'):
        return s
    return s + "?"


print(ensure_question(""))             # "?","Expected: '?'"
print(ensure_question("Yes"))          # "Yes?","Expected: '?'"
print(ensure_question("No?"))          # "No?","Expected: '?'"
print(ensure_question("Well????"))     # "Well????","Expected: '?'"