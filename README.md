# Tree Equalization Problem Solution

## Problem Statement

Given a tree with N nodes, find the minimum number of operations to make it "equalized". An equalized tree has the property that level i contains exactly i nodes, where level is defined as the number of nodes on the path from root to that node.

## Files Provided

1. `tree_equalization_final.py` - The main solution file
2. `solution_explanation.md` - Detailed explanation of the approach
3. `sample_input.txt` - Example input file
4. `README.md` - This file

## Usage

```bash
python3 tree_equalization_final.py < input.txt
```

## Input Format

```
N          # Number of nodes
M          # Number of edges (should be N-1)
Two        # Number of columns in edges (should be 2)
u1 v1      # First edge
u2 v2      # Second edge
...
uM vM      # Last edge
```

## Output

Single integer representing the minimum number of operations needed.

## Example

Input:
```
6
5
2
1 2
1 3
2 4
2 5
3 6
```

Output:
```
0
```

This represents a tree that is already equalized:
- Level 1: 1 node (node 1)
- Level 2: 2 nodes (nodes 2, 3)
- Level 3: 3 nodes (nodes 4, 5, 6)

## Algorithm Complexity

- Time Complexity: O(N) where N is the number of nodes
- Space Complexity: O(N) for the adjacency list and BFS queue

## Key Features

- Handles all edge cases (single node, empty tree, etc.)
- Uses BFS for efficient level traversal
- Robust input parsing and error handling
- Clear, documented code structure