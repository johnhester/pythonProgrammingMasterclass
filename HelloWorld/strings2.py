# Like most programming languages, Strings and Arrays are 0-indexed in Python
#         01234567890123
parrot = "Norwegian Blue"

print(parrot)
#indexing challenge: print 'we win' vertically using only indexes on the variable parrot
# print(parrot[3] + "\n" + parrot[4] + "\n" + parrot[9] + "\n" + parrot[3] + "\n" + parrot[6] + "\n" + parrot[8])

print()
#negative indexing also works
#starts at -1, zero is already taken
#previous indexing challenge using negative indexing
# print(parrot[-11] + '\n' + parrot[-10] + '\n' + parrot[-5] + '\n' + parrot[-11] + '\n' + parrot[-8] + '\n' + parrot[-6])

#when splicing strings in python, the last number is not included ("up to, but not including")
# print(parrot[0:9])
# print(parrot[3:5])
# #Python will begin splicing from index 0 if you do not provide a starting value, but you MUST supply the colon
# print(parrot[:9])
# #Python will slice to the end of the string automatically if you do not provide a second value, but you must still supply the colon
# print(parrot[10:])
# #Python will print the entire string if you only provide the colon
# #not always useful, but it does produce a copy of the original string
# print(parrot[:])
#positive and negative indexing can be used together
# print(parrot[-4:-2])
# print(parrot[-4: 12])


#You can include a 3rd argument to 'Step' through the string in increments (2: every other char, 3: every third char, etc)
# print(parrot[0:6:3])

number = "9,223;372:036 854;775,807"
seperators = number[1::4]
print(seperators)

values = "".join(char if char not in seperators else " " for char in number).split()
print([int(val) for val in values])