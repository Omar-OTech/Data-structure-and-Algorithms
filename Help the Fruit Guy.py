def remove_rotten(bag_of_fruits):
    if not bag_of_fruits:
        return []
    for i in range(len(bag_of_fruits)):
        if 'rotten' in bag_of_fruits[i]:
            bag_of_fruits[i] = bag_of_fruits[i].replace('rotten', '').lower()
    return bag_of_fruits


print(remove_rotten(["rottenApple","rottenBanana","rottenApple","rottenPineapple","rottenKiwi"]))              # ["apple","banana","apple","pineapple","kiwi"]
print(remove_rotten([]))              # []