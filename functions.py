
polynomials = {
    # Original name - CRC-4-ITU
    # Polynomial - x^4 + x + 1
    "CRC4": "10011",
    # Original name - CRC-8
    # Polynomial - x^8 + x^7 + x^6 + x^4 + x^2 + 1
    "CRC8": "111010101",
    # Original name - CRC-16-CCITT
    # Polynomial - x^16 + x^12 + x^5 + x^1
    "CRC16": "10001000000100001",
    # Original name CRC-32-IEEE 802.3
    # Polynomial - x^32 + x^26 + x^23 + x^22 + x^16 + x^12 + x^11 + x^10 + x^8 + x^7 + x^5 + x^4 + x^2 + x + 1
    "CRC32": "100000100110000010001110110110101"
}


def mod(divisible, divisor):
    """ Function mod is polynomial division without transfer """
    divisibleBinLength = len(bin(divisible)[2:])  # get length of binary number
    divisorBinLength = len(bin(divisor)[2:])  # get length of binary number

    while divisibleBinLength >= divisorBinLength:
        difference = divisibleBinLength - divisorBinLength

        # adding extra bits to divisor, because length of divisor have to has the same length like divisible.
        # after that making addition modulo 2 "XOR"
        divisible = divisible ^ (divisor << difference)

        divisibleBinLength = len(bin(divisible)[2:])

    return divisible


def getPosSumFile(pathToFile):
    """ This function returns the sum of all symbols in a file."""
    file = open(pathToFile, 'rb')
    data = file.read(1)  # getting the first byte
    sum = 0

    while data:
        sum += ord(data)  # get decimal position symbol and add to total sum
        data = file.read(1)  # # getting other bytes

    return sum


def getPosSumText(text):
    """ This function returns the sum of all symbols in a string."""
    sum = 0
    for symbol in text:
        sum += ord(symbol)  # get decimal position from symbol and add to total sum

    return sum


def calculateCheckSum(posSum, polynomial):
    """ This function returns the remainder of source data (sum of symbols positions) and polynomial."""
    divisor = int(polynomial, 2)  # convert binary polynomial to decimal view

    # calculate number of extra bits for source data.
    # these numbers are number bits of checksum
    offset = len(polynomial) - 1
    remainder = mod(posSum << offset, divisor)  # calculate remainder from source data and polynomial

    return remainder


def verifyCheckSum(posSum, checkSum, polynomial):
    """ This function returns bool value.
        Find remainder from posSum + checkSun and polynomial.
        If remainder == 0: return True. It means, that text or file has no integrity violation.
    """
    divisor = int(polynomial, 2)  # convert binary polynomial to decimal view

    # concatenating sum of symbols positions and remainder (checksum) in binary view
    # after that find decimal view of binary number
    sumPosAndCheckSum = int(bin(posSum)[2:] + f'{checkSum:0{len(polynomial)-1}b}', 2)
    remainder = mod(sumPosAndCheckSum, divisor)  # finding remainder

    if remainder == 0:
        return True
    else:
        return False
