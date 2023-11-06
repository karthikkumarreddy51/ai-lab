from collections import deque
class State:
    def __init__(self, missionaries, cannibals, boat):
        self.m = missionaries
        self.c = cannibals
        self.b = boat
    def __eq__(self, other):
        return self.m == other.m and self.c == other.c and self.b == other.b
    def __hash__(self):
        return hash((self.m, self.c, self.b))
M=int(input("Enter the missionaries :"))
C=int(input("Enter the cannibals :"))# Define the initial state and goal state
initial_state = State(M, C, 1)  # (Missionaries on the left, Cannibals on the left, Boat position)
goal_state = State(0, 0, 0)     # (Missionaries on the right, Cannibals on the right, Boat position)
def is_valid_state(state):
    m, c, b = state.m, state.c, state.b
    return 0 <= m <= M and 0 <= c <= C and (m == 0 or m >= c) and ((M - m) == 0 or (M - m) >= (C - c))
def get_next_states(state):
    moves = [(1, 0), (2, 0), (0, 1), (0, 2), (1, 1)]
    next_states = []
    for move in moves:
        if state.b == 1:  # Boat on the left
            new_state = State(state.m - move[0], state.c - move[1], 0)
        else:  # Boat on the right
            new_state = State(state.m + move[0], state.c + move[1], 1)
        if is_valid_state(new_state):
            next_states.append(new_state)
    return next_states
def dfs_search():
    visited = set()
    stack = deque([(initial_state, [])])
    while stack:
        current_state, path = stack.pop()
        if current_state == goal_state:
            return path
        if current_state not in visited:
            visited.add(current_state)
            for next_state in get_next_states(current_state):
                stack.append((next_state, path + [next_state]))
solution = dfs_search()
if solution:
    print("Solution found:")
    for i, state in enumerate(solution):
        moved_m = abs(state.m - solution[i-1].m) if i >= 0 else 0
        moved_c = abs(state.c - solution[i-1].c) if i >= 0 else 0
        boat = "Left" if state.b == 1 else "Right"
        m, c = M - state.m, C - state.c
        print(f"Step {i + 1}: {moved_m}M {moved_c}C moved from {'Right' if state.b == 1 else 'Left'} to {'Right' if state.b == 0 else 'Left'}")
        print(f"{state.m}M {state.c}C are on Left Side")
        print(f"{m}M {c}C are on Right Side")
        print(f"Boat: {boat} side")
        print()
else:
    print("No solution found.")




