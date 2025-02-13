from collections import Counter

def most_frequent_item_count(collection):
    if not collection:
        return 0
    
    # Count the frequencies of each item in the collection
    count = Counter(collection)
    
    # Return the highest frequency
    return max(count.values())

print(most_frequent_item_count([3, -1, -1]))                                  # 2, "didn't work for [3, -1, -1]")
print(most_frequent_item_count([3, -1, -1, -1, 2, 3, -1, 3, -1, 2, 4, 9, 3])) # 5, "didn't work for [3, -1, -1, -1, 2, 3, -1, 3, -1, 2, 4, 9, 3]")
print(most_frequent_item_count([]))                                           # 0, "didn't work for []")
print(most_frequent_item_count([9]))                                          # 1, "didn't work for [9]")