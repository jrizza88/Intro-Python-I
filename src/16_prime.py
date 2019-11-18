# Write a program to determine if a number, given on the command line, is prime.

user_input = int(input('check if number is prime: '))

# num = input("Enter a number: ")
# num = int(num)

def check_prime(num):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                print(num, 'is not a prime...')
                print(i,"times",num//i,"is",num)
                break
            else: 
                print(num, 'is a prime')
                break

    else:
        print(f'{num} is not a prime..')



if check_prime(user_input):
    print(user_input)