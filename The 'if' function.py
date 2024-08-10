def _if(bool, func1, func2):
    if bool:
        return func1()
    else:
        return func2()

def truthy(): return True
def falsey(): return False

print(_if(True, truthy, falsey)) # True
print(_if(False, truthy, falsey)) # False
print(_if(True, lambda: 'True', lambda: 'False')) # True
print(_if(False, lambda: 'True', lambda: 'False')) # False
print(_if(True, lambda: 1, lambda: 0)) # 1
print(_if(False, lambda: 1, lambda: 0)) # 0
print(_if(True, lambda: 'True', lambda: 0)) # 'True'
print(_if(False, lambda: 'True', lambda: 0)) # 0
print(_if(True, lambda: 1, lambda: 'False')) # 1
print(_if(False, lambda: 1, lambda: 'False')) # 'False'