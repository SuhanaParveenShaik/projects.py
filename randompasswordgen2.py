import random
import string

letters = string.ascii_letters
numbers = string.digits
specialchar = string.punctuation

print(letters, type(letters))
print(numbers, type(numbers))
print(specialchar, type(specialchar))

#type conversion(optional)

letters = str(letters)
numbers = str(numbers)
print(type(numbers))

#creating password
pass_len = 12
result = [random.choice(letters + numbers + specialchar) for i in range(pass_len)]
print(result)

