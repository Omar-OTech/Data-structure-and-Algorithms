def update_light(current):
# 1st solution
    traffic_light = ["green", "yellow", "red"]
    for i in range(len(traffic_light)):
        if current == traffic_light[i]:
            return traffic_light[(i + 1) % 3]
    return None


# 2nd solution
    # return {"green": "yellow", "yellow": "red", "red": "green"}[current]


print(update_light('green'))      #   'yellow'
print(update_light('yellow'))     #   'red'
print(update_light('red'))        #   'green'
