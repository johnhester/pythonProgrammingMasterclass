# print('Today is a good day to learn Python!')
# print("Python is fun")
# print("Python's strings are easy to use")
# print('We can even include "quotes" in strings!')
#
# print("hello " + "world")

greeting = 'Hello'
# name = input("Please enter your name: ")
name = 'John'
print(greeting + ' ' + name)

age = 31
print(type(greeting))
print(type(age))

age_in_words = "2 years"
#f-strings work similarly to replacement fields, but allow direct variable insertion
#replacement field formatting also works on f-strings
print(name + f" is {age} years old")

print(f"Pi is approximately {22/7:12.50f}")
pi = 22/7
print(f"Pi is approximately {pi:12.50f}")

