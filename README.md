# Sorting via Array Reversion

## Introduction

In computer science, sorting algorithms range from simple and naive to complex and efficient. Most of these algorithms (such as bubble sort, insertion sort, binary sort, merge sort, heap sort) rely on the operation `exchange(arr,i,j)`, meaning to swap the elements at positions `i` and `j` in the array `arr`.

However, in a computational system, let's assume that the only operation allowed to modify the elements of an array is `reverse(arr,i)`, which reverses the order of elements in the array `arr` starting from position `i`. This means that instead of swapping elements directly, we can only reverse portions of the array. 

The goal is to implement sorting of any array using only reversals. The objective is to find the minimal number of reversals required to sort an array while minimizing the time required to solve the problem.

## Implemented Search Methods

To solve the problem, the following search methods are implemented:

## Implemented Search Methods

To tackle the array sorting problem using only array reversion operations, several search methods have been implemented:

### Depth-First Search (DFS)
- **Algorithm**: DFS delves as deeply as possible along each branch of the search tree before backtracking. It employs a stack to manage the search frontier, expanding nodes in a depth-first manner.
- **How it works**: DFS systematically explores each branch of the search tree, traversing as deeply as possible until a solution is found or all nodes have been visited. It prioritizes exploring the deepest unexplored node first, which may lead to long paths before discovering a solution.
- **Complexity**: In the worst-case scenario, where the solution is located deep in the search tree, DFS exhibits exponential time complexity, typically expressed as O(b^m), where b is the branching factor and m is the maximum depth of the search tree.

### Breadth-First Search (BFS)
- **Algorithm**: BFS systematically explores all neighbor nodes at the present depth level before moving to the nodes at the next depth level. It uses a queue data structure to maintain the search frontier, expanding nodes level by level.
- **How it works**: BFS methodically examines all nodes at a given depth level before proceeding to the next level. This approach ensures that the shallowest solution is found first, guaranteeing optimality in terms of path length.
- **Complexity**: In the worst-case scenario, BFS may need to explore the entire search tree, resulting in exponential time complexity, typically O(b^d), where b is the branching factor and d is the depth of the shallowest solution.

### Random Search
- **Algorithm**: Random search selects actions randomly without considering the structure of the search space or the quality of solutions. It explores the search space in a non-deterministic manner.
- **How it works**: Random search randomly selects actions from the available set of moves at each step. This approach does not rely on any heuristics or systematic exploration strategies, making it highly unpredictable.
- **Complexity**: Random search does not guarantee any specific time complexity as it depends on the probability of randomly selecting the correct actions. However, in terms of space complexity, it typically requires linear space, O(n), where n is the size of the search space.

### A* Search
- **Algorithm**: A* search is an informed search algorithm that evaluates nodes based on a combination of the cost function (g) and the heuristic function (h). It aims to find the most efficient path from the initial state to the goal state.
- **How it works**: A* evaluates nodes by considering both the cost of reaching the current node (g) and an estimate of the cost from the current node to the goal (h). It selects the node with the lowest total cost f = g + h for expansion.
- **Complexity**: The time complexity of A* search depends on the quality of the heuristic function and the size of the search space. In general, it is expressed as O(b^d), where b is the branching factor and d is the depth of the solution. The space complexity is also influenced by the heuristic quality and typically ranges from linear to exponential in the size of the search space.

### Custom Heuristic
- **Algorithm**: Custom heuristic allows the definition of a specialized heuristic function tailored to the problem's characteristics. It provides flexibility in designing heuristics that exploit domain-specific knowledge.
- **How it works**: Custom heuristics are user-defined functions that estimate the distance from the current state to the goal state. By incorporating domain-specific knowledge, custom heuristics can guide the search towards more promising regions of the search space.
- **Complexity**: The complexity of custom heuristics depends on the specific implementation and the problem domain. It may vary from linear to exponential in the size of the search space, depending on the heuristic's effectiveness and computational requirements.

These search methods offer different trade-offs between solution optimality, time complexity, and space complexity. By comparing their performance, we can determine the most suitable approach for solving the array sorting problem using array reversion operations.

## Complexity Analysis

| Search Method       | Time Complexity      | Space Complexity  |
|---------------------|----------------------|-------------------|
| Depth-First Search  | O(b^m)               | O(m)              |
| Breadth-First Search| O(b^d)               | O(b^d)            |
| Random Search       | Dependent on actions | O(n)              |
| A* Search           | O(b^d)               | Varies            |

- **b**: Branching factor (average number of successors per state/the average number of options at each decision point in a search) 
- **m**: Maximum depth of the search tree
- **d**: Depth of the shallowest solution
- **n**: Size of the search space
- 
## Example Output for Heuristic (A* SEARCH)

The following output demonstrates the solution path and heuristic values obtained using a custom heuristic where:
- g = 0
- h: For each element, calculate the sum of the number of elements greater on the left and the number of elements smaller on the right.
  
'''
- Current State: [4, 5, 1, 3, 2], Heuristic Value: 14
- Current State: [2, 3, 1, 5, 4], Heuristic Value: 6
- Current State: [2, 3, 1, 4, 5], Heuristic Value: 4
- Current State: [2, 3, 5, 4, 1], Heuristic Value: 10
- Current State: [2, 1, 4, 5, 3], Heuristic Value: 6
- Current State: [2, 1, 3, 5, 4], Heuristic Value: 4
- Current State: [2, 1, 3, 4, 5], Heuristic Value: 2
- Current State: [2, 1, 5, 4, 3], Heuristic Value: 8
- Current State: [2, 1, 5, 3, 4], Heuristic Value: 6
- Current State: [2, 1, 4, 3, 5], Heuristic Value: 4
- Current State: [2, 5, 3, 4, 1], Heuristic Value: 12
- Current State: [1, 4, 3, 5, 2], Heuristic Value: 8
- Current State: [1, 2, 5, 3, 4], Heuristic Value: 4
- Current State: [1, 2, 4, 3, 5], Heuristic Value: 2
- Current State: [1, 2, 4, 5, 3], Heuristic Value: 4
- Current State: [1, 2, 3, 5, 4], Heuristic Value: 2
- Time taken by A* Search: 0.001984 seconds
- States visited by A* Search: 16
- Sorted array found: [1, 2, 3, 4, 5], Heuristic Value: 0


## License
All rights reserved.

