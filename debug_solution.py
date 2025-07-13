import sys
from collections import defaultdict, deque

def count(N, M, Two, Edges):
    # Build adjacency list representation of the tree
    adj = defaultdict(list)
    for edge in Edges:
        u, v = edge[0], edge[1]
        adj[u].append(v)
        adj[v].append(u)
    
    # Find the root - assume it's node 1 (or the first node that appears)
    root = 1
    if root not in adj:
        root = Edges[0][0]  # Use first node if 1 doesn't exist
    
    print(f"Root: {root}")
    print(f"Adjacency list: {dict(adj)}")
    
    # BFS to find current level distribution
    def get_level_distribution(root):
        visited = set()
        queue = deque([(root, 1)])  # (node, level)
        visited.add(root)
        level_count = defaultdict(int)
        
        while queue:
            node, level = queue.popleft()
            level_count[level] += 1
            print(f"Node {node} at level {level}")
            
            for neighbor in adj[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, level + 1))
        
        return level_count
    
    current_levels = get_level_distribution(root)
    print(f"Current level distribution: {dict(current_levels)}")
    
    # Calculate what k should be for N nodes
    # We need 1 + 2 + 3 + ... + k = N
    k = 1
    while k * (k + 1) // 2 < N:
        k += 1
    
    print(f"k = {k}, sum = {k * (k + 1) // 2}")
    
    # Verify that N can form a perfect equalized tree
    if k * (k + 1) // 2 != N:
        return -1  # Shouldn't happen according to problem statement
    
    # Calculate minimum operations needed
    operations = 0
    
    # For each level, count how many nodes need to be moved
    for level in range(1, k + 1):
        current_at_level = current_levels.get(level, 0)
        target_at_level = level
        
        print(f"Level {level}: current = {current_at_level}, target = {target_at_level}")
        
        if current_at_level > target_at_level:
            # We have excess nodes at this level that need to be moved
            excess = current_at_level - target_at_level
            operations += excess
            print(f"  Excess: {excess}")
    
    print(f"Total operations: {operations}")
    return operations

# Test case 1: Linear tree
print("=== Test 1: Linear tree 1-2-3-4-5-6 ===")
N = 6
M = 5
Two = 2
Edges = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6]]
result = count(N, M, Two, Edges)
print(f"Result: {result}")
print()

# Test case 2: Already equalized tree
print("=== Test 2: Already equalized tree ===")
Edges2 = [[1, 2], [1, 3], [2, 4], [2, 5], [3, 6]]
result2 = count(N, M, Two, Edges2)
print(f"Result: {result2}")