def fix_teen(n):
    if n in range(13,20):
        if n not in range(15,17):
            return True
    return False
def no_teen_sum(a, b, c):
  mylist = [a,b,c]
  teen = False
  sum = 0
  for i in mylist:
    teen = fix_teen(i)
    if not teen:
      sum += i
  return sum

no_teen_sum(2,1,15)
  
