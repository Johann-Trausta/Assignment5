# The program asks you first for the length of the sequence (n), the program then prints out the numbers from 1 upto n.




n = int(input("Enter the length of the sequence: ")) # Do not change this line

n_1=1
n_2=2
n_3=3

for i in range(1, n+1):
    if i == 1:
        print(n_1)
    elif i == 2:
        print(n_2)
    elif i == 3:
        print(n_3)
    else:
        n_summa=n_1+n_2+n_3
        n_1=n_2
        n_2=n_3
        n_3=n_summa
        print(n_summa)