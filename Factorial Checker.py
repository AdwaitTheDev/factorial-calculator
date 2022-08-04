number = int(input('Enter The Number To Find Its Factorial: '))
factorial = 1

if number <= 0:
    print('There cant be factorial for this!')

elif number == 0:
    print('The factorial of 0 is 1!')

else:
    for i in range(1,number+1):
        factorial = factorial * i
    print('The factorial of',number,'is',factorial)


