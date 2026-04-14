#Expected result = 7
from math import inf
input_1 = [
    [1,3,1],
    [1,5,1],
    [4,2,1]]

"""
UNDERSTAND
Smallest grid [[0]]

Return -> Value of cheapest path

MATCH
- Optimization problem
- Memoization helpful?
- Shortest path 
-Dijkstra's algo?

Dynamic Programming
"""
def cheapest_route(grid):
    height = len(grid)
    width = len(grid[0])
        #Set up a second grid for costs
    best_value = []
    for i in range(height):
        best_value.append([None]*width)
    #print (best_value)

    # Initialize the starting position
    best_value[0][0] = grid [0][0]

    # Build a helper function to get value of a cell
    def get_value(row, col):
        if row < 0 or col < 0:
            return inf
        if best_value[row][col] == None:
             # If value is not in helper grid
            value = min(
                get_value(row - 1, col),
                get_value(row, col-1)
            ) +grid[row][col]
       
            # Value = min(above, left) + grid
            # Store value in helper grid
            best_value[row][col] = value
        # return it from helper grid
        return best_value[row][col]

       #Get value of lower-right and return 
    result = get_value(height-1, width-1)
    #print(best_value)
    return result


print(cheapest_route(input_1))

