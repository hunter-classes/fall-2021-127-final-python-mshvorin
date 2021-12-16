def isincreasing(list):
    index = 0
    for f in range(len(list)-1):
        if list[index] < list [index + 1]:
            index += 1
        else:
            return False
    return True
        
def NumConvert(list):
    converted = ""
    for num in list:
        converted += str(num)
    return int(converted)

def BinConverter(Binary):
    total = 0
    BinaryInts = []
    for int in (str(Binary)):
        BinaryInts += int
    BinaryInts.reverse()
    for i,v in enumerate(BinaryInts):
        if v == "1":
            total += pow(2,i)
        else:
            pass
    return total
print("------------------- Question 1 ----------------\n\n Write a function named isIncreasing that takes a list of integers as a parameter. isIncreasing should return True if it continually increases. That is given a parameter list L, then L[0] < L[1] < L[2] etc. otherwise return False.\n")
print("Input:\n\n print(isincreasing([1,4,7,9])) \n print(isincreasing([1,2,9,6])) \n print(isincreasing([1,1,7,9]))\n\nOutput:\n")
print(isincreasing([1,4,7,9]))
print(isincreasing([1,2,9,6]))
print(isincreasing([1,1,7,9]))
print("------------------- Question 2 ----------------\n\n Write a function named NumConvert. It should take a list of single digit numbers and convert it to an integer and return it.\n")
print("Input:\n\n print(NumConvert([3,5,1])) \n print(NumConvert([5,9,9,1,4])) \n print(NumConvert([1,0,1,4,6,2,5]))\n\nOutput:\n")
print(NumConvert([3,5,1]))
print(NumConvert([5,9,9,1,4]))
print(NumConvert([1,0,1,4,6,2,5]))
print("------------------- Question 3 ----------------\n\n Write a function named BinConvert that takes a string representing a binary number and returns an integer with that number converted to decimal.\n")
print("Input:\n\n print(BinConverter(11)) \n print(BinConverter(1011)) \n print(BinConverter(10010))\n\nOutput:\n")
print(BinConverter(11))
print(BinConverter(1011))
print(BinConverter(10010))
