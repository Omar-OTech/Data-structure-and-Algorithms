def rev_rot(strng, sz):
    # Handle invalid input cases
    if sz <= 0 or strng == "" or sz > len(strng):
        return ""

    result = []
    
    # Iterate through the string in chunks of size sz
    for i in range(0, len(strng), sz):
        chunk = strng[i:i + sz]
        
        # Ignore the last chunk if its length is less than sz
        if len(chunk) < sz:
            break
        
        # Calculate the sum of the digits in the chunk
        chunk_sum = sum(int(digit) for digit in chunk)
        
        # Reverse the chunk if the sum of digits is divisible by 2
        if chunk_sum % 2 == 0:
            result.append(chunk[::-1])
        else:
            # Rotate the chunk to the left by one position
            result.append(chunk[1:] + chunk[0])
    
    # Join the processed chunks and return the final result
    return ''.join(result)

# Test cases
print(rev_rot("123456987654", 6))   # Expected: "234561876549"
print(rev_rot("123456987653", 6))   # Expected: "234561356789"
print(rev_rot("66443875", 4))       # Expected: "44668753"
print(rev_rot("66443875", 8))       # Expected: "64438756"
print(rev_rot("664438769", 8))      # Expected: "67834466"
print(rev_rot("123456779", 8))      # Expected: "23456771"
print(rev_rot("", 8))               # Expected: ""
print(rev_rot("123456779", 0))      # Expected: ""
print(rev_rot("563000655734469485", 4))  # Expected: "0365065073456944"
