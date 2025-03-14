# Complete the function to return the total cost in dollars and cents of (n) cupcakes
def total_cost(d, c, n):
    total_centavos = c*n
    centavos = total_centavos%100
    dolares = d*n + total_centavos//100
    return (dolares,centavos)


# Invoke the function with three integers: total_cost(dollars, cents, number_of_cupcakes)
print(total_cost(15,60,4))
