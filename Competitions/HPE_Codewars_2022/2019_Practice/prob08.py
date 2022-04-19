# use a set

num_dict = {0:"ZERO",
            1:"ONE",
            2:"TWO",
            3:"THREE",
            4:"FOUR",
            5:"FIVE",
            6:'SIX',
            7:"SEVEN",
            8:'EIGHT',
            9:'NINE',
            10:'TEN',
            11:'ELEVEN',
            12:'TWELVE'}

nums = list(map(int, input().split()[:-1]))

letters_needed = {}
for num in nums:
	letter_num = num_dict[num]
	cur_letters_needed = {}
	for letter in letter_num:
		if letter in cur_letters_needed:
			cur_letters_needed[letter] += 1
		else:
			cur_letters_needed[letter] = 1
	for letter in cur_letters_needed:
		if letter in letters_needed:
			if letters_needed[letter] < cur_letters_needed[letter]:
				letters_needed[letter] = cur_letters_needed[letter]
		else:
			letters_needed[letter] = cur_letters_needed[letter]
out = ""
for num in nums:
	out += str(num) + " "
for letter in sorted(letters_needed.keys()):
	for i in range(letters_needed[letter]):
		out += letter + " "
print(out.strip())