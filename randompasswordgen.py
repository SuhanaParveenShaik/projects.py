import random
import string
first = string.ascii_letters
second = string.digits
third = string.punctuation
#print(first)
#print(second)
#print(third)
pass_len = 10
password = ""
for i in range (pass_len):
   password += random.choice(first+ second + third)
   print(password)