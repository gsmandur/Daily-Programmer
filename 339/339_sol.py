# Question at:
# https://www.reddit.com/r/dailyprogrammer/comments/7btzrw/20171108_challenge_339_intermediate_a_car_renting/

# determines the optimal solution to serve the most rental requests)
# uses greedy solution, sorting by the rental finish date
# input is n the number of requests and and array of pairs for the start->end periods 
import sys
from operator import itemgetter


# Greedy Algo, give rentals based on earliest end dates
# inputs: the number of requests and a list of tuples for (start,end) requests
# returns the list of accepted rental requests
def RentSolver(n, startEndList):
	# first sort by earliest start date, then by earliest end date
	startEndList = sorted(startEndList, key=itemgetter(0))
	startEndList = sorted(startEndList, key=itemgetter(1))

	# remove any element that has start date before end date
	startEndList[:] = [x for x in startEndList if not (x[0] > x[1]) ]
	for x in startEndList: print (x[0],x[1])

	# create rental list with first element set
	rentalList = [startEndList[0]]
	latestRental = startEndList[0]

	# add elements to rentalList
	for period in startEndList[1:]:
		# accept request if period starts after the last accepted request ends
		if period[0] > latestRental[1]:
			rentalList.append(period)
			latestRental= period	

	return rentalList



def main():
	# read input from file
	# usage: py script.py input.in

	# read and parse input
	f = open(sys.argv[1], 'r')
	n = int(f.readline())
	xList = [int(i) for i in str.split(f.readline())]	# coverts input into int list 
	yList = [int(i) for i in str.split(f.readline())] 

	# store requests in list	
	startEndList = []
	for i in range(n):
		startEndList.append( (xList[i],yList[i]) )	# array of tuples (start, end)

	rentalList = RentSolver(n, startEndList)
	print(rentalList)		



main()

