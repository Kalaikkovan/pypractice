def round10(num):
    remainder = num%10
    quotient = num//10
    if remainder<5:
        return num - remainder
    else:
        return 10 *(quotient+1)
    
def round_sum(a, b, c):
  sum = 0
  for i in (a,b,c):
    sum += round10(i)
  return sum

round_sum(16,17,18)