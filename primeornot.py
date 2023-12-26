number = int(input("enter the number:"))
flag = 0
if number>1:
    for i in range(2,number):
        if number%i==0:
            flag = 1
            break
    if flag == 1:
        print(number," is not a prime number.")
    else:
        print(number," is a prime number.")
else:
    print(number," is not a prime number.")