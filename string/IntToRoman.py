def intToRoman(number):
        dict = { " I": 1,
                 "IV": 4,
                  "V": 5,
                 "IX": 9,
                  "X": 10,
                 "XL": 40,
                  "L": 50,
                 "XC": 90,
                  "C": 100,
                 "CD": 400,
                  "D": 500,
                 "CM": 900,
                  "M": 1000
                }

        thousands = number // 1000
        sisa = number % 1000
        ninehundreds = sisa // 900
        sisa = sisa % 900
        fivehundreds = sisa // 500
        sisa = sisa % 500
        fourhundreds = sisa // 400
        sisa = sisa % 400
        hundreds = sisa // 100
        sisa = sisa % 100
        nineties = sisa // 90
        sisa = sisa % 90
        fifties = sisa // 50
        sisa = sisa % 50
        forties = sisa // 40
        sisa = sisa % 40
        tens = sisa // 10
        sisa = sisa % 10
        nines = sisa // 9
        sisa = sisa % 9
        fives = sisa // 5
        sisa = sisa % 5
        fours = sisa // 4
        ones = sisa % 4


        # print("thousands :" ,thousands)
        # print("9hundreds :" ,ninehundreds)
        # print("5hundreds: ", fivehundreds)
        # print("4hundreds: ", fourhundreds)
        # print("hundreds: ", hundreds)
        # print("ninety: ", nineties)
        # print("fifties: ", fifties)
        # print("forties: ", forties)
        # print("tens: ", tens)
        # print("nines: ", nines)
        # print("fives: ", fives)
        # print("fours: ", fours)
        # print("ones: ", ones)

        rdict = {v: k for k, v in dict.items()}
        print(rdict[1000]*thousands + rdict[900]*ninehundreds + rdict[500]*fivehundreds + rdict[400]*fourhundreds
              + rdict[100]*hundreds + rdict[90]*nineties + rdict[50]*fifties + rdict[40]*forties
              + rdict[10]*tens + rdict[9]*nines + rdict[5]*fives + rdict[4]*fours + rdict[1]*ones
              )

number = 1649
print("Converting ", number, " to roman numeral -> ", end="")
intToRoman(1649)
print()

"""
OUTPUT:
Converting  1649  to roman numeral -> MDCXLIX
"""
