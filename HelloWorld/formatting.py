#replacement fields can be formatted
#{1:1} add a colon and a second arg to expand your field width
# < will left align a value, > will right align a value, ^ will center a value
# for i in range(1,13):
#     print("No. {0:2} squared is {1:<3} and cubed is {2:^4}".format(i, i**2, i**3))


print()
#field witdth of 12
print("Pi is approximately {0:12}".format(22/7))
#floating point value designated by 'f'
print("Pi is approximately {0:12f}".format(22/7))
#.50 represents 50 characters of precision and precision overrides field width
print("Pi is approximately {0:12.50f}".format(22/7))
print("Pi is approximately {0:52.50f}".format(22/7))
print("Pi is approximately {0:62.50f}".format(22/7))
print("Pi is approximately {0:<72.50f}".format(22/7))
print("Pi is approximately {0:<72.54f}".format(22/7))

#specific designations are optional and fields can by automatically inferred
#
for i in range(1, 13):
    print("No. {} squared is {} and cubed is {:4}".format(i, i**2, i**3))