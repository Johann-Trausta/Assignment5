# The program first asks to input a number, the program then goes into while where choose another number until you choose a negative number, when you choose a negative number the while breaks and the program prints out the max_int or the highest number you had put in on your input



num_int = int(input("Input a number: "))    # Do not change this line
max_int=0
while True:

    if num_int<0:
        break
    max_int=max(num_int, max_int)
    num_int = int(input("Input a number: ")) 
# Fill in the missing code
print("The maximum is", max_int)
