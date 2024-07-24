def dir_reduc(arr):
# 2nd solution
    opposites = {'NORTH': 'SOUTH', 'EAST': 'WEST', 'SOUTH': 'NORTH', 'WEST': 'EAST'}
    res = []
    for i in arr:
        if res and opposites[i] == res[-1]:
            res.pop()
        else:
            res.append(i)
    return res




a = ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]
print(dir_reduc(a)) # ['WEST'])
a=["NORTH", "WEST", "SOUTH", "EAST"]
print(dir_reduc(a)) # ["NORTH", "WEST", "SOUTH", "EAST"])
a = ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"] # ['WEST']
print(dir_reduc(a)) # ['WEST'])
a = ["NORTH", "SOUTH", "EAST", "WEST", "NORTH", "NORTH", "SOUTH", "NORTH","WEST", "EAST"] # ['NORTH', 'NORTH']
print(dir_reduc(a)) # ['NORTH', 'NORTH'])
a = [] # []
print(dir_reduc(a)) # []) 
a=["NORTH","SOUTH","SOUTH","EAST","WEST","NORTH"] # []
print(dir_reduc(a)) # [])
a = ["NORTH","SOUTH","SOUTH","EAST","WEST","NORTH","NORTH"] # ["NORTH"]
print(dir_reduc(a)) # ["NORTH"])
a = ["EAST", "EAST", "WEST", "NORTH", "WEST", "EAST", "EAST", "SOUTH", "NORTH", "WEST"] # ["EAST", "NORTH"]
print(dir_reduc(a)) # ["EAST", "NORTH"])
a = ["NORTH", "EAST", "NORTH", "EAST", "WEST", "WEST", "EAST", "EAST", "WEST", "SOUTH"] # ["NORTH", "EAST"])
print(dir_reduc(a)) # ["NORTH", "EAST"])
a = ["NORTH", "WEST", "SOUTH", "EAST"] # ["NORTH", "WEST", "SOUTH", "EAST"])
print(dir_reduc(a)) # ["NORTH", "WEST", "SOUTH", "EAST"])
a = ['NORTH', 'NORTH', 'EAST', 'SOUTH', 'EAST', 'EAST', 'SOUTH', 'SOUTH', 'SOUTH', 'NORTH']
print(dir_reduc(a)) # ['NORTH', 'NORTH', 'EAST', 'SOUTH', 'EAST', 'EAST', 'SOUTH', 'SOUTH'])    