#!/usr/bin/env python3

def admin_login(username, password):
    if (username =='admin' or username=='ADMIN') and password=='12345':
        return('Access granted')
    else :
        return('Access denied')
        

def hows_the_weather(temperature):
    # your code here
#     hows_the_weather(33)
# # "Brisk!"
# hows_the_weather(99)
# # "Too dang hot"
# hows_the_weather(75)
# # "Perfect!"
     if temperature<= 40:
         return("It's brisk out there!")
     elif (temperature>40 and temperature<65):
         return("It's a little chilly out there!")
     elif temperature==75:
         return("It's perfect out there!")
     elif temperature>80 :
         return("It's too dang hot out there!")

def fizzbuzz(num):
    # your code here
    # Write a function fizzbuzz() takes in a number. For multiples of three, return "Fizz" instead of the number.
    # For the multiples of five, return "Buzz". For numbers 
    # which are multiples of both three and five, return "FizzBuzz". For all other numbers, just return the number itself.
    if num%3==0 and num%5==0:
        return('FizzBuzz')
    elif num%5==0:
        return('Buzz')
    elif num%3==0:
        return('Fizz')
    else:
        return num

def calculator(operation, num1, num2):
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        return num1 / num2
    else:
        print('Invalid operation!')
        return(None)
