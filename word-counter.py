linediv = "*" * 68
print(linediv)
print("Let's see which word appears the most in a text file of your choice")
print(linediv)
def main():
	fname = input("\nEnter file name: ")
	print("Counting...\n")

	try:
		fhandle = open(fname)
	except:
		print("The file you tried to open doesn't exist.\nPlease, try again...")
		main()

	counts = dict()
	for line in fhandle:
		words = line.split()
		for word in words:
			counts[word] = counts.get(word, 0) + 1

	bigword = None
	bigcount = None

	for word,count in counts.items():
		if bigcount is None or count > bigcount:
			bigword = word
			bigcount = count
			
	print("The word \"{}\" appears {} times".format(bigword, bigcount))
