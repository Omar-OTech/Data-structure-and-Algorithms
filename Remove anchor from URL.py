def remove_url_anchor(url):
# 1st solution 
    res = ''
    for i in url:
        if i == '#':
            break
        res += i
    return res

# 2nd solution
    # return url.split('#')[0]

# 3rd solution
    # index = url.find('#')
    # return url[:index] if index >= 0 else url

print(remove_url_anchor("www.codewars.com#about"))                 #  "www.codewars.com"
print(remove_url_anchor("www.codewars.com/katas/?page=1#about"))   #  "www.codewars.com/katas/?page=1"
print(remove_url_anchor("www.codewars.com/katas/"))                #  "www.codewars.com/katas/"