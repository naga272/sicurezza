i = 0
while True:
	with open(f"./file{i}.txt", "w") as f_in:
		f_in.write("c")
		i+=1