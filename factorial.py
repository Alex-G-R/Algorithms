
# Define the function factorial.
# factorial mean !x so bassicly if you have !5
# it will be equal to 1 * 2 * 3 * 4 * 5
def factorial(x):
    # If the provided number is 1 the result will always be one.
    if x == 1:
        return 1
    else: # Use recursion to multiply x * x - 1 so if the x is 3 it will go something like this:
          # 3 * (3 - 1) * (2 - 1) 
        return x * factorial(x - 1)
    
print(factorial(5))