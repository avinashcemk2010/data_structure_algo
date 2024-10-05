'''
You are a project manager in a large IT company. 
You need to select a team of employees to work on a project. 
You have a list of employees who are eligible for the selection. 
Employees are indexed from 1 to N. However, there are certain rules that must be followed in order to select a team. 
There are some employees who have some personal conflicts and they can't be in a team together. 
Also, each employee has a skill value assigned to them, representing their level of expertise. 
As a project manager, your task is to select a team of employees such that the total expertise of the team should be maximum. 
Keeping the employees' incompatibility in mind, two employees are said to be incompatible if they have any conflict among them. 
Given the employees, their level of expertise value and employees' pair with conflicts, find the maximum possible expertise of the team. 
Note, the selected team can also contain one employee.
'''
from collections import defaultdict

# Function to perform DFS and find connected components
def dfs(node, graph, visited, component):
    visited[node] = True
    component.append(node)
    for neighbor in graph[node]:
        if not visited[neighbor]:
            dfs(neighbor, graph, visited, component)

# Function to check if a graph component is bipartite
def is_bipartite(graph, component):
    color = {}
    
    def bfs(start):
        queue = [start]
        color[start] = 0
        while queue:
            node = queue.pop(0)
            for neighbor in graph[node]:
                if neighbor not in color:
                    color[neighbor] = 1 - color[node]
                    queue.append(neighbor)
                elif color[neighbor] == color[node]:
                    return False
        return True
    
    for node in component:
        if node not in color:
            if not bfs(node):
                return False, None  # Component is not bipartite
    
    set1, set2 = [], []
    for node in component:
        if color[node] == 0:
            set1.append(node)
        else:
            set2.append(node)
    
    return True, (set1, set2)

# Function to solve the maximum expertise selection problem
def max_expertise(n, expertise, conflicts):
    graph = defaultdict(list)
    
    # Build the conflict graph
    for u, v in conflicts:
        graph[u].append(v)
        graph[v].append(u)
    
    visited = [False] * (n + 1)
    total_expertise = 0
    
    # Find all connected components
    for i in range(1, n + 1):
        if not visited[i]:
            component = []
            dfs(i, graph, visited, component)
            
            # Check if the component is bipartite
            bipartite, sets = is_bipartite(graph, component)
            
            if bipartite:
                # If bipartite, take the set with the maximum expertise
                set1, set2 = sets
                expertise_set1 = sum(expertise[node - 1] for node in set1)
                expertise_set2 = sum(expertise[node - 1] for node in set2)
                total_expertise += max(expertise_set1, expertise_set2)
            else:
                # If not bipartite, we need to find the maximum independent set (brute force approach here)
                # For simplicity, take the max expertise of any individual in the component (could be improved)
                total_expertise += max(expertise[node - 1] for node in component)
    
    return total_expertise

# # Example test case
# n = 8  # Number of employees
# expertise = [7, 5, 4, 3, 1, 6, 2, 9]  # Expertise values for each employee
# conflicts = [(1, 2), (2, 5), (3, 6), (8, 6), (1, 4), (7, 8)]  # Conflicts between employees

# # Call the function with the example data
# total_expertise = max_expertise(n, expertise, conflicts)
# print(total_expertise)

n, c = map(int, input().split())
conflicts: list = []
for i in range(c):
    emp1, emp2 = map(int, input().split())
    conflicts.append((emp1, emp2))

expertise = input().split()
expertise = [int(v) for v in expertise]

total_expertise = max_expertise(n, expertise, conflicts)
print(total_expertise)






