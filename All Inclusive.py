def contain_all_rots(strng, arr):
    for i in range(len(strng)):
        if ''.join(sorted([strng[i:] + strng[:i]])) not in arr:
            return False
    return True

# 2nd solution
    # for _ in range(len(strng)):
    #     if not strng in arr:
    #         return False
    #     strng = strng[-1] + strng[:-1]
    # return True



print(contain_all_rots("bsjq", ["bsjq", "qbsj", "sjqb", "twZNsslC", "jqbs"]))                                                          #  True
print(contain_all_rots("XjYABhR", ["TzYxlgfnhf", "yqVAuoLjMLy", "BhRXjYA", "YABhRXj", "hRXjYAB", "jYABhRX", "XjYABhR", "ABhRXjY"]))    #  False
print(contain_all_rots("QJAhQmS", ["hQmSQJA", "QJAhQmS", "QmSQJAh", "yUgUXoQE", "AhQmSQJ", "mSQJAhQ", "SQJAhQm", "JAhQmSQ"]))          #  True
print(contain_all_rots("Etsshp", ["nVOETcaxdvuk", "shpEts", "hpEtss", "Etsshp", "OuIiQ", "sXrDdPXIaW", "tsshpE", "pEtssh"]))           #  False
print(contain_all_rots("Ajylvpy", ["Ajylvpy", "ylvpyAj", "jylvpyA", "lvpyAjy", "pyAjylv", "vpyAjyl"]))                                 #  False
print(contain_all_rots("MqhWvHF", ["numMfygcH", "HFMqhWv", "qhWvHFM", "ZJKKxM", "hWvHFMq", "MqhWvHF", "hfZWYSqk", "BTcSoEdchPlL", "WvHFMqh", "vHFMqhW", "FMqhWvH"]))    #  True)
print(contain_all_rots("UDvG", ["vGUD", "UDvG", "GUDv", "DvGU"]))                                                                      #  True
print(contain_all_rots("sObPfw", ["ObPfws", "Cofuhqrmmzq", "wFvfcqU", "sObPfw", "bPfwsO", "PfwsOb", "wsObPf", "fwsObP"]))              #  True
print(contain_all_rots("KUckM", ["MKUck", "EDjfbQB", "GUPwzk", "SKZvilwnL", "UckMK", "KUckM", "kMKUc"]))                               #  False
print(contain_all_rots("FDIe", ["DIeF", "IeFD", "FDIe", "eFDI"]))                                                                      #  True
print(contain_all_rots("12341234", ["DIeF", "IeFD", "12341234", "41234123", "34123412", "23412341"]))                                  #  True