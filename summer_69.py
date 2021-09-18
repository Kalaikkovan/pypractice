# sum the numbers from the list [1,2,3,4,5,6,7,8,9,10] excluding 6 to 9

def summer_69(arr):
    num = 0 
    add = True
    for i in arr:
        while add:
            if i!=6:
                num = num + i
                break
            else:
                add = False
                break
        while not add:
            if i!=9:
                break
            else:
                add = True
    return num

sumof69 = summer_69([1,2,3,4,5,6,7,8,9,10,11,12,13])
print(sumof69)