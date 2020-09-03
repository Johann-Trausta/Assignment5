num_int = int(input("Input a number: "))    # Do not change this line
max_int=0
while True:

    if num_int<0:
        break
    max_int=max(num_int, max_int)
    num_int = int(input("Input a number: ")) 
# Fill in the missing code
print("The maximum is", max_int)
