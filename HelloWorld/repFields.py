age = 24

#normally a number added to a string throws an error, but with type coercion you can get around that
# print("My age is " + str(age) + " years")

#python3 has an alternative method
#replacement field is represented by {0}, and the first value in .format() will display there
print("My age is {0} years".format(age))

#the replacement method works best when you have multiple values
print("There are {0} days in {1}, {2}, {3}, {4}, {5}, {6}, and {7}"
    .format(31, "Jan", "Mar", "May", "Jul", "Aug", "Oct", "Dec"))

#replacement field operators don't have to be in order and can be repeated
print("Jan: {2}, Feb: {0}, Mar: {2}, Apr: {1}, May: {2}, Jun: {1}, Jul: {2}, Aug: {2}, Sep: {1}, Oct: {2}, Nov: {1}, Dec: {2}"
      .format(28, 30, 31))

print("""Jan: {2}
Feb: {0}
Mar: {2}
Apr: {1}
May: {2}
Jun: {1}
Jul: {2}
Aug: {2}
Sep: {1}
Oct: {2}
Nov: {1}
Dec: {2}""".format(28, 30, 31))