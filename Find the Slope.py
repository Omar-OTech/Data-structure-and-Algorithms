def find_slope(points):
    return "undefined" if points[0] == points[2] else str((points[3] - points[1]) // (points[2] - points[0]))

# 2nd solution
    # x1, y1, x2, y2 = points
    # if x1 == x2:
    #     return "undefined"
    # return str((y2 - y1) // (x2 - x1))


print(find_slope([19,3,20,3]))        #"0"
print(find_slope([-7,2,-7,4]))        #"undefined"
print(find_slope([10,50,30,150]))     #"5"
print(find_slope([10,20,20,80]))      #"6"
print(find_slope([-10,6,-10,3]))      #"undefined"