def romanToInt(str):
    dict = { "I": 1,
             "V": 5,
             "X": 10,
             "L": 50,
             "C": 100,
             "D": 500,
             "M": 1000
            }

    sum = 0
    last = "I"      # use "I", because "I" is the smallest

    for i in str[::-1]:
        if dict[i] < dict[last]:
            sum -= dict[i]
        else:
            sum += dict[i]
        last = i
    return sum

roman = "DXLII"
res = romanToInt(roman)
print(f"\n{roman} = {res}")     # 542

roman = "XXXVI"
res = romanToInt(roman)
print(f"\n{roman} = {res}")     # 36

roman = "MXXIII"
res = romanToInt(roman)
print(f"\n{roman} = {res}")     # 1023

roman = "MDCXLIX"
res = romanToInt(roman)
print(f"\n{roman} = {res}")     # 1649


#=======================================
print("*********************************************")
def romanToInt2(str):
    dict = { "I": 1,
             "V": 5,
             "X": 10,
             "L": 50,
             "C": 100,
             "D": 500,
             "M": 1000
            }

    convert = { "IV": "IIII",
                "IX": "VIIII",
                "XL": "XXXX",
                "XC": "LXXXX",
                "CD": "CCCC",
                "CM": "DCCCC"
              }

    for k, v in convert.items():
        str = str.replace(k, v)         # tricky !!!

    print(f"Converted String: {str}")
    return sum([dict[numeral] for numeral in str])



###
###TEST
roman = "DXLII"
res = romanToInt2(roman)
print(f"{roman} = {res}\n")     # Converted String: DXXXXII
                                # sum([500, 10, 10, 10, 10, 1, 1])
                                # DXLII = 542

roman = "XXXVI"
res = romanToInt2(roman)
print(f"{roman} = {res}\n")     # Converted String: XXXVI
                                # sum([10, 10, 10, 5, 1])
                                # XXXVI = 36

roman = "MXXIII"
res = romanToInt2(roman)
print(f"{roman} = {res}\n")     # Converted String: MXXIII
                                # sum([1000, 10, 10, 1, 1, 1])
                                # MXXIII = 1023

roman = "MDCXLIX"
res = romanToInt2(roman)
print(f"{roman} = {res}\n")      # 1649

