import random
import sys
import time
import statistics

# Set recursion limit to avoid stack overflow
sys.setrecursionlimit(5000)

def coordinatesToBoard(coordinates):
    """
    Convert coordinates to a board representation.
    """
    board = [["_"] * n for _ in range(n)]
    for i in coordinates:
        board[i[0]][i[1]] = 'Q'
    return board

def countAttacks(coordinates):
    """
    Count the number of attacks on a given board.
    """
    count = 0
    for i in range(len(coordinates)):
        for j in range(len(coordinates)):
            if (abs(coordinates[i][0] - coordinates[j][0]) == abs(coordinates[i][1] - coordinates[j][1]) and coordinates[i] != coordinates[j]):
                # Diagonal attack
                count += 0.5
            if (coordinates[i][0] == coordinates[j][0] and coordinates[i] != coordinates[j]):
                # Horizontal attack
                count += 0.5
            # The function placeQueens doesn't add queens on the same column => there can't be vertical attacks
    return count

def hillClimbing(coordinates):
    """
    Basic Hill Climbing algorithm for the N-Queens problem.
    """
    if countAttacks(coordinates) != 0:
        chosenCoordinate = random.randint(0, len(coordinates) - 1)
        move = random.choice([-1, 1])
        coordinates2 = coordinates[:]
        if (coordinates2[chosenCoordinate][0] + move < len(coordinates) and coordinates2[chosenCoordinate][0] + move >= 0):
            coordinates2[chosenCoordinate][0] += move
        else:
            coordinates2[chosenCoordinate][0] -= move
        if countAttacks(coordinates2) < countAttacks(coordinates):
            hillClimbing(coordinates2)
    if (countAttacks(coordinates) == 0):
        return coordinates
    return []

def hillClimbingWithSidewaysMove(coordinates, sidewaysmoveLimit):
    """
    Hill Climbing algorithm with sideways moves for the N-Queens problem.
    """
    limit = sidewaysmoveLimit
    if countAttacks(coordinates) != 0:
        chosenCoordinate = random.randint(0, len(coordinates) - 1)
        move = random.choice([-1, 1])
        coordinates2 = coordinates[:]
        if (coordinates2[chosenCoordinate][0] + move < len(coordinates) and coordinates2[chosenCoordinate][0] + move >= 0):
            coordinates2[chosenCoordinate][0] += move
        else:
            coordinates2[chosenCoordinate][0] -= move
        if countAttacks(coordinates2) < countAttacks(coordinates):
            hillClimbingWithSidewaysMove(coordinates2, limit)
        elif countAttacks(coordinates2) == countAttacks(coordinates) and limit > 0:
            limit -= 1
            hillClimbingWithSidewaysMove(coordinates2, limit)
    if (countAttacks(coordinates) == 0):
        return coordinates
    return []

def hillClimbingWithSidewaysMoveRandomRestarts(coordinates, sidewaysmoveLimit, RandomrestartsLimit):
    """
    Hill Climbing algorithm with sideways moves and random restarts for the N-Queens problem.
    """
    limit = sidewaysmoveLimit
    restarts = RandomrestartsLimit
    if countAttacks(coordinates) != 0:
        chosenCoordinate = random.randint(0, len(coordinates) - 1)
        move = random.choice([-1, 1])
        coordinates2 = coordinates[:]
        if (coordinates2[chosenCoordinate][0] + move < len(coordinates) and coordinates2[chosenCoordinate][0] + move >= 0):
            coordinates2[chosenCoordinate][0] += move
        else:
            coordinates2[chosenCoordinate][0] -= move
        if countAttacks(coordinates2) < countAttacks(coordinates):
            hillClimbingWithSidewaysMoveRandomRestarts(coordinates2, limit, restarts)
        elif countAttacks(coordinates2) == countAttacks(coordinates) and limit > 0:
            limit -= 1
            if limit == 0 and restarts > 0:
                restarts -= 1
                new_coordinates = [[random.randint(0, n - 1), i] for i in range(n)]
                hillClimbingWithSidewaysMoveRandomRestarts(new_coordinates, limit, restarts)
            hillClimbingWithSidewaysMoveRandomRestarts(coordinates2, limit, restarts)
    if (countAttacks(coordinates) == 0):
        return coordinates
    return []

# Set the number of queens
n = 6
solutionCount = 0
times_solution = []
times_noSolution = []
runCount = 5000

# Run the algorithm multiple times
for _ in range(runCount):
    coordinates = [[random.randint(0, n - 1), i] for i in range(n)]
    start = time.time()
    solution = hillClimbingWithSidewaysMoveRandomRestarts(coordinates, 100, 10)
    end = time.time()
    if solution != []:
        solutionCount += 1
        times_solution.append(end - start)
    else:
        times_noSolution.append(end - start)

# Print results
print("The algorithm found the solution", solutionCount / runCount * 100, "percent of time")
print(statistics.mean(times_solution), "- average time spent on finding a solution")
print(statistics.mean(times_noSolution), "- average time spent till the algorithm asserted it didn't find a solution")
