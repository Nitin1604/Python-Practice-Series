# Practice Series 11

number = int(input('Enter any number to check armstrong number: '))
sum = 0
order = len(str(number))
copy_number = number 
while(number>0):
    digit = number%10
    sum += digit ** order
    number = number // 10

if(sum == copy_number):
    print(f"{copy_number} is an armstrong number")
else:
    print(f"{copy_number} is not an armstrong number")
