import sys
from collections import defaultdict, deque

def count(N, M, Two, Edges):
    """
    Calculate minimum operations to make tree equalized.
    
    An equalized tree has exactly i nodes at level i for all valid levels.
    """
    # Build adjacency list representation of the tree
    adj = defaultdict(list)
    for edge in Edges:
        u, v = edge[0], edge[1]
        adj[u].append(v)
        adj[v].append(u)
    
    # Find the root - assume it's node 1, or use first node if 1 doesn't exist
    root = 1
    if root not in adj and Edges:
        root = Edges[0][0]
    
    # BFS to find current level distribution
    def get_level_distribution(root):
        visited = set()
        queue = deque([(root, 1)])  # (node, level)
        visited.add(root)
        level_count = defaultdict(int)
        
        while queue:
            node, level = queue.popleft()
            level_count[level] += 1
            
            for neighbor in adj[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, level + 1))
        
        return level_count
    
    current_levels = get_level_distribution(root)
    
    # Calculate what k should be for N nodes
    # We need 1 + 2 + 3 + ... + k = N
    k = 1
    while k * (k + 1) // 2 < N:
        k += 1
    
    # Verify that N can form a perfect equalized tree
    if k * (k + 1) // 2 != N:
        return -1  # Shouldn't happen according to problem statement
    
    # Calculate minimum operations needed
    operations = 0
    
    # Count all nodes that need to be moved
    for level in current_levels:
        current_at_level = current_levels[level]
        
        if level <= k:
            # This level should exist in the target tree
            target_at_level = level
            if current_at_level > target_at_level:
                # We have excess nodes at this level that need to be moved
                operations += current_at_level - target_at_level
        else:
            # This level should not exist in the target tree
            # All nodes at this level need to be moved
            operations += current_at_level
    
    return operations

def main():
    N = int(sys.stdin.readline().strip())
    M = int(sys.stdin.readline().strip())
    Two = int(sys.stdin.readline().strip())
    
    Edges = []
    for _ in range(M):
        Edges.append(list(map(lambda x: int(x), sys.stdin.readline().strip().split())))
    
    result = count(N, M, Two, Edges)
    print(result)

if __name__ == "__main__":
    main()