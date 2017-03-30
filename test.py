import sys, helloWorld
def main():
	if len(sys.argv) > 1:
		name = sys.argv[1]
	else:
		name = "Osama"

	print "attempting test with name " + name
	
	assert helloWorld.printName(name) == "Hello World, I am " + name

	print "All assertion conditions met!"
	return True
	
if __name__ == "__main__":
	main()