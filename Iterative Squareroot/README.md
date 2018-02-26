######################
#Iterative Squareroot#
######################

I was asked this question during an interview and I thought the implementation would be fun:

		"How would you find the squareroot of a number without the squareroot (or exponential) functions?"

This is an implementation of the answer I gave:

- Find the digits in the number
- Find a range of the squareroot of a number of that size
- Binary search and check until we are within some threshold of distance


The program outputs the number of tail recursions required to find the solution.

I believe rather than binary search, we could calculate a better heurisitic (than cutting the list in half) if we measured the error distance.
I think that will be the next update (if there is one).