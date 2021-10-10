def toBinary(n: str) -> str:
    bin = []
    # conver to Binary
    while (n > 1):
        if n % 2 == 1:
            bin.insert(0, "1")
        else:
            bin.insert(0, "0")
        n = n // 2
    if n == 1:
        bin.insert(0, "1")

    bin = ''.join([_ for _ in bin])    # convert from [] to string
    print(bin)
    return bin


def make_32_bit(bin: str) -> str:
    newBin = '0' * (32 - len(bin)) + bin    # append 0 to make 32-bit
    print(newBin)
    return newBin

def inverseBit(newBin: str) -> str:
    # inverse 0 -> 1, 1 -> 0
    nBin = ""
    for i in newBin:
        conversedDigit = "1" if i == '0' else "0"
        nBin += conversedDigit
    print(nBin)
    return nBin

def toDecimal(nBin: str) -> int:
    result = 0
    for i in range(len(nBin)):
        result = result * 2 + int(nBin[i])
    print(result)
    return result



def processBin(number: int) -> int:
    bin = toBinary(number)
    newBin = make_32_bit(bin)
    nBin = inverseBit(newBin)
    result = toDecimal(nBin)
    print(f'RESULT: {result}\n')

if __name__ == "__main__":
    processBin(4)       # OUTPUT: 4294967291
    processBin(3)       # OUTPUT: 2147483647
    processBin(1)       # OUTPUT: 4294967294
    processBin(2147483647)  # OUTPUT: 2147483648
    processBin(802743475)   # OUTPUT: 3492223820


