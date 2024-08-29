websites = []
websites_internal = websites
websites.append("codewars")


print((websites_internal == websites))         # "You assigned a new array to the websites variable. You should instead alter the existing reference.")
print((len(websites_internal) > 0))            # 'The array is still empty')
print((len(websites_internal) == 1))           # 'The array contains too many values')
print((websites_internal[0] == 'codewars'))    # 'The array does not contain the correct value "codewars"')