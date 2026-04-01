'''
# Problem: Path with Minimum Effort

You are a hiker preparing for an upcoming hike. You are given `heights`, a 2D array of size $rows \times columns$, where `heights[row][col]` represents the height of cell `(row, col)`. You are situated in the top-left cell, `(0, 0)`, and you hope to travel to the bottom-right cell, `(rows-1, columns-1)`.

**The Goal:** Find a path that minimizes the **effort** required. Return the effort value for the best path possible.

**The Constraints**

- You can move **up**, **down**, **left**, or **right**.
- A path's **effort** is the **maximum absolute difference** in heights between two consecutive cells of the path.

**Example**

- **Input:** `heights = [[1,2,2],[3,8,2],[5,3,5]]`
- **Output:** `2`
- **Explanation:** The path `[1,3,5,3,5]` has a maximum difference of 2, which is better than the "shorter" path `[1,2,2,2,5]` which has a maximum difference of 3.
'''

heights_1 = [
    [1,2,2],
    [3,8,2],
    [5,3,5]]
result_1 = 2

heights_2 = [
    [1,2,3,4],
    [6,7,6,5],
    [5,4,3,2]]
result_2 = 1

import heapq

def min_effort(heights):
    start = (0,0)
    rows = len(heights)
    cols = len(heights[0])
    finish = (rows-1, cols-1)
    print(start, finish)

    # Using Djikstra
    # Start has cost 0 - we're already there
    # Each adjacent node (NSEW) has cost of:
    #   max(this cost, cost to get there)
    # cost to get there = abs(this node - that node)

    heap = []
    heapq.heappush(heap, (0, start))
    
    def neighbors(pos):
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        result = []
        for d in directions:
            p = (pos[0] + d[0], pos[1] + d[1])
            if (p[0] >= 0 and p[0] < rows and p[1] >= 0 and p[1] < cols):
                result.append(p)
        return result
    
    while heap:
        cost, position = heapq.heappop(heap)

        if position == finish:
            return cost

        val = heights[position[0]][position[1]]
        for neighbor in neighbors(position):
            n_val = heights[neighbor[0]][neighbor[1]]
            step_cost = abs(val - n_val)
            # print(cost, val, n_val, step_cost)
            path_cost = max(cost, step_cost)
            heapq.heappush(heap, (path_cost, neighbor))

print(min_effort(heights_1))