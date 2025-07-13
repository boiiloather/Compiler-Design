from solution import count

# Test case 1: N=6 (should form levels 1,2,3 with 1,2,3 nodes)
# Let's create a simple linear tree: 1-2-3-4-5-6
# This would have:
# Level 1: node 1 (1 node) ✓
# Level 2: node 2 (1 node) - should be 2 nodes
# Level 3: node 3 (1 node) - should be 3 nodes  
# Level 4: node 4 (1 node) - should not exist
# Level 5: node 5 (1 node) - should not exist
# Level 6: node 6 (1 node) - should not exist

N = 6
M = 5  # 5 edges for 6 nodes
Two = 2  # 2 columns per edge
Edges = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6]]

result = count(N, M, Two, Edges)
print(f"Test 1 - Linear tree with N=6: {result}")

# Test case 2: N=6 - Already equalized tree
# Level 1: node 1 (1 node)
# Level 2: nodes 2,3 (2 nodes)  
# Level 3: nodes 4,5,6 (3 nodes)
# Tree structure: 1 -> 2,3 and 2 -> 4,5 and 3 -> 6
Edges2 = [[1, 2], [1, 3], [2, 4], [2, 5], [3, 6]]

result2 = count(N, M, Two, Edges2)
print(f"Test 2 - Already equalized tree with N=6: {result2}")

# Test case 3: N=3 (should form levels 1,2 with 1,2 nodes)
N3 = 3
M3 = 2
Edges3 = [[1, 2], [2, 3]]  # Linear: 1-2-3

result3 = count(N3, M3, Two, Edges3)
print(f"Test 3 - Linear tree with N=3: {result3}")