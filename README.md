# Hill Climbing and Local Beam Search Algorithms in Python

## Hill Climbing Search Algorithm

This implementation includes three variants of the hill climbing search algorithm: basic hill climbing, hill climbing with sideways moves, and hill climbing with sideways moves and random restarts.

### Functions

#### 1. `hillClimbing`

- **Parameters**: `coordinates` - the coordinates of the initial state board.
- **Output**: Outputs either the solution or asserts that no solution was found.

#### 2. `hillClimbingWithSidewaysMove`

- **Parameters**:
  - `coordinates` - the coordinates of the initial state board.
  - `limit` - the limit of sideways moves.
- **Output**: Outputs either the solution or asserts that no solution was found.

#### 3. `hillClimbingWithSidewaysMoveRandomRestarts`

- **Parameters**:
  - `coordinates` - the coordinates of the initial state board.
  - `limit` - the limit of sideways moves.
  - `restarts` - the number of restarts allowed.
- **Output**: Outputs either the solution or asserts that no solution was found.

## Local Beam Search Algorithm

This implementation includes a local beam search algorithm.

### Function

#### `localBeam`

* **Parameters** :
* `num_queens` - the number of queens.
* `num_initial_states` - the number of initial states.
* **Output** : Outputs either the solution or asserts that no solution was found.
