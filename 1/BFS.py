# Python3 Program to print BFS traversal
# from a given source vertex. BFS(int s)
# traverses vertices reachable from s.
from collections import defaultdict


# This class represents a directed graph
# using adjacency list representation
class Card:

	def __init__(self, color, number):
		self.color = color
		self.number = number


if __name__ == '__main__':
	# k = number of decks
	# m = number of colors
	# n = number of each color of cards (from )
	k, m, n = input().split()


