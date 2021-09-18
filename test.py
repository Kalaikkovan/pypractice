def myfunc(string):
    mynewString = []
    string = string.lower()
    if len(string)>1:
        for i in string:
            mynewString.append(i)
    k=0
    for j in mynewString:
        
        if k>=1 and k%2 != 0:
            tempstr = mynewString[k]
            mynewString[k]= tempstr.upper()
        k +=1
            
    return mynewString
    #print(mynewString)



def listtostring(mynewString):
    string =''
    for i in mynewString:
        string += i;
    return string

mynewString = myfunc('asakdhklfhlkfh')
listtostring(mynewString)