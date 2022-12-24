#python3 has 5 sequence types built in
## string, list, tuple, range, bytes, and bytearray

#What is a sequence?
#an ordered set of items


string1 = "he's "
string2 = "probably "
string3 = "pining "
string4 = "for the "
string5 = 'fjords'
#both of the following work
print(string1 + string2 + string3 + string4 + string5)
print("he's " "probably " "pining " "for the " "fjords")
#strings can be 'multiplied' to repeat the string multiple times
print("Hello " * 5)

print("Hello " * (5 + 4))
print("Hello " * 5 + "4")

today = "friday"
#is 'day' in 'friday'
print("day" in today) #true
#is 'fri' in 'friday
print("fri" in today) #true
#is 'thur' in friday
print("thur" in today) #false
#is 'parrot' in 'fjord
print("parrot" in "fjord") #false