# Complete the function to return the swapped digits of a given two-digit integer
def swap_digits(num):
  # Your code here
  decenas = num//10
  unidades = num%10
  return (unidades*10+decenas)
   
# Invoke the function with any two-digit integer as its argument
print(swap_digits(79))
