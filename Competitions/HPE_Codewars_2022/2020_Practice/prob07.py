colors = input()
out = ""
while colors != "":
	colors = colors.split()
	# Check if it's dark/light
	if "BLACK" in colors:
		colors.remove("BLACK")
		other_color = colors[0]
		out += f"\nDARK {other_color}"

	elif "WHITE" in colors:
		colors.remove("WHITE")
		other_color = colors[0]
		out += f"\nLIGHT {other_color}"


	# Mixing primary colors

	elif "RED" in colors and "YELLOW" in colors:
		out += "\nORANGE"
	elif "YELLOW" in colors and "BLUE" in colors:
		out += '\nGREEN'
	elif "BLUE" in colors and "RED" in colors:
		out += '\nPURPLE'

	elif len(set(colors)) == 1:
		out += f"\n{colors[0]}"
	colors = input()

print(out)