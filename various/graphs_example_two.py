"""
You are given a 2d grid of `"1"`s and `"0"`s that represents a "map". The
`"1"`s represent land and the `"0"s` represent water.
You need to write a function that, given a "map" as an argument, counts the
number of islands. Islands are defined as adjacent pieces of land that are
connected horizontally or vertically. You can also assume that the edges of the
map are surrounded by water.
Example 1:
Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
Example 2:
Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
"""
from collections import deque

def numIslands(grid):
    # Your code here
    num_islands = 0


    #need to iterate through the map
    for i, row in enumerate(grid):
        for j, loc in enumerate(row):
            #what to do when we see a 1?
            #figure out how big is the island. an island consists of single 1 or connected 1s

            if loc == "1":
                num_islands += 1


            #when we find a 1, we check right and down
            

            #how do we avoid counting 1s that we have seen before
            #toogle any 1s we have seen to 0 to avoid double counting
        