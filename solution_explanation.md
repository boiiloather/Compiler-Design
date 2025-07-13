# Tree Equalization Solution

## Problem Summary

Given a tree with N nodes, we need to find the minimum number of operations to make it "equalized". An equalized tree has the property that level i contains exactly i nodes, where level is defined as the number of nodes on the path from root to that node.

## Solution Approach

### 1. Understanding the Target Structure

For an equalized tree:
- Level 1: 1 node (root)
- Level 2: 2 nodes
- Level 3: 3 nodes
- ...
- Level k: k nodes

The maximum complete level k is found such that 1 + 2 + ... + k ≤ N.
If there are remaining nodes after k complete levels, they go to level k+1.

### 2. Algorithm Steps

1. **Build the tree**: Create adjacency list from edges
2. **Find current distribution**: Use BFS to count nodes at each level
3. **Calculate target distribution**: Determine ideal level distribution
4. **Count operations**: Sum up excess nodes that need to be moved

### 3. Key Insights

- We only need to count nodes that are in excess at each level
- Each excess node requires one operation to move it to a different level
- We don't need to track where nodes are moved to, just count excess nodes

### 4. Time Complexity

- Building adjacency list: O(M) where M is number of edges
- BFS traversal: O(N) where N is number of nodes
- Calculating operations: O(levels)
- Overall: O(N + M) = O(N) since M = N-1 for a tree

### 5. Test Cases

| Test Case | N | Current Structure | Target Structure | Operations |
|-----------|---|-------------------|------------------|------------|
| Linear (3) | 3 | [1,1,1] | [1,2] | 1 |
| Star (5) | 5 | [1,4] | [1,2,2] | 2 |
| Perfect (6) | 6 | [1,2,3] | [1,2,3] | 0 |
| Perfect (10) | 10 | [1,2,3,4] | [1,2,3,4] | 0 |

### 6. Edge Cases Handled

- Single node (N=1): Returns 0
- Empty edge list: Returns 0
- Already equalized trees: Returns 0
- Trees with remaining nodes: Places them at level k+1

## Implementation Notes

- Uses BFS for level traversal
- Handles arbitrary node numbering by using min(nodes) as root
- Robust error handling for edge cases
- Clear variable names and documentation