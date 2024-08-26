class solution(object):
    def fizzBuzz(self, n):
        # Initialize an empty list to store the results
        result = []
        
        # Loop through numbers from 1 to n
        for i in range(1, n + 1):
            # Check divisibility conditions
            if i % 3 == 0 and i % 5 == 0:
                result.append("FizzBuzz")
            elif i % 3 == 0:
                result.append("Fizz")
            elif i % 5 == 0:
                result.append("Buzz")
            else:
                result.append(str(i))  # Convert integer to string and append
        
        return result
        
# Test Cases
n = 15
sol = solution()
print(sol.fizzBuzz(n))        # "FizzBuzz"

n = 3
sol = solution()
print(sol.fizzBuzz(n))        # "Fizz"

n = 5
sol = solution()
print(sol.fizzBuzz(n))        # "Buzz"

n = 1
sol = solution()
print(sol.fizzBuzz(n))        # "1"

n = 2
sol = solution()
print(sol.fizzBuzz(n))        # "2"

n = 4
sol = solution()
print(sol.fizzBuzz(n))        # "4"