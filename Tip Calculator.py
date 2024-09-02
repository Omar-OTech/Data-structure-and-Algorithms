import math

def calculate_tip(amount, rating):
    # Define the tip percentages for each rating
    tips = {
        "terrible": 0,
        "poor": 5,
        "good": 10,
        "great": 15,
        "excellent": 20
    }
    
    # Convert the rating to lowercase for case insensitive comparison
    rating = rating.lower()
    
    # Check if the rating is in the dictionary of valid ratings
    if rating in tips:
        # Calculate the tip based on the percentage
        tip_percentage = tips[rating]
        tip_amount = (tip_percentage / 100) * amount
        # Round up the tip and return it
        return math.ceil(tip_amount)
    else:
        return "Rating not recognised"

# Test cases
print(calculate_tip(30, "poor"))          # 2
print(calculate_tip(20, "Excellent"))     # 4
print(calculate_tip(20, "hi"))            # 'Rating not recognised'
print(calculate_tip(107.65, "GReat"))     # 17
print(calculate_tip(20, "great!"))        # 'Rating not recognised'
