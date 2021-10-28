number=int(input())
number_copy=number
reversed_number=0
while(number!=0):
  reversed_number=(reversed_number*10)+(number%10)
  number=int(number/10)
if number_copy==reversed_number:
  print("yes")
else:
  print("no")