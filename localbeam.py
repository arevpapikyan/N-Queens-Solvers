import pandas as pd
import random
import sys
import copy
import time

sys.setrecursionlimit(5000)

def coordinatesToBoard(coordinates):
    board = [["_"] * n for _ in range(n)]
    for i in coordinates:
        board[i[0]][i[1]] = 'Q'
    return board

def countAttacks(coordinates):
    count = 0
    for i in range(len(coordinates)):
        for j in range(len(coordinates)):
            if abs(coordinates[i][0] - coordinates[j][0]) == abs(coordinates[i][1] - coordinates[j][1]) and coordinates[i] != coordinates[j]:
                count += 1
            if coordinates[i][0] == coordinates[j][0] and coordinates[i] != coordinates[j]:
                count += 1
    return count

def generateSuccessors(coordinates):
    successors = []
    for i in range(len(coordinates)):
        current_column = coordinates[i][1]
        for j in range(n):
            if j != coordinates[i][0]:  # Avoid placing a queen in the same row
                new_state = copy.deepcopy(coordinates)
                new_state[i] = [j, current_column]
                successors.append(new_state)
    return successors

def k_smallest(lst, attacks, k):
    sorted_attacks = sorted(attacks)
    smallest = []
    for i in range(k):
        ind = attacks.index(sorted_attacks[i])
        if lst[ind] not in smallest:
            smallest.append(lst[ind])
    return smallest

def localBeam(k, n):
    def generate_initial_state(n):
        return [[random.randint(0, n-1), i] for i in range(n)]
    def is_goal_state(coordinates):
        return countAttacks(coordinates) == 0
    def local_beam_search(initial_states, k):
        current_states = initial_states
        limit=100
        while limit>0:
            limit-=1
            next_states = []
            for state in current_states:
                successors = generateSuccessors(state)
                for successor in successors:
                    if is_goal_state(successor):
                        return successor
                    next_states.append(successor)
            attacks = [countAttacks(state) for state in next_states]
            current_states = k_smallest(next_states, attacks, k)
        if limit==0 and 0 not in attacks:
            return 'no solution was found in 100 steps'
    initial_states = [generate_initial_state(n) for _ in range(k)]
    solution = local_beam_search(initial_states, k)
    if isinstance(solution, list):
        return pd.DataFrame(coordinatesToBoard(solution)).to_string(index=False, header=False)
    else:
        return solution

n = 5
k = 5
start = time.time()
solution=localBeam(k, n)
end=time.time()
print(solution)
print(end-start)