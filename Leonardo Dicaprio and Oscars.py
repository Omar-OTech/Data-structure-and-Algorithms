def leo(oscar):
    if oscar == 88:
        return 'Leo finally won the oscar! Leo is happy'
    elif oscar == 86:
        return 'Not even for Wolf of wallstreet?!'
    elif oscar < 88:
        return "When will you give Leo an Oscar?"
    elif oscar > 88:
        return "Leo got one already!"
    
# 2nd solution
    # return "Leo got one already!" if oscar > 88 else "Leo finally won the oscar! Leo is happy" if oscar == 88 else "Not even for Wolf of wallstreet?!" if oscar == 86 else "When will you give Leo an Oscar?"


print(leo(88))     #"Leo finally won the oscar! Leo is happy"
print(leo(87))     #"When will you give Leo an Oscar?"
print(leo(86))     #"Not even for Wolf of wallstreet?!"