def ip_to_int32(ip):
    res = 0
    for x in ip.split('.'):
        res = res * 256 + int(x)
    return res

# 2nd solution
    # return int(''.join([bin(int(x))[2:].zfill(8) for x in ip.split('.')]), 2)

# 3rd solution
    # add = ip.split('.')
    # res = int(add[0]) << 24
    # res += int(add[1]) << 16
    # res += int(add[2]) << 8
    # res += int(add[3])
    # return res

# 4th solution
    # res = ""
    # for x in ip.split("."):
    #     res += "{0:08b}".format(int(x))   # res += bin(int(x))[2:].zfill(8)
    # return int(res, 2)


print(ip_to_int32("128.114.17.104"))   # 2154959208
print(ip_to_int32("0.0.0.0"))          # 0
print(ip_to_int32("128.32.10.1"))      # 2149583361