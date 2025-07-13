import sys
from collections import defaultdict, deque

def count(N, M, Two, Edges):
    """
    Find the minimum number of operations to make a tree equalized.
    
    An equalized tree has the property that level i contains exactly i nodes
    for i = 1, 2, 3, ... where level is defined as the number of nodes on the
    path from root to that node.
    
    Args:
        N: Number of nodes in the tree
        M: Number of edges (should be N-1 for a tree)
        Two: Number of columns in Edges (should be 2)
        Edges: List of edges, each edge is [u, v]
    
    Returns:
        Minimum number of operations needed
    """
    
    # Handle edge case of single node
    if N == 1:
        return 0
    
    # Build adjacency list representation of the tree
    adj = defaultdict(list)
    for edge in Edges:
        u, v = edge[0], edge[1]
        adj[u].append(v)
        adj[v].append(u)
    
    # Find all nodes and use the smallest as root
    nodes = set()
    for edge in Edges:
        nodes.add(edge[0])
        nodes.add(edge[1])
    
    if not nodes:
        return 0
    
    root = min(nodes)
    
    # BFS to find current level distribution
    queue = deque([(root, 1)])  # (node, level)
    visited = set([root])
    level_count = defaultdict(int)
    
    while queue:
        node, level = queue.popleft()
        level_count[level] += 1
        
        for neighbor in adj[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, level + 1))
    
    # Calculate target level distribution for equalized tree
    # Level i should have i nodes for i = 1, 2, 3, ...
    # Find the maximum level k such that 1 + 2 + ... + k <= N
    k = 1
    total = 0
    while total + k <= N:
        total += k
        k += 1
    k -= 1  # k is now the maximum complete level
    
    # Build target distribution
    target_levels = {}
    for i in range(1, k + 1):
        target_levels[i] = i
    
    # If there are remaining nodes after complete levels, they go to level k+1
    remaining = N - total
    if remaining > 0:
        target_levels[k + 1] = remaining
    
    # Calculate operations needed
    operations = 0
    
    # Count nodes that are at wrong levels (excess nodes that need to be moved)
    max_level = max(max(level_count.keys()) if level_count else 0, 
                   max(target_levels.keys()) if target_levels else 0)
    
    for level in range(1, max_level + 1):
        current = level_count.get(level, 0)
        target = target_levels.get(level, 0)
        
        if current > target:
            # We have excess nodes at this level that need to be moved
            operations += current - target
    
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