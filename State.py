from queue import Queue

# Represents a state of the board
class State:
  def __init__(self, board, cost, prev_move):
    self.board = board
    self.cost = cost
    self.prev_move = prev_move

# Returns the sequence of moves required to solve the board
def search(initial_state, goal_state, strategy):
  if strategy == "uniform_cost":
    # Use a priority queue to perform uniform cost search
    queue = PriorityQueue()
  else:
    # Use a regular queue to perform A* search
    queue = Queue()

  # Add the initial state to the queue
  queue.put(initial_state)

  # Keep track of the visited states
  visited = set()

  while not queue.empty():
    current_state = queue.get()

    # Check if the current state is the goal state
    if current_state.board == goal_state:
      # Return the sequence of moves required to solve the board
      return current_state.prev_move

    # Mark the current state as visited
    visited.add(tuple(current_state.board))

    # Generate the next states
    next_states = generate_next_states(current_state)

    for next_state in next_states:
      # Calculate the cost of reaching this state
      if strategy == "uniform_cost":
        cost = next_state.cost
    
      else:
  # Use the Hamming distance as the heuristics for A* search
        cost = next_state.cost + heuristics(next_state.board, goal_state)

# Add the next state to the queue if it has not been visited
      if tuple(next_state.board) not in visited:
        queue.put(next_state)

# Generates the next states that can be reached from the current state
def generate_next_states(current_state):
  next_states = []

  # Find the position of the empty cell (represented by 0)
  i, j = find_empty_cell(current_state.board)

  # Move the empty cell up, down, left, or right
  if i > 0:
    next_board = move(current_state.board, i, j, i-1, j)
    next_states.append(State(next_board, current_state.cost+1, current_state.prev_move+[(i, j, i-1, j)]))
  if i < 2:
    next_board = move(current_state.board, i, j, i+1, j)
    next_states.append(State(next_board, current_state.cost+1, current_state.prev_move+[(i, j, i+1, j)]))
  if j > 0:
    next_board = move(current_state.board, i, j, i, j-1)
    next_states.append(State(next_board, current_state.cost+1, current_state.prev_move+[(i, j, i, j-1)]))
  if j < 2:
    next_board = move(current_state.board, i, j, i, j+1)
    next_states.append(State(next_board, current_state.cost+1, current_state.prev_move+[(i, j, i, j+1)]))

  return next_states

# Moves the cell at (i, j) to (x, y) on the board and returns the resulting board
def move(board, i, j, x, y):
  new_board = [row[:] for row in board]
  new_board[x][y], new_board[i][j] = new_board[i][j], new_board[x][y]
  return new_board

# Finds the position of the empty cell (represented by 0) on the board
def find_empty_cell(board):
  for i in range(3):
    for j in range(3):
      if board[i][j] == 0:
        return i, j

# Calculates the Hamming distance between the current state and the goal state
def heuristics(current_state, goal_state):
  distance = 0
  for i in range(3):
    for j in range(3):
      if current_state[i][j] != goal_state[i][j]:
        distance += 1
  return distance


