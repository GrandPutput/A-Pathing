from simpleai.search import SearchProblem, astar
import copy

# Instructions for finding simpleai algorithms!!!
'''
A* search.
If graph_search=True, will avoid exploring repeated states.
Requires: SearchProblem.actions, SearchProblem.result,
SearchProblem.is_goal, SearchProblem.cost, and SearchProblem.heuristic.
    All Taken from traditional.py
See models.py in simpleai for SearchProblem guide.    
'''

# Pathfinder Class 
class PathFinder(SearchProblem):
    def __init__(self, maze, start, goal):
        self.maze = maze
        self.goal = goal
        super(PathFinder, self).__init__(initial_state=start)

    def actions(self, state):
        actions = []
        # Directions (down, up, left, right)
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for direction in directions:
            future_state = (state[0] + direction[0], state[1] + direction[1])
            if 0 <= future_state[0] < len(self.maze) and 0 <= future_state[1] < len(self.maze[0]) and self.maze[future_state[0]][future_state[1]] == 0:
                actions.append(future_state)
        print(f"Actions from state {state}: {actions}")
        return actions

    def result(self, state, action):
        print(f"Result of action {action} from state {state}: {action}")
        return action

    def is_goal(self, state):
        is_goal = state == self.goal
        print(f"Checking if state {state} is goal: {is_goal}")
        return is_goal

    def heuristic(self, state):
        heuristic_value = abs(state[0] - self.goal[0]) + abs(state[1] - self.goal[1])
        print(f"Heuristic value for state {state}: {heuristic_value}") # Can also modify cost function to output cost
        return heuristic_value

def print_maze(maze, path):
    for position in path:
        maze[position[0]][position[1]] = '*'
    for row in maze:
        print(" ".join(str(cell) for cell in row))

if __name__ == "__main__":
    print("Starting Pathfinder!!!")
    # Original Maze
    original_maze = [
        [0, 1, 0, 0, 0, 0, 0],
        [0, 1, 0, 1, 0, 1, 0],
        [0, 0, 0, 1, 0, 1, 0],
        [1, 0, 1, 0, 0, 1, 0],
        [0, 0, 1, 0, 1, 0, 0],
        [0, 1, 1, 1, 1, 0, 1],
        [0, 0, 1, 0, 1, 0, 0],
        [1, 0, 1, 0, 0, 1, 0],
        [0, 0, 0, 1, 0, 0, 0],
        [0, 1, 0, 1, 1, 0, 1],
        [0, 1, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 0, 1, 1, 1]
    ]

    # Start and Goal can be change to functions to take input as player and npc loctions.
    start = (0, 0)
    goal = (12, 3)

    # Added for future testing and modification
    i = 0 

    # Looping can be modified for possible input as player and NPC positions
    while i < 1:
        # Copy is for testing itterations
        maze = copy.deepcopy(original_maze)
        # Visited not needed, remove in the future
        # visited = set() # Prevent visiting same states. Not needed as simpleai handles on its own
        problem = PathFinder(maze, start, goal)
        result = astar(problem)
        
        path = [step[1] for step in result.path()]

        print(f"Run #{i + 1}")
        print("Path from start to goal:")
        print(path)
        print("\nMaze with path:")
        print_maze(maze, path)
        print("\n")

        i = i + 1