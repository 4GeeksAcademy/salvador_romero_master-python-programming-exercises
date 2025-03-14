# Complete the function "digits_sum" so that it prints the sum of a three-digit number
def digits_sum(num):
  centenas = int(num/100)
  decenas = int((num%100)/10)
  unidades = num%10
  return centenas + decenas + unidades


# Invoke the function with any three-digit number
print(digits_sum(252))
