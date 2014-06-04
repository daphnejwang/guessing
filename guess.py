import random

def get_guess():
    while True:
	try:
	    guess = int(raw_input())
      	    return guess
	    break
	except ValueError:
	    print "Please enter an integer."

def main():
	target_num = random.randint(1,100)
	num_guesses = 1
	
	print "Howdy, what's your name?"
	name = raw_input("(type in your name) ")
	print "%s, I'm thinking of a number between 1 and 100. Try to guess it" % name
	print target_num

	guess = get_guess()
	
	while guess != target_num:
		num_guesses += 1
		if guess > target_num:
			print "Your guess is too high! Try again."
		else:
			print "Your guess is too low! Try again."
		guess = get_guess()

	print "Well done! You've got it right in %d of guesses." % num_guesses

if __name__ == "__main__":
	main()

