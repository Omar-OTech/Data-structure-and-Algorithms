def include(arr, item):
    if item in arr:
        return True
    else:
        return False


lst = [0,1,2,3,5,8,13,2,2,2,11];
print(include(lst, 100))     # False, "list does not include 100")
print(include(lst, 2))       # True, "list includes 2 multiple times")
print(include(lst, 11))      # True, "list includes 11")
print(include(lst, "2"))     # False, "list includes 2 (integer))     # not ''2'' (string)")
print(include(lst, 0))       # True, "list includes 0")
print(include([], 0))        # False, "empty list doesn't include anything")