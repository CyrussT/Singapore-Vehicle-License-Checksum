"""
Sources: 
https://en.wikipedia.org/wiki/Vehicle_registration_plates_of_Singapore#Checksum
https://sgwiki.com/wiki/Vehicle_Checksum_Formula

"""

import string

def checksum(license):
    suffixTable = ["A","Z","Y","X","U","T","S","R","P","M","L","K","J","H","G","E","D","C","B"]
    suffixValue = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]

    license = license.upper()
    prefixLength = prefixIndex(license)
    prefixValue = 0

    if prefixLength == 3:
        prefixValue = calculatePrefixValue(license[1:prefixLength])
    elif prefixLength == 2:
        prefixValue = calculatePrefixValue(license[:prefixLength])
    elif prefixLength == 1:
        prefixValue = calculatePrefixValue(license[0])
    else:
        print("Invalid prefix length")
        raise ValueError
    
    suffixValue = calculateSuffixValue(license[prefixLength:])
    totalValue = prefixValue + suffixValue
    last = suffixTable[totalValue % 19]
    return license + last


def prefixIndex(license):
    for i in license:
        if i in string.digits:
            return license.index(i)


def calculatePrefixValue(prefix):
    sum = []
    for i in prefix:
        sum.append(string.ascii_uppercase.index(i) + 1)
    return sum[0] * 9 + sum[1] * 4


def calculateSuffixValue(suffix):
    num = [5, 4, 3, 2]
    sum = 0
    for i in range(-1, - len(suffix) -1, -1):
        sum += num[i] * int(suffix[i])
    return sum

if __name__ == "__main__":
    checker = input("Enter license plate (without the last alphabet): ")
    print(checksum(checker))