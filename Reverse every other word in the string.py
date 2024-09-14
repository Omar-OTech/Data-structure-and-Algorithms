def reverse_alternate(st):
    st = st.split()
    for i in range(1, len(st), 2):
        st[i] = st[i][::-1]
    return ' '.join(st)

print(reverse_alternate("Did it work?"))                               #  "Did ti work?"
print(reverse_alternate("I really hope it works this time..."))        #  "I yllaer hope ti works siht time..."
print(reverse_alternate("Reverse this string, please!"))               #  "Reverse siht string, !esaelp"
print(reverse_alternate("Have a beer"))                                #  "Have a beer"
print(reverse_alternate("   "))                                        #  ""
print(reverse_alternate("This is not a test "))                        #  "This si not a test"
print(reverse_alternate("This       is a  test "))                     #  "This si a tset"