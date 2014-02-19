from collections import deque
N, M, T = map(int, raw_input().split())

matrix = [raw_input().split() for row in xrange(N)]
for row in xrange(N):
	for col in xrange(M):
		if matrix[row][col] == 'S':
			startCoords = (row, col)

class State:
	def __init__(self, coords, steps, lives, celltype, keys):
		self.coords = coords
		self.steps = steps
		self.lives = lives
		self.celltype = celltype
		self.keys = keys

	def getSuccessors(self):
		successors = []
		coords = self.coords
		possibleCoords = [(coords[0] - 1, coords[1]), (coords[0] + 1, coords[1]), (coords[0], coords[1] - 1), (coords[0], coords[1] + 1)]
		for cs in possibleCoords:
			if cs[0] >= 0 and cs[0] < N and cs[1] >= 0 and cs[1] < M:
				celltype = matrix[cs[0]][cs[1]]
				if celltype == 'O':
					neighbor = State(cs, self.steps+1, self.lives, celltype, self.keys)
					successors.append(neighbor)
				elif celltype == 'M':
					if self.lives > 1:
						neighbor = State(cs, self.steps+1, self.lives-1, celltype, self.keys)
						successors.append(neighbor)
				elif celltype == 'E':
					neighbor = State(cs, self.steps+1, self.lives, celltype, self.keys)
					successors.append(neighbor)
		return successors

	def isGoalState(self):
		return self.celltype == 'E'

def BFS():
	startState = State(startCoords, 0, T, 'S', [])
	fringe = deque()
	fringe.append(startState)

	visited = [[[False for col in xrange(M)] for row in xrange(N)] for life in xrange(T)]
	while fringe:
		currentState = fringe.popleft()
		coords = currentState.coords
		if visited[currentState.lives-1][coords[0]][coords[1]]:
			continue
		else:
			if currentState.isGoalState():
				return currentState.steps
			else:
				visited[currentState.lives-1][coords[0]][coords[1]] = True
				fringe.extend(currentState.getSuccessors())
	return -1

print BFS()
