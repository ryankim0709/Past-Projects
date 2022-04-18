alphabet = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' '}

numbers = {'1', '2', '3', '4', '5', '6', '7', '8', '9', '0'}

# 18

str1 = '/*Jon is @developer & musician!!'

for x in range(0, len(str1)):
    if not str1[x].lower() in alphabet:
        str1 = str1[:x]+"#"+str1[x+1:]

print(str1)

# 17

str1 = "Emma25 is Data scientist50 and AI Expert"

words = str1.split()

letter = False
number = False

for word in words:
    letter = False
    number = False
    for char in word:
        if char in numbers:
            number = True

        elif char in alphabet:
            letter = True

    if number and letter:
        print(word)

# 16

str1 = 'I am 25 years and 10 months old'

final = ""

for char in str1:
    if char in numbers:
        final = final + char

print(final)

# 15

str1 = "/*Jon is @developer & musician"

final = ""

for char in str1:
    if char.lower() in alphabet or char in numbers:
        final = final + char

final = " ".join(final.split())

print(final)

# 14

str_list = ["Emma", "Jon", "", "Kelly", None, "Eric", ""]

print("Original list of string")
print(str_list)

for element in str_list:
    if not type(element) == str or len(element) < 1:
        str_list.remove(element)

print("After removing empty strings")
print(str_list)
