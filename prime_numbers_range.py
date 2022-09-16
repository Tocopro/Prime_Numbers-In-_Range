# user input of a positive number greater than 1
print("Printing all the Prime numbers from 0 to the Number input by the User")
user_input = int(input("Enter a Number: "))
test_number = 0
print("All the Prime Numbers between 2 and", user_input)
# function test if the number is positive and greater than 1
if user_input > 1:
    test_number = user_input
# for loop test if the number in the range is a prime number or not
for i in range(2, test_number + 1):
    # loop test of all the numbers in the range up to the number the user input
    # if the number is divisible by another number in the range then it isi not a prime number
    for j in range(2, i):
        if i % j == 0:
            break
    # if the numbers passed in the range have no numbers to evenly divide them, they are passed on tho be printed as
    # the prime number
    else:
        print(i, end=' ')

