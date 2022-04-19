total, num_items = map(int, input().split())
items = []
for i in range(num_items):
	name, price = input().split()
	items.append((name, int(price)))


things = sorted(items, key=lambda x: x[1])
affordable = []
for name, price in things:
	if total >= price:
		affordable.append(name)
		total -= price
	else:
		break

for item in items:
	if item[0] in affordable:
		print(f"I can afford {item[0]}")
	else:
		print(f"I can't afford {item[0]}")
if len(affordable) == 0:
	print("I need more Yen!")

print(total)