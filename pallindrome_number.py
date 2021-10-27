
# Program to check if number is palindrome or not

def check_palindrome(input_number):
        original_number = input_number
        temp_number = 0
        while(True):
                if input_number == 0:
                        break
                temp_number = temp_number*10 + input_number%10
                input_number = int(input_number/10)
        if temp_number == original_number:
            print(True)
        else:
            print(False)

check_pallindrome(12321)
