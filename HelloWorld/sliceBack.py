letters = "abcdefghijklmnopqrstuvwxyz"
#returns entire string printed in reverse order thanks to -1 step
backwards = letters[::-1]

print(backwards)
#slice challenge: produce the following strings by slicing
#qpo
print(letters[16:13:-1])
#edcba
print(letters[4::-1])
#last 8 chars in reverse order
print(letters[:-9:-1])

print(letters[-4:])
print(letters[-1:])
print(letters[:1])

