table = 1

while table < 13:
	count = 0
	for i in range(1000):
		if i % table == 0:
			print(str(count) + " x " + str(table) + " = " + str(i))
			count += 1
			if count > 12:
				break
	table += 1
print("Done!")